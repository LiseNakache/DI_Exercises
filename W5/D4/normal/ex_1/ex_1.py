from random import randint


def get_words_file(filename):
    """
    gets a list of words from a txt file, each word has to be on a separate line in the file
    :param filename: txt file, each word has to be on a separate line in the file
    :return: returns list of words
    """
    with open(filename, 'r+') as f:
        return f.readlines()


def get_random_sentence(length):
    """
    gets a random sentence with length (arg: length) from a file containing words
    :param length:length of sentence
    :return: returns random sentence
    """

    words_list = get_words_file("sowpods.txt")
    random_sentence = ""
    try:
        for word in range(length):
            word_to_add = words_list[randint(0, len(words_list)-1)].lower()
            word_to_add = word_to_add.replace("\n", " ")
            random_sentence += word_to_add
    except ValueError:
        raise ValueError
    return random_sentence


def main():
    print(f"A program that will generate a random sentence and display it to the user. \
    We will allow the user to choose how long the sentence will be.")
    try:
        length = int(input("Please enter a number between 2 and 20\n"))
        if 2 <= length <= 20:
            print(get_random_sentence(length))
    except ValueError:
        raise ValueError

    
if __name__ == "__main__":
    main()
