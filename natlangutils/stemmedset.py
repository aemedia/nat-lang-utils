from nltk.stem import PorterStemmer

class StemmedSet(object):
    """
    A set-like object for strings allowing natural-language membership testing.
    >>> s = StemmedSet(['cameras', 'university', 'navigate'])
    >>> t = set(['camera', 'eggs', 'universe', 'navigable', 'spam'])
    >>> s & t
    set(['navigate', 'university', 'cameras'])
    """

    def __init__(self, words):
        self.stemmer = self._get_stemmer()
        self.members = dict((self.stemmer.stem_word(w), w) for w in set(words))

    def _get_stemmer(self):
        return PorterStemmer()

    def __contains__(self, val):
        """
        A word belongs to the set if its stem matches one already in the set.
        >>> s = StemmedSet(['university', 'navigate'])
        >>> 'navigable' in s
        True
        """
        stemmed_val = self.stemmer.stem_word(val)
        return stemmed_val in self.members

    def __and__(self, obj):
        """
        >>> s = StemmedSet(['university', 'navigate'])
        >>> text = set(['universe', 'spam', 'eggs'])
        >>> s & text
        set(['university'])
        """
        matching_stems = (set(self.members.keys()) &
                          set(self.stemmer.stem_word(w) for w in obj))
        return set(self.members[k] for k in matching_stems if k in self.members)

    def __rand__(self, obj):
        """
        >>> s = StemmedSet(['university', 'navigate'])
        >>> text = set(['universe', 'spam', 'eggs'])
        >>> text & s
        set(['universe'])
        """
        return set(StemmedSet(obj) & self)

    def __str__(self):
        """
        >>> s = StemmedSet(['university', 'navigate'])
        >>> print s
        StemmedSet(['university', 'navigate'])
        """
        return 'StemmedSet(%s)' % repr(self.members.values())

    def __repr__(self):
        """
        >>> s = StemmedSet(['university', 'navigate'])
        >>> s
        StemmedSet(['university', 'navigate'])
        """
        return str(self)

    def __iter__(self):
        """
        >>> s = StemmedSet(['university', 'navigate'])
        >>> [word for word in s]
        ['university', 'navigate']
        """
        for val in self.members.values():
            yield val

if __name__ == '__main__':
    import doctest
    doctest.testmod()
