from collections import Counter

class AnagramChecker():
    def __init__(self):
        with open('C:\\Users\\navag\\Desktop\\developersinstitute\\weekfive\\dayfive\\miniproject2\\sowpods.txt') as my_file:
           self.words_file = my_file.read() 

    def is_valid_word(self, word):
        return True if word in self.words_file.lower() else False
    
    def get_anagrams(self, word):
        anagrams = []
        letter_count = Counter(word)
        for file_word in self.words_file.split('\n'):
            if Counter(file_word.lower()) == letter_count and file_word.lower() != word:
                anagrams.append(file_word.lower())
        return anagrams        

ag = AnagramChecker()
ag.get_anagrams('princess')