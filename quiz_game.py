""" version one
print(" Welcome to my quiz! ")

playing = input("Do you want to play ")

if playing.lower() != "yes": 
    quit()
    
print("let's play :) ")
score = 0

answer = input("what does  CPU stand for? ")
if answer  == "central processing unit":
    print('Correct!')
    score = score +1
    print(score)

else :
    print('Incorrect!')
    
    
answer = input("what does  GPU stand for? ")
if answer.lower()  == "graphics processing unit":
    print('Great Job !')
    score =+1
    print(score)

else :
    print('Keep trying !')
    
    

answer = input("what does a PSU stand for? ")
if answer  == "power supply unit":
    print('proud of you !')
    score =+1
    print(score)

else :
    print('Dont give up!')



answer = input("What is the most popular programming language for web development? : \n Javascript \n python \n Go \n C++ \n")
if answer  == "Javascript":
    print('wow keep going!')
    score = +2
    print(score)

else :
    print('hang in there!')


answer = input("Which of the following is a version control system?: \n Docker \n Github \n Linux \n")
if answer  == "Github":
    print('just one more !')
    score =+1
    print(score)

else :
    print('try again :)')


answer = input("what does RAM stand for? ")
if answer  == "random access memory":
    print('you made it!')
    score =+ 1
    print(score)
else :
    print('try again!')

print('your score is '+ str(score) + ' points') """


"""updated version """
import random
score  = 0 
questions = [
    ("What does CPU stand for?", "central processing unit"),
    ("What does GPU stand for?", "graphics processing unit"),
    ("What does PSU stand for?", "power supply unit"),
    ("What is the most popular programming language for web development?  choose a number \n1) JavaScript \n2) Python \n3) Go \n4) C++", "1"),
    ("Which of the following is a version control system? \n1) Docker \n2) GitHub \n3) Linux", "2"),
    ("What does RAM stand for?", "random access memory")
]


playing   =  input('Do you want to play ? ')
if playing != "yes" : 
    quit()
else :
    random.shuffle(questions)
    for question , correct_asnwer in questions:
        answer = input(question + '\n').lower()
        if answer == correct_asnwer :
            print('Correct')
            score= score+1
            print(score)
        else: 
            print('Incorrect')
    print("your score is " +str(score)  + " points! ")
    
    


    
    


