# This is my madlibs game, made on April 28, 2016
import time

# Get some user input first
adjective1 = raw_input("Enter an adjective ")
noun1 = raw_input("Enter a noun ")

name1 = raw_input("Enter a name ")
name2 = raw_input("Enter a name ")
plural_noun1 = raw_input("Enter a plural noun ")
plural_noun2 = raw_input("Enter a plural noun ")
adjective2 = raw_input("Enter an adjective ")
noun2 = raw_input("Enter a noun ")

adverb1 = raw_input("Enter an adverb ")

adjective3 = raw_input("Enter an adjective ")
noun3 = raw_input("Enter a noun ")

plural_noun3 = raw_input("Enter a plural noun ")
plural_noun4 = raw_input("Enter a plural noun ")

clothing = raw_input("Enter a clothing item ")
noun4 = raw_input("Enter a noun ")

adverb2 = raw_input("Enter an adverb ")

# Build up the suspense
print "Welcome to MadLibs!"
time.sleep(5)
print "Here are your results!"
time.sleep(2)

# Humorous results if we are lucky!
print "Good News! Today we are going to the beach!"
print "It is a(n) %s day for it too, as there is plenty of %s in the sky." % (adjective1, noun1)  
print "%s and %s are bringing %s and %s so that everyone can build a %s %s." % (name1, name2, plural_noun1, plural_noun2, adjective2, noun2) 
print "We will time it, whoever is the %s will win!" % (adverb1) 
print "After the competition, we have reserved a(n) %s %s for lunch." % (adjective3, noun3)
print "For your dining pleasure, we will be serving %s and %s," % (plural_noun3, plural_noun4)
print "which are always delicious at the beach."
print "Be sure to bring your %s and %s, as there will be plent of time to swim in the ocean." % (clothing, noun4)
print "It is sure to be a(n) %s day!" % (adverb2) 