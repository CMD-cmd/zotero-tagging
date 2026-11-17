import importlib.util
import json
from pathlib import Path
import unittest
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('query', ROOT / 'scripts/query_taxonomy.py')
q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
T = json.loads((ROOT/'references/taxonomy.json').read_text())
def count(prefix):return sum(t['tag'].startswith(prefix) for t in T['terms'])

class QueryTests(unittest.TestCase):
    def test_index_is_compact(self):
        r = q.query_taxonomy()
        self.assertEqual(r['mode'], 'index'); self.assertNotIn('terms', r)
        self.assertEqual([x['code'] for x in r['dimensions']], ['A1','B1','B2','C1','C2','C3','D1','D2','D3','E1'])
        self.assertEqual(sum(x['count'] for x in r['dimensions']), T['canonical_count'])
    def test_dimension_boundaries(self):
        for code, prefix in [('C3','#Ｃ３Drug/'),('D3','#Ｄ３Phenotype/'),('A1','#Ａ１Type/')]:
            with self.subTest(code=code):
                r = q.query_taxonomy(dimensions=[code])
                self.assertEqual(r['total_matches'], count(prefix))
                self.assertTrue(all(t['tag'].startswith(prefix) for t in r['terms']))
    def test_combined_dimensions(self):
        self.assertEqual(q.query_taxonomy(dimensions=['A1','C1'])['total_matches'], count('#Ａ１Type/')+count('#Ｃ１Material/'))
    def test_keyword_and_alias(self):
        for text in ['SSRO','BSSO']:
            self.assertEqual([t['id'] for t in q.query_taxonomy(query=text)['terms']], ['ZT-050'])
    def test_stable_id(self):
        r=q.query_taxonomy(ids=['ZT-051'])
        self.assertTrue(r['terms'][0]['tag'].endswith('LeFort-I 截骨术'))
    def test_intersection(self):
        self.assertEqual(q.query_taxonomy(dimensions=['C1'],ids=['ZT-050'])['total_matches'], 0)
    def test_fullwidth_dimension(self):
        self.assertEqual(q.query_taxonomy(dimensions=['#Ｃ３Drug'])['total_matches'], count('#Ｃ３Drug/'))
    def test_pagination(self):
        r=q.query_taxonomy(all_terms=True,limit=50)
        self.assertEqual(r['total_matches'],T['canonical_count']);self.assertEqual(r['returned'],50);self.assertEqual(r['next_offset'],50)
        r=q.query_taxonomy(all_terms=True,offset=T['canonical_count']-4,limit=50)
        self.assertEqual(r['returned'],4);self.assertIsNone(r['next_offset'])
    def test_invalid_filters(self):
        for args in [{'dimensions':['Z9']},{'dimensions':['C10']},{'ids':['missing']},{'query':''},{'limit':0},{'offset':-1},{'all_terms':True,'dimensions':['A1']}]:
            with self.subTest(args=args),self.assertRaises(ValueError):q.query_taxonomy(**args)
    def test_vocabulary_can_grow(self):
        extended=json.loads(json.dumps(T))
        tag='#Ｅ１Method/TestModel 测试模型'
        extended['terms'].append({'id':'ZT-TEST','tag':tag,'definition':'test fixture','aliases':[]})
        extended['canonical_tags'].append(tag)
        extended['canonical_count']+=1
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'taxonomy.json';path.write_text(json.dumps(extended))
            with patch.object(q,'TAX_PATH',path):
                self.assertEqual(q.query_taxonomy()['canonical_count'],T['canonical_count']+1)
                self.assertEqual(q.query_taxonomy(ids=['ZT-TEST'])['terms'][0]['tag'],tag)
    def test_same_canonical_source(self):
        r=q.query_taxonomy(all_terms=True,limit=T['canonical_count'])
        source=json.loads((ROOT/'references/taxonomy.json').read_text())
        self.assertEqual(r['terms'],source['terms'])

if __name__=='__main__':unittest.main()
