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

poem_words=[]

def lines_printed_forward(poem):
    poem_lines = poem.split('\n')
    return poem_lines

def lines_printed_backwards():
    pass

def words_printed_forward(poem):
    poem_words = poem.split()
    return poem_words

def words_printed_backward(poem):
    poem_words = poem.split()
    poem_word_length = len(poem_words)
    poem_reverse_words =[]
    for word in range(poem_word_length-1, -1, -1):
        poem_reverse_words += poem_words[word]
    return poem_reverse_words

print(poem)
print("\nWords Printed Forward\n")
print(words_printed_forward(poem))
print("\nLines Printed Foward\n")
print(lines_printed_forward(poem))
print("\nWords Printed In Reverse\n")
print(words_printed_backward(poem))