import anagram_checker, string
           
def show_menu():
    while True:
        user_choice = input('''Welcome to the anagram checker! Would you like to:
        (w) input a word
        (x) exit the program
        ''')
        if user_choice == 'w' or user_choice == 'x':
            return user_choice
            
def get_word_choice():
    while True:
        word_choice = input('Which word would you like to check?').strip()
        if validate_user_input(word_choice):
            return word_choice

def validate_user_input(word):
    if len(word.split(' ')) != 1:
        print('Only one word allowed.')
        return False
    if word.isalpha() == False:
        print('No special chars allowed') 
        return False
    return True

def run_anagram_checker():
    choice = show_menu()
    if choice == 'x':
        print('Goodbye!')
    else:
        while True:
            word = get_word_choice()
            my_anagram_checker = anagram_checker.AnagramChecker()
            if my_anagram_checker.is_valid_word(word):
                anagram_list = my_anagram_checker.get_anagrams(word)
                print(f'Your word is: {word} \nAnagrams of your word include {", ".join(anagram_list)}')
                break
            else :
                print('Please choose an English word')

run_anagram_checker()
    