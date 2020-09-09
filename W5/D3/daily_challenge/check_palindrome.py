# Create a class that checks if a word is a palindrome(i.e. words that look the same written backwards).
# For example, if the word is “radar”, it should return True.

class Word():
    def __init__(self, word):
        self.word = str(word)

    def is_palindrome(self):
        reverse_word = self.word[::-1]
        palindrome = False
        if reverse_word == self.word:
            palindrome = True
        return palindrome


def main():
    radar = Word("radar")
    print(radar.is_palindrome())

if __name__ == "__main__":
    main()
