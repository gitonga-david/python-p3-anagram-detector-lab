# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
       return [anagram for anagram in anagrams if sorted(anagram) == sorted(self.word)]
    
