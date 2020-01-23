
number = int(input("Enter a number from 1 to 12 "))
noun = input("Enter a noun (plural): ")
name = input("Enter a name: ")
sentence = input("Enter any sentence: ").upper()
verb = input("Enter a verb ")


line1 = " It was %d o'clock when I heard a knock at the door.\n" % (number)
line2 = ' I opened the door and there was a box full of %s with a note saying "From Mr. %s." \n' % (noun, name.title())
line3 = 'Just as I closed the door I heard a scream "%s"\n' % (sentence)
line4 = " I froze in place and all I could do was %s." % (verb)

print("The stroy goes...")
print()
print(line1 + line2 + line3 + line4)

