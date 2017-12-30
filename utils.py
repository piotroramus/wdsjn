# coding=utf-8

from plp import PLP

plp = PLP()


def basic_form(word):
    ids = plp.rec(word)
    if not ids:
        return word
    return plp.bform(ids[0])


def deogonkify(word):
    """The word must be lowercase."""
    substitutions = {
        u'ą': 'a',
        u'ć': 'c',
        u'ę': 'e',
        u'ł': 'l',
        u'ń': 'n',
        u'ó': 'o',
        u'ś': 's',
        u'ż': 'z',
        u'ź': 'z',
    }

    result = ""
    for i, char in enumerate(word):
        if char in substitutions:
            result += substitutions[char]
        else:
            result += char
    return result
