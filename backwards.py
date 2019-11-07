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

# Reads from file
poem_file = open("poem.txt", "r")

#Colors for use later
class colors:
    purple = '\033[35m'
    grey = '\033[37m'
    red='\033[31m'

# Global Vairables
funtion_choice = None
poem_words=[]

# Functions
def lines_printed_forward(poem): #print lines forward  -  lf
    """ 
    Takes in a poem and prints it our line by line. 
    Parameters: 
    poem (string): Multiline string 
    Prints: 
    string: Each line in the input 
    """
    poem_lines = poem.split('\n')
    for lines in poem_lines:
        print(colors.grey,lines)

def words_printed_forward(poem):    #print words forward  -  wf
    """ 
    Takes in a poem and prints it out word by word. 
    Parameters: 
    poem (string): Multiline string 
    Prints: 
    string: Each word in the input 
    """  
    poem_words = poem.split()
    for word in poem_words:
        print(colors.grey,word)

def words_printed_backward(poem):  # print words backward   -  wb
    """ 
    Takes in a poem and prints it out backward word for word. 
    Parameters: 
    poem (string): Multiline string 
    Prints: 
    string: Each word in the input backwards
    """
    poem_words = poem.split()
    for words in poem_words:
        print(colors.grey,words[::-1])

def lines_printed_backward(poem):   # print lines backward  -  lb
    """ 
    Takes in a poem and prints it out backward line by line. 
    Parameters: 
    poem (string): Multiline string 
    Prints: 
    string: Each line in the input backwards
    """
    poem_words = poem.split('\n')
    for words in poem_words:
        print (colors.grey,words[::-1])

def lines_printed_in_reverse(poem):     # print lines reverse  -  lrv
    """ 
    Takes in a poem and prints it out line by line in reverse. 
    Parameters: 
    poem (string): Multiline string 
    Prints: 
    string: Each line in the input in reverse
    """
    poem_words = poem.split('\n')
    print(colors.grey, poem_words[::-1])

def lines_printed_randomly(poem):    # print lines randomly  -  lrd
    """ 
    Takes in a poem and prints it out lime by line randomly. 
    Parameters: 
    poem (string): Multiline string 
    Prints: 
    string: Each line in the input randomly
    """
    random_lines=[]
    poem_lines = poem.split('\n') 
    for lines in poem_lines:
        random_lines.append(lines)

    random.shuffle(random_lines)
    amount_of_random_lines = len(random_lines)

    for i in range(0, amount_of_random_lines): 
        print (colors.grey, random_lines[i], end=" ")

def lines_fenced(poem, wrapper='*~*'):    # Custom Function (Fences each line with special characters) - c 
    """ 
    Takes in a poem and prints it out line by line and 
    fences each line with special characters
    Parameters: 
    poem (string): Multiline string 
    Prints: 
    string: Each line in the input fenced in by special characters
    """
    poem_lines = poem.split('\n') 
    for lines in poem_lines:
        print(colors.grey, wrapper, lines, wrapper)

def choices(poem_type):         # Choices for when deciding what type of poem input
    """ 
    Looks at user choice to see what funtionality is to be ran
    to be used
    Parameters: 
    poem_type (string): A collection of bytes from user inout
    Return: 
    Will continue to run loop and ask user for inputs to test different 
    functionality until the user indicates to quit
    """
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



# Main Code
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(colors.purple, "\nWelcome to Backwards Poetry\n")
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
    elif user_input == 'i':
        print("\n\nEnter your poem. Press enter to add new lines. Press Control+D (Ctrl+D) to end input: \n")
        user_poem = sys.stdin.read()
        choices(user_poem)
    elif user_input == 'q':
        running =  False
    else:
        print("Invalid entry")
        continue
poem_file.close()
