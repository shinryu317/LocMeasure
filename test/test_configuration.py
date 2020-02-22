# -*- coding: utf-8 -*-
import sys
import unittest

sys.path.append('../loc_measure')
from loc_measure import LocMeasure


class TestConfiguration(unittest.TestCase):
    def test_not_exist_cfg(self):
        cfg_file = '../loc_measure/dummy.json'
        with self.assertRaises(FileNotFoundError):
            _ = LocMeasure(cfg_file)
