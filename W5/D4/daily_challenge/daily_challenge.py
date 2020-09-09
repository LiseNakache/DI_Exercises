from gensim.parsing.preprocessing import remove_stopwords
import re
import string


class Text:
    def __init__(self, string=""):
        if string == "" or None:
            Text.from_txt_file('the_stranger.txt')
        else:
            self.string = string

    def get_word_freq(self, word):
        """
        gets the frequency of a word used in a text.
        #args: string
        #:return count of word in a string
        """
        try:
            count = self.string.count(word)
            if count == 0:
                count = None
            # else:
                # count = f"This word appears {count} times in the text"
            return count
        except ValueError:
            ValueError(f"This word is not in here {word}")

    def word_list(self):
        """:return strips dots and commas and special characters and returns list of words in string."""
        try:
            self.string = re.sub('[^A-Za-z0-9]+', ' ', self.string)
            word_list = self.string.split()
        except ValueError:
            raise ValueError("Oh OOHHH")
        return word_list

    def word_is_unique(self):
        """:return returns a list of unique words"""
        try:
            word_list = self.word_list()
            # check for unique words in word_list and add to unique_words list
            unique_words = []
            for word in word_list:
                if word not in unique_words:
                    unique_words.append(word)
        except ValueError:
            raise ValueError("does seem like there is something wrong with the value")
        return unique_words

    def get_most_common(self):
        """:return returns the word that appears the most in a string"""
        try:
            word_list = self.word_list()
            count_dict = {}
            count_dict.update({"most_common": ""})
            most_common_count = 0
            # for each word in the list, check if already exists,
            # if not add to count_dict, if yes increment value in count dict
            for word in word_list:
                if word.isalpha():
                    if word not in count_dict:
                        count_dict.update({word: 1})
                    else:
                        count_dict[word] += 1
                        if count_dict.get(word) > most_common_count:
                            count_dict.update({"most_common": word})
        except ValueError:
            raise ValueError
        most_common = count_dict.get("most_common")
        return most_common

    def create_txt(self, filename):
        """
        creates a text file from string in working directory
        :arg filename
        :return
        """
        try:
            with open(str(filename), "r") as f:
                f.read()
        except FileExistsError:
            FileExistsError("This file already exists, do you want to overwrite?")
            overwrite = input(str("Y/N\n"))
            if overwrite == "N":
                exit()
            else:
                with open(str(filename), "w+") as f:
                    f.write(self.string)
                print(f"The text was converted to a new txt file called {filename}")

    @classmethod
    def from_txt_file(cls, filename):
        try:
            with open(str(filename), "r") as f:
                f = f.read()
            cls.string = f
        except FileNotFoundError:
            raise FileNotFoundError


class TextModification(Text):
    def __init__(self, string=""):
        if string == "" or None:
            Text.from_txt_file('the_stranger.txt')
        else:
            self.string = string
        super().__init__(string)

    def remove_special_ch(self):
        """:return returns string of words in self.string without special characters."""
        try:
            self.string = re.sub('[^A-Za-z0-9]+', ' ', self.string)
        except ValueError:
            raise ValueError("Oh OOHHH")
        return self.string

    def remove_punctuation(self):
        """:return returns self.string stipped of punctuation"""
        self.string = self.string.strip(string.punctuation)
        return self.string

    def remove_stop_words(self):
        """ method that returns the text without english stop-words
        :returns string withour stop words"""
        self.string = remove_stopwords(self.string)
        return self.string

def main():
    # text1 = Text("Bla baksdba bald asdlk asd asba asd asd a sa asd")
    # print(f"frequency of 'text1' in text1 {text1.get_word_freq('Bla')}")
    # print(f"most common word: {text1.get_most_common()}")
    # print(f"Word is unique list {text1.word_is_unique()}")
    # Text.from_txt_file('the_stranger.txt')
    text2 = Text()
    # print(f"frequency of 'and' in textfile {text2.get_word_freq('and')}")
    print(f"most common word: {text2.get_most_common()}")
    # # print(f"Word is unique list {text2.word_is_unique()}")
    # text3 = TextModification()
    # # print(text3.remove_punctuation())
    # print(text3.remove_stop_words())

if __name__ == '__main__':
    main()
