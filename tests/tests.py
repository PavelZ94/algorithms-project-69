import unittest
from search_engine.search_engine import search


class TestSeacrhFunction(unittest.TestCase):

    def test_search_with_word_found(self):
        fixture = [
        {'id': 'doc_test1', 'text': 'Test text'},
        {'id': 'doc_test2', 'text': 'Notest text'},
        {'id': 'doc_test2', 'text': 'Test1 text'},
    ]

        test_word = 'test'
        result = search(fixture, test_word)
        self.assertEqual(result, ['doc_test1'])

    def test_search_without_word_found(self):
        fixture = [
            {'id': 'doc_test1', 'text': 'No words'},
            {'id': 'doc_test1', 'text': ''},
            {'id': 'doc_test3', 'text': 'ok'}
        ]

        test_word = 'test'
        result = search(fixture, test_word)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
