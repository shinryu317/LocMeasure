# -*- coding: utf-8 -*-
import sys
import unittest

sys.path.append('../loc_measure')
from loc_measure import LocMeasure


class TestCount(unittest.TestCase):
    def setUp(self):
        cfg_file = '../loc_measure/config.json'
        self.loc_measure = LocMeasure(cfg_file)

    def test_loc_cpp(self):
        self.loc_measure.language = 'C/C++'
        self.assertEqual(self.loc_measure.count('code.cpp'), 9)

    def test_loc_py(self):
        self.loc_measure.language = 'Python'
        self.assertEqual(self.loc_measure.count('code.py'), 16)

    def test_loc_java(self):
        self.loc_measure.language = 'Java'
        self.assertEqual(self.loc_measure.count('code.java'), 8)

    def test_loc_ruby(self):
        self.loc_measure.language = 'Ruby'
        self.assertEqual(self.loc_measure.count('code.rb'), 1)

    def test_loc_go(self):
        self.loc_measure.language = 'Go'
        self.assertEqual(self.loc_measure.count('code.go'), 5)

    def test_loc_r(self):
        self.loc_measure.language = 'R'
        self.assertEqual(self.loc_measure.count('code.r'), 1)

    def test_loc_sh(self):
        self.loc_measure.language = 'ShellScript'
        self.assertEqual(self.loc_measure.count('code.sh'), 2)

    def test_loc_perl(self):
        self.loc_measure.language = 'Perl'
        self.assertEqual(self.loc_measure.count('code.pl'), 2)

    def test_loc_php(self):
        self.loc_measure.language = 'PHP'
        self.assertEqual(self.loc_measure.count('code.php'), 2)

    def test_loc_lua(self):
        self.loc_measure.language = 'Lua'
        self.assertEqual(self.loc_measure.count('code.lua'), 1)

    def test_loc_fortran(self):
        self.loc_measure.language = 'Fortran'
        self.assertEqual(self.loc_measure.count('code.f'), 3)

    def test_loc_html(self):
        self.loc_measure.language = 'HTML'
        self.assertEqual(self.loc_measure.count('code.html'), 18)

    def test_loc_css(self):
        self.loc_measure.language = 'CSS'
        self.assertEqual(self.loc_measure.count('code.css'), 14)

    def test_loc_scala(self):
        self.loc_measure.language = 'Scala'
        self.assertEqual(self.loc_measure.count('code.scala'), 5)

    def test_set_none_to_language(self):
        with self.assertRaises(ValueError):
            self.loc_measure.language = None

    def test_language_is_none(self):
        with self.assertRaises(ValueError):
            self.loc_measure.count('code.cpp')
