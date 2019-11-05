import random
import sys

poem = """White against blue
Or is it blue against white
Seen surely in the day
And sometimes at night
A cloud
A bird in a cage
Struggling to be free
Laying in the sand
Staring past the sea
Me"""


poem_file = open("poem.txt", "r")

class colors:
    purple = '\033[35m'
    green = '\033[32m'
    yellow = '\033[93m'
    grey = '\033[37m'
    red='\033[31m'
    cyan='\033[46m'

funtion_choice = None

poem_words=[]

def lines_printed_forward(poem): #print lines forward  -  lf
    poem_lines = poem.split('\n')
    for lines in poem_lines:
        print(colors.grey,lines)

# def lines_printed_backward(poem):
#     for lines in poem:
#         print(colors.yellow, lines[::-1])

def words_printed_forward(poem):  #print words forward  -  wf
    poem_words = poem.split()
    for word in poem_words:
        print(colors.grey,word)

def words_printed_backward(poem):  # print words backward   -  wb
    poem_words = poem.split()
    for words in poem_words:
        print(colors.grey,words[::-1])

def lines_printed_backward(poem):   # print lines backward  -  lb
    poem_words = poem.split('\n')
    for words in poem_words:
        print (colors.grey,words[::-1])

def lines_printed_in_reverse(poem):     # print lines reverse  -  lrv
    poem_words = poem.split('\n')
    print(colors.grey, poem_words[::-1])

def lines_printed_randomly(poem):    # print lines randomly  -  lrd
    lines2=[]
    poem_lines = poem.split('\n') 
    for lines in poem_lines:
        lines2.append(lines)

    random.shuffle(lines2)
    amount_of_lines2 = len(lines2)

    for i in range(0, amount_of_lines2): 
        print (colors.grey, lines2[i], end=" ")

def choices(poem_type):
    while True:
        print(colors.red, "\nWhat functionality would you like to see?\n")
        function_choice = input("\nWords printed forward (wf),\nWords printed Backward (wb),\nLines printed Forward (lf),\nLines printed Forward (lb),\nLines printed Reverse (lrv),\nLines printed Backward (lrd),\nQuit (q)\n")
        function_choice.lower()
        print('\n\n')
        if function_choice == 'wf':
            print(words_printed_forward(poem_type))
        elif function_choice == 'wb':
            print(words_printed_backward(poem_type))
        elif function_choice == 'lf':
            print(colors.grey, poem_type)
        elif function_choice == 'lb':
            print(lines_printed_backward(poem_type))
        elif function_choice == 'lrv':
            print(lines_printed_in_reverse(poem_type))
        elif function_choice == 'lrd':
            print(lines_printed_randomly(poem_type))
        elif function_choice == 'quit':
            return False
        else:
            return True



# Test Functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print(colors.red, "\n" + poem)

# print(colors.green, "\nWords Printed Forward\n")
# print( words_printed_forward(poem))

# print(colors.green, "\nWords Printed Backward\n")
# print(words_printed_backward(poem))

# print(colors.green, "\nLines Printed In Reverse and Backward\n")
# print(lines_printed_backward(poem))

# print(colors.green, "\nLines Printed In Reverse\n")
# print(lines_printed_in_reverse(poem))

# print(colors.green, "\nLines Printed Randomly\n")
# print(lines_printed_randomly(poem))



# print(colors.green, "\nLines Printed Foward\n")
# print(lines_printed_forward(poem))

# print(colors.green, "\nLines Printed Backward\n")
# print(lines_printed_backward(poem))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

print(colors.purple, "\nWelcome to Backwards Poetry\n")
print("Before we continue, would you like to use the default poem, read from the file, or input your own?\n")
user_input = input("Choose default(d), file(f), or input(i): \n ")
user_input.lower()

if user_input == 'd':
    choices(poem)
    # print(poem)
elif user_input == 'f':
    choices(poem_file.read())
    # print(poem_file.read())
elif user_input == 'i':
    print("\n\nEnter your poem. Press enter to add new lines. Press Control+D (Ctrl+D) to end input: \n")
    user_poem = sys.stdin.readlines()
    choices(user_poem)
    # print(user_poem)
else:
    print("Invalid entry")





poem_file.close()
