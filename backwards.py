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
    grey = '\033[37m'
    red='\033[31m'

funtion_choice = None

poem_words=[]

def lines_printed_forward(poem): #print lines forward  -  lf
    poem_lines = poem.split('\n')
    for lines in poem_lines:
        print(colors.grey,lines)

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
    random_lines=[]
    poem_lines = poem.split('\n') 
    for lines in poem_lines:
        random_lines.append(lines)

    random.shuffle(random_lines)
    amount_of_random_lines = len(random_lines)

    for i in range(0, amount_of_random_lines): 
        print (colors.grey, random_lines[i], end=" ")

# Custom Function
def lines_fenced(poem, wrapper='*~*'):
    poem_lines = poem.split('\n') 
    for lines in poem_lines:
        print(colors.grey, wrapper, lines, wrapper)

def choices(poem_type):
    while True:
        print(colors.red, "\n\nWhat functionality would you like to see?\n")
        function_choice = input("\nWords printed forward (wf),\nWords printed Backward (wb),\nLines printed Forward (lf),\nLines printed Forward (lb),\nLines printed Reverse (lrv),\nLines printed Backward (lrd),\nLines Fenced/Custom (c), \nAnother Poem Input Type (ap),\nQuit (q)\n")
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
        elif function_choice == 'c':
            print(lines_fenced(poem_type))
        elif function_choice == 'ap':
            return False
        elif function_choice == 'q':
            return False
        else:
            print("Invalid response. Try again\n")
            continue



# Testing 
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


# print(colors.grey, "\nLines Fenced\n")
# print(lines_fenced(poem))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# Main Code
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print(colors.purple, "\nWelcome to Backwards Poetry\n")
print("Before we continue, would you like to use the default poem, read from the file, or input your own?\n")
running = True
while running:
    user_input = input("Choose default(d), file(f), input(i), or quit(q): \n ")
    user_input.lower()

    if user_input == 'd':
        choices(poem)
        # print(poem)
    elif user_input == 'f':
        choices(poem_file.read())
        # print(poem_file.read())
    elif user_input == 'i':
        print("\n\nEnter your poem. Press enter to add new lines. Press Control+D (Ctrl+D) to end input: \n")
        user_poem = sys.stdin.read()
        # user_poem = input()
        choices(user_poem)
        # print(user_poem)
    elif user_input == 'q':
        running =  False
    else:
        print("Invalid entry")
        continue





poem_file.close()
