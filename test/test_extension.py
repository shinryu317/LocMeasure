# -*- coding: utf-8 -*-
import sys
import unittest
from glob import glob

sys.path.append('../loc_measure')
from loc_measure import LocMeasure


class TestExtension(unittest.TestCase):
    def setUp(self):
        cfg_file = '../loc_measure/config.json'
        self.loc_measure = LocMeasure(cfg_file)

    def run_test(self, language, actual):
        self.loc_measure.language = language
        code_path_list = glob('code*.*')

        results = []
        for code_path in code_path_list:
            loc = self.loc_measure.count(code_path)
            if loc is not None:
                results.append(loc)
        self.assertEqual(len(results), actual)

    def test_for_c_cpp(self):
        self.run_test('C/C++', 3)

    def test_for_python(self):
        self.run_test('Python', 1)

    def test_for_java(self):
        self.run_test('Java', 1)

    def test_for_ruby(self):
        self.run_test('Ruby', 1)

    def test_for_go(self):
        self.run_test('Go', 1)

    def test_for_r(self):
        self.run_test('R', 1)

    def test_for_shellscript(self):
        self.run_test('ShellScript', 1)

    def test_for_perl(self):
        self.run_test('Perl', 1)

    def test_for_php(self):
        self.run_test('PHP', 1)

    def test_for_lua(self):
        self.run_test('Lua', 1)

    def test_for_fortran(self):
        self.run_test('Fortran', 1)

    def test_for_html(self):
        self.run_test('HTML', 1)

    def test_for_css(self):
        self.run_test('CSS', 1)

    def test_for_scala(self):
        self.run_test('Scala', 1)

if __name__ == '__main__':
    unittest.main()
