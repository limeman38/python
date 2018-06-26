#!/usr/bin/python

import random
import time
import sys

responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

## Following function asks user question, then returns random results from responses
def answerQuery():
    question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")
    print("Let me dig deep into the waters of life, and find your answer")
    time.sleep(2)
    print("Hmmm.. thinking of the answer")
    time.sleep(2)
    print(random.choice(responses))
    print("\n")
answerQuery()

## Following asks user if they would like to play again, and loops until user is finished
secondQuestion =  raw_input("Would you like to ask the Wise One another question? y/n: ")
while secondQuestion == str("y"):
    answerQuery()
    secondQuestion = raw_input("Would you like to ask the Wise One another question? y/n: ")
else:
    sys.exit()
