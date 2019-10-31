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

class colors:
    purple = '\033[35m'
    green = '\033[32m'
    yellow = '\033[93m'
    grey = '\033[37m'
    red='\033[31m'
    cyan='\033[46m'

poem_words=[]

def lines_printed_forward(poem):
    poem_lines = poem.split('\n')
    return poem_lines

def lines_printed_backward(poem):
    return poem[::-1]

def words_printed_forward(poem):
    poem_words = poem.split()
    return poem_words

def words_printed_backward(poem):
    pass


print("\n" + poem)
print(colors.green, "\nWords Printed Forward\n")
print(colors.yellow, words_printed_forward(poem))
print(colors.green, "\nLines Printed Foward\n")
print(colors.yellow, lines_printed_forward(poem))
print(colors.green, "\nWords Printed In Reverse\n")
print(colors.yellow, lines_printed_backward(poem))