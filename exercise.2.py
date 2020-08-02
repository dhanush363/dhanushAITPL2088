#PYTHON PROGRAM TO SORT IN ALPHABETICAL ORDER
my_string = input("enter a string:")
words = my_string.split()
#sort the list
words.sort()
#display the sorted words
for word in words:
    print(word)