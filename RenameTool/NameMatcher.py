import re
from pathlib import Path
import os

name_pattern = re.compile(r'([CcSsVvPpWwAaMm])([0-9]{3})_([\S][^-\s]*)_([\S][^-\s]*)_([Vv])([0-9]{3})')

def match_file_name_pattern(filename):
    basename,ext = os.path.splitext(filename)
    m = name_pattern.match(basename)
    
    # TODO: infer Type from each group values, c = Character, P = Prop etc.
    
    print(filename,ext,m)
    return m

def match_extension(extension):
    pass

'''
Unit Test for Name Matcher
'''
import unittest

class TestNameMatcher(unittest.TestCase):
    def test_name_match(self):
        self.assertIsNot(match_file_name_pattern('s001_EstherianRuin_MODELH_V001.pnga'),None)
        self.assertIs(match_file_name_pattern('s001_EstherianRuin_MODE-LH_V001.pnga'),None)
        self.assertIs(match_file_name_pattern('s001_EstherianRuin_MODE LH_V001.pnga'),None)
        self.assertIs(match_file_name_pattern('s001_Esther-ianRuin_MODELH_V001.pnga'),None)
        self.assertIs(match_file_name_pattern('s001_Esther ianRuin_MODELH_V001.pnga'),None)
        
if __name__ == '__main__':
    unittest.main()
