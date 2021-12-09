from datetime import datetime
from random import shuffle

def optionlist_shuffle(option_list):
    if "all of above" in option_list:
        shuffle(option_list[:2])
    elif "none of above" in option_list:
        shuffle(option_list[:2])
    else:
        shuffle(option_list)

print("     WELCOME TO QUIZ    ")

name = input(" your name= ")
user_time = datetime.now()

greeting = "Good morning"

#get user time
if user_time.hour >= 12 and user_time.hour <16:
    greeting = "Good Afternoon "
elif user_time.hour >= 16 and user_time.hour < 20:
    greeting ="Good evening "
elif user_time.hour >=20 and user_time.hour < 12 :
    greeting = "Good Night "

print(f"{greeting} {name.capitalize()}")

print("Here are the question")
Question = [
    {
        "question" : "Which is the international sports competitions that is held only in Nepal?",
        "options" : ["football","volleyball","elephant polo","cricket"],
        "correct_ans" : "elephant polo"
    },
    {
        "question" : "What is the height of MT Everest? ",
        "options" : ["8848", "7800", "8142", "9976"],
        "correct_ans" : "8848"
    },
    {
        "question" : "For which of the following disciplines is Nobel Prize awarded? ",
        "options" :  [
            "physics and chemistry", "physiology or medicine",
            "literature, peace and economics", "all of above"
            ],
        "correct_ans" : "all of above"
    },
    {
        "question" :"World population day celebrates on.....",
        "options" : ["dec 11", "july 11", "march 15", "october 20"],
        "correct_ans" : "dec 11"
    },
    {
        "question" : "According to the 2058 census, which caste of Nepal is in least minority?",
        "options" : ["kusunda", "chepang", "Raute", "none of above"],
        "correct_ans" : "kusunda"
    },
    {
        "question" : "When was the Sagarmatha National Park included in the World Heritage Sites?",
        "options" : ["1959", "1979", "1970",  "1565"],
        "correct_ans" : "1979"
    },
    {
        "question" : "Grand Central Terminal, Park Avenue, New York is the world’s?",
        "options" : [
            "largest railway station", "highest railway station",
            "longest railway station", "none of above"
            ],
        "correct_ans" : "largest railway station"
    },
    {
        "question" : "Which of the following national parks is not listed in a UNESCO World Heritage site? ",
        "options" : ["kaziranga", "keoladeo", "sundarbans", "kanha"],
        "correct_ans" : "kanha"
    },
    {
        "question" : "When did the World Trade Organization come into existence?",
        "options" : ["1992", "1993", "1994", "1995"],
        "correct_ans" : "1995"
    },
    {
        "question" : "When was the war of american independence?",
        "options" : ["1770", "1772", "1774", "1776"],
        "correct_ans" : "1776"
    }
    ]

shuffle(Question)

#To shuffle options
option_list = []
for option_shuffle in range(10):
    option_list = Question[option_shuffle].get('options')
    optionlist_shuffle(option_list)
    # shuffle(option_list[:2])
    Question[option_shuffle]['options'] = option_list
    

print("Lets start the quiz")
print("Select your answer from options using 1, 2, 3, 4")

question_count = len(Question)
i = 0
point = 0

# print questionw
while(0 <= i < question_count):
    print(Question[i]['question'])
    
    # print options
    j = 0 
    for j in range(len(Question[i]['options'])):
        print(f"{j+1} : {Question[i]['options'][j]}")

    # Get answer from user in terms of 1 or 2 or 3 or 4
    user_ans = int(input("your answer =  "))

    # check ans
    if 1 <= user_ans <=4:
        for_ans = []
        for ans in Question[i]['options']:
            for_ans.append(ans)
        if user_ans == 1:
            answer = for_ans[user_ans-1]
        elif user_ans == 2:
            answer = for_ans[user_ans-1]
        elif user_ans == 3:
            answer = for_ans[user_ans-1]
        else:
            answer = for_ans[user_ans-1]
        if answer == Question[i]['correct_ans']:
            point += 1
            print("correct")
        else:
            print("wrong")
    else:
        print("choose from the given option")
        continue
    i = i + 1

print(f"Your total score is {point}")
if point >= 8:
    print(f"Congratulation!!.You won the first prize by scoring {point} point")
elif 5 <= point < 8:
    print(f"Congratulation!!.You won the second prize by scoring {point} point")
else:
    print(f"Your score is too low. You have score only {point} point.Better luck next time")

print("This much for today")
print("Thank you")
 
