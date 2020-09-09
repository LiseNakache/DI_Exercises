
def get_line(file_name, linenumber):
    with open(file_name, 'r') as f:
        for i in range(linenumber):
            line = f.readline()
    return line

def create_file(file_name):
    with open(file_name, 'w+') as f:
        print(f'{file_name} created')
# f = open('secrets.txt', 'w+', 'r')
# with open('secrets.txt', 'r+') as f:
#     f.seek(50)
#     text = f.readline()
# for i in text:
#     print(i)

# with open('secrets.txt', 'a+') as f:
#     f.write(text)


# print(get_line('/Users/royaltstadter/Desktop/DI_Exercises/W5/D4/normal/secrets.txt', 2))
create_file('/Users/royaltstadter/Desktop/DI_Exercises/W5/D4/normal/secrets.txt')
