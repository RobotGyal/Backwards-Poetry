import random

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
    for lines in poem_lines:
        print(colors.yellow,lines)

# def lines_printed_backward(poem):
#     for lines in poem:
#         print(colors.yellow, lines[::-1])

def words_printed_forward(poem):
    poem_words = poem.split()
    for word in poem_words:
        print(colors.yellow,word)
    return 
def words_printed_backward(poem):
    poem_words = poem.split()
    for words in poem_words:
        print(colors.yellow,words[::-1])

def lines_printed_backward(poem):
    poem_words = poem.split('\n')
    for words in poem_words:
        print (colors.yellow,words[::-1])

def lines_printed_in_reverse(poem):
    poem_words = poem.split('\n')
    print(colors.yellow, poem_words[::-1])

def lines_printed_randomly(poem):
    lines2=[]
    poem_lines = poem.split('\n') 
    for lines in poem_lines:
        lines2.append(lines)

    random.shuffle(lines2)
    amount_of_lines2 = len(lines2)

    for i in range(0, amount_of_lines2): 
        print (colors.yellow, lines2[i], end=" ")





print(colors.red, "\n" + poem)

print(colors.green, "\nWords Printed Forward\n")
print( words_printed_forward(poem))

# print(colors.green, "\nLines Printed Foward\n")
# print(lines_printed_forward(poem))

# print(colors.green, "\nLines Printed Backward\n")
# print(lines_printed_backward(poem))

print(colors.green, "\nWords Printed Backward\n")
print(words_printed_backward(poem))

print(colors.green, "\nLines Printed In Reverse and Backward\n")
print(lines_printed_backward(poem))

print(colors.green, "\nLines Printed In Reverse\n")
print(lines_printed_in_reverse(poem))

print(colors.green, "\nLines Printed Randomly\n")
print(lines_printed_randomly(poem))