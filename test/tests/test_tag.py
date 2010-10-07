import os
import random
import unittest
import traceback

from html2markdown import Html2MarkdownParser

data_dir = 'data'

def get_input_buf():
    s = traceback.extract_stack()[-2][2]
    return open(data_dir + '/' + s.split('_')[1] + '.html').read()

def get_output_buf():
    s = traceback.extract_stack()[-2][2]
    return open(data_dir + '/' + s.split('_')[1] + '.markdown').read()

class TestTag(unittest.TestCase):
    def setUp(self):
        self._parser = Html2MarkdownParser()

    def tearDown(self):
        self._parser.close()

    def test_a(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_b(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_blockquote(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_em(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_h1(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_h2(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_h3(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_h4(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_h5(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_h6(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_hr(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_ol(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_p(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())
        
    def test_pre(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_strong(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())

    def test_ul(self):
        self._parser.feed(get_input_buf())
        self.assertEqual(self._parser.get_markdown(), get_output_buf())
