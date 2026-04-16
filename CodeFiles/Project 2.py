"""
Created on Wed Apr  8 15:14:53 2026

@author: Christian Quintana, 034789311
"""

import random # for randomizing the quiz, never get the same quiz twice! Unless you are REALLY unlucky. Or REALLY lucky, depends on your perspective.
import time # a library for delaying the program so the text doesn't fly past you at breakneck speeds

QuizQuestions = [] # this is where the information for the quiz questions are stored after 
Rules = ["Answer the questions to the best of your ability.","This quiz contains no negative numbers.","Calculators are not allowed.","For division, remainder will be included as a whole number."]
Index = ["X","+","-","*","/"] # the operation is stored as a number, and 1 0 1 is not the same as 1 + 1.

print("Welcome to the mathematics examination. \n\n")

time.sleep(0.5)

grade = 0  # What is the targeted grade level of this quiz.
quizsize = 0 # How many questions are there?
score = 0 # How many questions scored correct
outof = 0 # Max number of questions

A = True # For try/except sweeps.

def GenerateQuestion(Conditions): # This function generates a question within given parameters
    Lim = 1 
    
    # Getting what operations are allowed, usually if a higher operation is allowed, the ones before it are also allowed.
    if Conditions[3] == True:
        Lim = 4
    elif Conditions[2] == True:
        Lim = 3
    elif Conditions[1] == True:
        Lim = 2
    elif Conditions[0] == True:
        Lim = 1
    
    Operand1 = 0 
    Operand2 = 0
    Operator = random.randint(1, Lim) # Chose a random operation for the question
    RemainderNecessary = False # If it is a division problem we need a remainder!
    Remainder = 0
    Answer = 0
    
    if Operator == 4: # If it is a division problem we need a remainder!
        RemainderNecessary = True

    if Operator <= 2: 
        Operand1 = random.randint(0, 10**Conditions[4])
        Operand2 = random.randint(0, 10**Conditions[4])
        while Operand2 > Operand1:
            Operand2 = random.randint(0, 10**Conditions[4]) # No negative numbers allowed
    else:
        Operand1 = random.randint(0, 10**Conditions[5])
        Operand2 = random.randint(1, 10**Conditions[5]) # No division by 0 allowed
        
        # Getting the answers here
    if Operator == 1: # 1 = Addition
        Answer = Operand1 + Operand2
    elif Operator == 2: # 2 = Subtraction
        Answer = Operand1 - Operand2
    elif Operator == 3: # 3 = Multiplication
        Answer = Operand1 * Operand2
    elif Operator == 4: # 4 = Division
        quotient, remainder = divmod(Operand1, Operand2)
        Answer = quotient
        Remainder = remainder

    return [Operand1,Operand2,Operator,Answer,RemainderNecessary,Remainder] # This is the complete answer
    
    
    
    
def GenerateQuiz(gradelevel,size): # This function generates the quiz as a whole
    Addition = True
    Subtraction = False
    Multiplication = False
    Division = False
    
    global outof # Bring in the function tallying up the max score

    ArithmeticDigits = 0 # Number of digits allowed for arithmetic 
    MultiplicationDigits = 0 # Number of digits allowed for multiplication
    NumOfQuestions = 0
    
    # Setting the parameters based on the grade level chosen
    if gradelevel == 1:
        #print("Grade level 1 selected.")<- for debugging
        ArithmeticDigits = 1
    elif gradelevel == 2:
       # print("Grade level 2 selected.")<- for debugging
        ArithmeticDigits = 1
        Subtraction = True 
    elif gradelevel == 3:
       # print("Grade level 3 selected.")<- for debugging
        Multiplication = True
        ArithmeticDigits = 1
        MultiplicationDigits = 1
    elif gradelevel == 4:
        Multiplication = True
        ArithmeticDigits = 2
        MultiplicationDigits = 2
       # print("Grade level 4 selected.")<- for debugging
    elif gradelevel == 5:
        Multiplication = True
        Division = True
        ArithmeticDigits = 3
        MultiplicationDigits = 2
      #  print("Grade level 5 selected.")<- for debugging

    # Setting the length of the quiz based upon the length we input
    if size == 1: 
        NumOfQuestions = 4
        outof = 4
    elif size == 2:
        NumOfQuestions = 10
        outof = 10
    elif size == 3:
        NumOfQuestions = 25
        outof = 25
        
    print("Quiz is going to be ",NumOfQuestions," questions long.")
    print("Generating questions...")
    
    Conditions = [Addition,Subtraction,Multiplication,Division,ArithmeticDigits,MultiplicationDigits] # The parameters we'll use to generate questions
    
    for i in range(NumOfQuestions):
        QuizQuestions.insert(len(QuizQuestions)-1,GenerateQuestion(Conditions)) # Generating the questions and storing them in an array
        
    # print(QuizQuestions) <- for debugging
    time.sleep(0.5)
    print("GENERATING QUIZ.")
    time.sleep(0.75)
    print("GENERATING QUIZ..")
    time.sleep(1)
    print("GENERATING QUIZ...")
    time.sleep(1.25)
    print("QUIZ GENERATED!")
    time.sleep(0.5)

def IntOnlyInput(Message,Bounds,UpperLimit,LowerLimit): # This is our error check, it is general purpose and accepts only integers, you can customize it how you like as well!!!
    A = True
    while A == True:    
        try:
            response = int(input(Message))
            if Bounds == True:
              if response <= UpperLimit and response > LowerLimit:
                  A = False
                  return response 
              else:
                  print("INVALID NUMBER!")
            else:
                return response
        except ValueError:
            print("\n\n FORBIDDEN INPUT DETECTED! \n\n")
            pass


grade = IntOnlyInput("Enter the grade level you want your examination to be on par with (1-5)",True,5,0)

print("\nPerfect!\nYou will be given a quiz that is equivalent to grade",grade,"of elementary school.") # With a 4 function quiz you really can't get higher than elementary school!

quizsize = IntOnlyInput("Please enter the size of examination you want.\n1 == Pop Quiz, 2 == Test, 3 == Comprehensive Final Exam (1-3)",True,3,0)


print("Perfect! Generating quiz now. \n\n")
    
GenerateQuiz(grade,quizsize) # Call our handy function to generate the quiz 

print("\n\nBefore we begin, here are some rules.\n\n")
for i in range(len(Rules)): # Letting you know the rules of the quiz...
    print("\n\n",Rules[i-1],"\n\n")
    time.sleep(0.75)

print("Ready? \n\n")
time.sleep(0.75)
print("Starting quiz now! Good luck! \n\n")
time.sleep(0.75)

for i in range(len(QuizQuestions)): # This is the part where the quiz is executed.
    Question = QuizQuestions[i]
    
    if Question[4] == True: # Division is actually an unfair 2 part question worth only one point. Sorry
        print("Question number ",i + 1,"! What is ",Question[0]," ",Index[Question[2]]," ",Question[1],"?\n")
        Response = IntOnlyInput("Type your answer:",False,0,0)
        
        print("What is the remainder?")
        Remainder = IntOnlyInput("Type the remainder:",False,0,0)

        if Remainder == Question[5] and Response == Question[3]:
            # Correct
            score += 1
    else: 
        print("Question number ",i + 1,"! \nWhat is ",Question[0]," ",Index[Question[2]]," ",Question[1],"?\n")
        Response = IntOnlyInput("Type your answer:",False,0,0)
       # print(Response) <- for debugging
       # print(type(Response)) <- for debugging
        if Response == Question[3]:
            score += 1

print("Your examination has concluded, we are tallying up your score now.\n")

print("You got...")
for i in range(score + 1): # Dramatically reads your score one by one. 
    print(i,"/",outof)
    time.sleep(0.25)
print(score," out of ",outof,"! Wow! That's ",float(score/outof)*100,"%") # The WOW part is either degrading, sympathetic, or praising based upon your score.

# _._     _,-'""`-._
#(,-.`._,'(       |\`-/|
#    `-.-' \ )-`( , o o)   <---  ASCII art I found on the internet
#          `-    \`_`"'-
