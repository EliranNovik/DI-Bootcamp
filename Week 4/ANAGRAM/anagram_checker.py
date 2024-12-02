class AnagramChecker:
    def __init__(self):
        with open("/Users/elirannovik/Desktop/DI-Bootcamp/Week 4/RockPaperExercice/sowpods.txt", "r") as file:
            self.words = [word.strip().lower() for word in file]

    def is_valid_word(self, word):
        return word.lower() in self.words

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and word1.lower() != word2.lower()

    def get_anagrams(self, word):
        return [w for w in self.words if self.is_anagram(word, w)]
