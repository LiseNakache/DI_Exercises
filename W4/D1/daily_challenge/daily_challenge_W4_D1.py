#get user input and save it
user_input_string = str(input("type a word with 10 characters\n"))

#check for user_input length
if len(user_input_string) == 10:
    print("this is the first letter: ",user_input_string[0])
    print("this is the last letter: ", user_input_string[len(user_input_string)-1])
    for letter in user_input_string:
        print(letter)
    print(user_input_string)
else: 
    print("Try again, but this time with a 10 lettered word!")
    errorCode = -1
    print(f"Error: {errorCode}")
