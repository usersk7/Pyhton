mstr = input("enter string: ")
words = mstr.split()
words.sort()
print("The Sorted Words are")
for word in words:
    print(word)