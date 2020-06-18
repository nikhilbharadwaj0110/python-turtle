import random

myvars = {}
with open("quiz-bank.txt") as myfile:
    for line in myfile:
        name, var = line.partition("=")[::2]
        myvars[name.strip()] = var

question_list = list(myvars.keys())
randomQuestion = random.randint(0,len(question_list)-1)

question = question_list[randomQuestion]
print(question)

userAnswer = input("Enter your answer: ")

systemAnswer = myvars[question]
systemAnswer = systemAnswer.strip()
systemAnswer = systemAnswer.rstrip('\n')

if systemAnswer.lower() == userAnswer.lower():
    print("You are correct!")
else:
    print("That's incorrect!  Correct answer is : " + systemAnswer)
