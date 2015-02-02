#!/usr/bin/env python

print "You are at a baby shower that has just ended; faced with two choices.  Do you go with your fiancee to let your dogs out (choice #1) or do you go to pick up pizza for everyone (choice #2)?"

choice = raw_input("> ")

if choice == "1":
    print "Wise choice. But now who will go get the pizza? What do you do?"
    print "1. Ask your sister."
    print "2. Get the pizza after you let the dogs out."

    pizza = raw_input("> ")


    if pizza == "1":
        print "Your sister hasn't been drinking much so that's a great idea.  Good job!"
    elif pizza == "2":
        print "There is no way your fiancee would want to do that. her back hurts and her feet are swollen."
    else:
        print "Well, choosing %s and getting delivery is better, you are correct." % pizza

elif choice == "2":
    print "You drank too much beer and should not drive."
    print "1. Ask you sister to go."
    print "2. Get the pizza delivered."
    print "3. Understanding revolvers yelling melodies."

    delivery = raw_input("> ")


    if delivery == "1" or delivery == "2":
        print "Get the pizza delivered; that's the best choice."
    else:
        print "Tell Bob to go get his damn gourmet pizza himself.  Good job!"

else:
    print "Tell Bob to go get his damn gourmet pizza himself."
