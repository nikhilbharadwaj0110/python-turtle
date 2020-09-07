import random
import time

# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()

# Welcome the user to the game and give them the instructions
# Generate 7 random letters using  a dictionary and set
# Give the user 7 letter to  let them make as may words as they can before they get an invalid words
# check if the letters used are valid from the list of letters
# If the word entered is a valid word and
# if the user has not used the word before and then add length of valid word  to the score

dictAlphabets = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l",
                 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w",
                 24: "x", 25: "y", 26: "z"}


def genRandLetters():
    randLtrsSet = set()
    while len(randLtrsSet) < 7:
        randnum = random.randint(1, 26)
        randLtrsSet.add(dictAlphabets[randnum])
    return randLtrsSet


wordList = []


def isValidWord(word):
    if word in validWords:
        return True
    else:
        return False


def isNewWord(wordList, word):
    if word in wordList:
        return False
    else:
        return True


def isValidLetters(word):
    for c in word:
        if c not in letters:
            return False
    return True


letters = genRandLetters()
# ["h","d","a","v","u","z","r"]
score = 0
input(
    "Welcome to Wordsmith! In this game, come up with as many words as you can using the 7 letters you are given. Press Enter to begin!")
print("Ready...")
time.sleep(1)
print("Set...")
time.sleep(1)
print("Go!")
print("Your random letters are:")
print(letters)

while True:
    inputWord = input("\nEnter a word: ")

    if isValidLetters(inputWord):
        if isNewWord(wordList, inputWord):
            wordList.append(inputWord)
            if isValidWord(inputWord):
                score += len(inputWord)
                print("Valid word! Your score: ", score)
            else:
                print("Invalid word!")
        else:
            print("You already entered this word. Your score: ", score)
    else:
        print("you can only use the 7 letters given to you.")



