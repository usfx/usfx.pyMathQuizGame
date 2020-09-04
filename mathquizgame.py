import time
import random
score = 0
print('Welcome to my Math Quiz!\n')

#This part for asking the user for name
print('What is your name?')
print('remember to press "Enter" after every answer.\n')

#input so i can put the user inside a text
name = input('Type your name here:')
print('Hey, ' + name + '!' + ' Good luck with the Quiz! and read the questions carfully ')

#questions and answers
questions = ["\nWhat's 200-98?","\nwhat's 235/5?","\nwhat's 545+65?","\nWhat is 10,000÷5? \nremeber to choose (a,b,c,d) as an answer. \n a. 5000 \n b. 2000 \n c. 2500 \n d. 1500","\nWhat's √81? \nremeber to choose (a,b,c,d) as an answer. \n a.9 \n b.6 \n c.8.9 \n d.9.05","\nWhat's √25? \nremeber to choose (a,b,c,d) as an answer. \n a.10 \n b.4 \n c.2 \n d.5"]

answers = ["102","47","610","b","a","d"]
number_of_questions = 5

#score points for each question
scores = [1,1,1,2,2,2]

comments = ['Correct you did great','great perfomance','good jop','nice jop','you are very good at that','you have got your brain in gear today','you make it look easy.','you must have been practicing','good thinking']
comments2 = ['Try harder next time','seems like someone was not practicing','incorrect','wasnt expecting that','very intersting']

#the loop i am using for questions
for q in range(number_of_questions+1):
  time.sleep(2)
  print(questions[q])
  answer = input("\nType your answer here:")
  if answer == answers[q]:
    
    #printing random comments by help of ibrahim he told me about import random he got it from intrnet
    print(random.choice(comments))
    
    score = score + scores[q]
    print("▶ Your current score is " + str(score))
  else:
    
    print(random.choice(comments2))
print('')
print(name + ',' + ' your final score is', score, 'out of 9.')
