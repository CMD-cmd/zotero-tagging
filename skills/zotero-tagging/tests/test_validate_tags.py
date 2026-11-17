import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('validator',ROOT/'scripts/validate_tags.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
T=json.loads((ROOT/'references/taxonomy.json').read_text())
TYPE='#Ａ１Type/Article 论著/Mechanistic 机制研究'
OTHER='#Ａ１Type/Article 论著/Biomaterial 生物材料研究'

class ValidatorTests(unittest.TestCase):
 def test_taxonomy_unique(self):
  self.assertEqual(len(T['canonical_tags']),154)
  self.assertEqual(len(set(T['canonical_tags'])),154)
  self.assertEqual(len({t['id'] for t in T['terms']}),154)
 def test_all_renames(self):
  for old,new in T['rename_map'].items():
   with self.subTest(old=old):
    existing=[old] if old.startswith('#Ａ１Type/') else [TYPE,old]
    r=v.validate_and_merge([],existing,mode='rename-only')
    self.assertTrue(r['valid']);self.assertIn(new,r['final_tags'])
    self.assertNotIn('~ZTag-V2',r['final_tags'])
 def test_user_tags_survive(self):
  r=v.validate_and_merge([OTHER],[TYPE,'#用户/线索','/自定状态','/reading','重要'],mode='replace-managed')
  self.assertTrue(r['valid'])
  for tag in ['#用户/线索','/自定状态','/reading','重要']:self.assertIn(tag,r['final_tags'])
  self.assertNotIn(TYPE,r['final_tags'])
 def test_add_preserves(self):
  r=v.validate_and_merge(['#Ｄ３Phenotype/Osteogenesis 成骨与骨再生'],[TYPE,'/unread'])
  self.assertTrue(r['valid']);self.assertIn(TYPE,r['final_tags'])
 def test_type_conflict(self):
  self.assertFalse(v.validate_and_merge([OTHER],[TYPE])['valid'])
 def test_unknown_proposal(self):
  self.assertFalse(v.validate_and_merge(['#陌生/词'],[TYPE])['valid'])
 def test_explicit_reading_status(self):
  r=v.validate_and_merge([],[TYPE,'/reading','/自定状态'],status='/Done')
  self.assertTrue(r['valid']);self.assertNotIn('/reading',r['final_tags']);self.assertIn('/Done',r['final_tags']);self.assertIn('/自定状态',r['final_tags'])
 def test_reading_conflict(self):
  self.assertFalse(v.validate_and_merge(['/Done'],[TYPE,'/reading'])['valid'])
 def test_bad_inputs(self):
  for args in [(None,[]),([3],[]),([],{})]:self.assertFalse(v.validate_and_merge(*args)['valid'])
 def test_no_marker_preserves_existing(self):
  r=v.validate_and_merge([],[TYPE,'~ZTag-V2'],add_marker=False)
  self.assertTrue(r['valid']);self.assertIn('~ZTag-V2',r['final_tags'])

if __name__=='__main__':unittest.main()
