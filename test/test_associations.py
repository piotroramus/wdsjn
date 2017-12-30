# coding=utf-8

import unittest

from .context import associations


class TestAssociations(unittest.TestCase):
    def test_adjacent_words(self):
        document = "a b c d".split(' ')

        adjacent = associations.adjacent_words(document, index=1, window_size=2)
        expected = "a c d".split(' ')
        self.assertEqual(adjacent, expected)

        adjacent = associations.adjacent_words(document, index=0, window_size=2)
        expected = "b c".split(' ')
        self.assertEqual(adjacent, expected)

        adjacent = associations.adjacent_words(document, index=3, window_size=2)
        expected = "b c".split(' ')
        self.assertEqual(adjacent, expected)

        adjacent = associations.adjacent_words(document, index=0, window_size=12)
        expected = "b c d".split(' ')
        self.assertEqual(adjacent, expected)

        adjacent = associations.adjacent_words(document, index=3, window_size=12)
        expected = "a b c".split(' ')
        self.assertEqual(adjacent, expected)

        adjacent = associations.adjacent_words(document, index=1, window_size=0)
        self.assertEqual(adjacent, [])

        document = "a b c d e f g".split(' ')

        adjacent = associations.adjacent_words(document, index=3, window_size=2)
        expected = "b c e f".split(' ')
        self.assertEqual(adjacent, expected)

        adjacent = associations.adjacent_words(document, index=1, window_size=2)
        expected = "a c d".split(' ')
        self.assertEqual(adjacent, expected)

        document = "a b c d e f g h i j k l m n o p e r s t u w x y z".split(' ')
        adjacent = associations.adjacent_words(document, index=13, window_size=12)
        expected = "b c d e f g h i j k l m o p e r s t u w x y z".split(' ')
        self.assertEqual(adjacent, expected)

        document = "word0 word1 word2 word3 word4".split(' ')
        adjacent = associations.adjacent_words(document, index=1, window_size=2)
        expected = "word0 word2 word3".split(' ')
        self.assertEqual(adjacent, expected)


if __name__ == '__main__':
    unittest.main()
