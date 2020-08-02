#PYTHON PROGRAM TO SORT IN ALPHABETICAL ORDER
my_string = input("enter a string:")
#breakdown the string into a list of words
words = my_string.split()
#sort the list
words.sort()
#display the sorted words
for word in words:
    print(word)