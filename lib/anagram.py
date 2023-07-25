# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        list_anagrams = []
        for anagram in anagrams:
            if sorted(anagram) == sorted(self.word):
                list_anagrams.append(anagram)
        return list_anagrams
