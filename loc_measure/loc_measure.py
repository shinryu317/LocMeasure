# -*- coding: utf-8 -*-
import json
import os
import re


class LocMeasure():
    '''
    LOC:Line-Of-Code
    '''

    def __init__(self, cfg_file):
        self._language = None
        if not os.path.exists(cfg_file):
            raise FileNotFoundError('Not found configuration file: {}'.format(cfg_file))
        with open(cfg_file, 'r') as f:
            self.cfg = json.loads(f.read())

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language):
        try:
            self._language = language
            self.single_line_comment_mark = self.cfg[language]['single_line_comment_mark']
            self.multi_line_comment_mark = self.cfg[language]['multi_line_comment_mark']
        except KeyError as e:
            raise ValueError('Unsupported language: {}'.format(language)) from e

    def is_blank_line(self, line):
        return line == ''

    def is_single_line_comment(self, line):
        if isinstance(self.single_line_comment_mark, str):
            if self.single_line_comment_mark == '':
                return False
            return line.startswith(self.single_line_comment_mark)
        elif isinstance(self.single_line_comment_mark, list):
            for comment_mark in self.single_line_comment_mark:
                if line.startswith(comment_mark):
                    return True
            return False
        else:
            raise ValueError('single_line_comment must be str or list of str.')

    def is_multi_line_comment(self, line):
        if len(self.multi_line_comment_mark) == 0:
            return False
        begin_mark = self.multi_line_comment_mark[0]
        end_mark = self.multi_line_comment_mark[1]

        if self._language == 'Perl':
            if self.belong_multi_line_comment:
                if line.endswith(end_mark):
                    self.belong_multi_line_comment = False
                return True
            if re.search(end_mark, line) is not None:
                if self.belong_multi_line_comment:
                    self.belong_multi_line_comment = False
                return True
            if re.search(begin_mark, line) is not None:
                if not self.belong_multi_line_comment:
                    self.belong_multi_line_comment = True
                return True
            return False

        if self._language == 'Python':
            lrhs = line.split('=')
            if len(lrhs) > 1:
                rhs = lrhs[1].strip()
                if rhs.startswith(begin_mark):
                    if not rhs.endswith(end_mark):
                        self.is_docstring = True
                    return False
            else:
                if self.is_docstring:
                    if line.endswith(end_mark):
                        self.is_docstring = False
                    elif end_mark in line:
                        self.is_docstring = False
                        return False
                    return True
                elif line.startswith(begin_mark):
                    if not line.endswith(end_mark):
                        self.is_docstring = True
                    return True
                return self.is_docstring

        else:
            if self.belong_multi_line_comment:
                if line.endswith(end_mark):
                    self.belong_multi_line_comment = False
                elif end_mark in line:
                    self.belong_multi_line_comment = False
                    return False
                return True
            elif line.startswith(begin_mark):
                if not line.endswith(end_mark):
                    self.belong_multi_line_comment = True
                return True
            elif line.endswith(begin_mark):
                self.belong_multi_line_comment = True
            return False

    def count(self, file_path):
        self.belong_multi_line_comment = False
        self.is_docstring = False
        if self._language is None:
            raise ValueError('Unsupported language: {}'.format(self._language))

        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        count = 0
        for line in lines:
            if self.is_multi_line_comment(line):
                continue
            if self.is_single_line_comment(line):
                continue
            if self.is_blank_line(line):
                continue
            count += 1
        return count

'''
cfg_file = 'loc_measure/config.json'
loc_measure = LocMeasure(cfg_file)
loc_measure.language = 'Python'
print(loc_measure.count('test/code.py'))
'''
