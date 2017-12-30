# coding=utf-8

import unittest

from .context import utils


class TestDeogonkify(unittest.TestCase):
    def test_deogonkify(self):
        expected = {
            u'ala': u'ala',
            u'żołądź': u'zoladz',
            u'Zbigniew': u'Zbigniew',
            u'ęółśążźćń': u'eolsazzcn',
            u'eolsazzcn': u'eolsazzcn'
        }
        for case in expected:
            self.assertEqual(utils.deogonkify(case), expected[case])


if __name__ == '__main__':
    unittest.main()
