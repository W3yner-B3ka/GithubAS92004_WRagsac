#Version 4.0
# This program will be about a chess quiz that ranges from difficulty--easy, medium, or hard.
#Github commit: Start the backbone of the structure and work on the welcomeText and defiining the constants and dictionaries
#Done the display insturctions and ready quiz. They run as usual
#Fixed the readyQuiz function and fixed some code on the runquiz function. Started on the displayscore functionn
#TODO Fix errors within the instructions text and some on the run quiz

#modules
import time
import os
import string

#Constants
MIN_AGE = 11
MAX_AGE = 18

RANKS = ["beginner", "intermediate", "advanced"]

#Begginner thresholds
BEGINER_THRESHOLD = 4
INTERMEDIATE_THRESHOLD = 8
ADVANCED_THRESHOLD = 12


#Dictionaries

#user attributes define various things the user has
user_attributes = {
    "isCompletedQuiz": False,
    "correctAnswers": [], #correct answers will be empty for now
    "wrongAnswers": [], #wrong answers will be empty for you.
    "userName": "", #The userName will initially be an empty string
    "rank": RANKS, #Ranks defined as beginner, intermediate, advanced
    "userScore": 0 #Score is initially set as zero
}

#Questions of the quiz
quiz_questions = {
    1 : "How do you win in chess: A By Check, B: Capturing all pieces: C: Checkmate: D: Capturing the Queen",
    2 :	"True or False: The knight can jump over pieces.",
    3 : "What directions can the queen go in? A: Up, B: Down, C: side to side, D: Diagonal, E: all of the above",
    4 :	"What is a check?",
    5 :	"Can you block a check with another piece?",
    6 :	"Which side goes first, white or black?",
    7 :	"What pieces can the pawn change if it reaches the end of the rank: A: Queen, B: Bishop: C: Knight, D: Rook, E: All of the above",
    8 :	"True or false: The king can move more than one space.",
    9 :	"Can the pawn move up two spaces after it’s moved from its starting position?",
    10:	"True or False: You can capture a pawn if the pawn has moved two squares from its starting position.",
    11:	"What is a stalemate: A: Checking the king B: The king has no legal moves while not in check C: The king has nowhere to move but in check D: Just a random term.",
    12:	"Can the king castle after it was checked?"

}

#key words or answers of the quiz:
quiz_answers = {
    1: "c",
    2: "true",
    3: "e",
    4: "a",
    5: "yes",
    6: "white",
    7: "e",
    8: "false",
    9: "no",
    10: "true",
    11: "b",
    12: "no"
}


# This function will clear the console
def clearText():
    os.system("cls" if os.name == "nt" else "clear")
    
#Clean the text input and it only accepts a string
def cleanText(user_input: str)-> str:
    cleanedText = user_input.lower().strip() #Strip any spaces and all lowercase
    cleanedText = user_input.replace(" ", "") #Replce any spaces with no spaces
    cleanedText = user_input.strip(string.punctuation) #remove special characters
    return cleanedText


#Display the results
def displayResults():
    print("Thank you for participating in this quiz!!!")
    #Display the results
    print("Here are your correct answers")
    for question_number, question in quiz_questions.items():
        for right_answers in user_attributes["correctAnswers"]:
            print(f"{question_number}, {question}")
            print(f"""{right_answers} ✔️""")



#Function to run the quiz
def runQuiz():
    #Loop through the questions
    for question_number, questions in quiz_questions.items():
            user_input = input(questions +"\n >")
            user_input = cleanText(user_input)
            while True:
                #Check if the user input is correct and add towards the correct answers list
                if user_input == quiz_answers[question_number]:
                    print("You are correct!!!!")
                    user_attributes["correctAnswers"].append(user_input)
                    #Increment the score
                    user_attributes["userScore"] += 1
                    time.sleep(1.5)
                    clearText()
                    break
                    #Check if the user input is incorrect and add towards the incorrect answers list
                elif user_input not in quiz_answers[question_number]:
                    print("You are incorrect!!!")
                    user_attributes["wrongAnswers"].append(user_input)
                    time.sleep(1.5)
                    clearText()
                    break
                elif user_input == "":
                    print("Please enter a valid input. Try again")
    #Tell the user that they have done all the questions
    print("Well done!!! You have completed all of the questions!!!")
    user_input = input("Would you like to see your results??? (yes: or no)")
    user_input = cleanText(user_input)
    #Check whether the user promts yes, no, or nothing and the program will give different responses
    while True:
        if user_input in ["yes", "y"]:
            print("Okay then, here are your results \n Hope you do well!!!!!")
            displayResults()
            break
        elif user_input in ["no", "n"]:
            print("It's okay user. You can view your results next time")
            break
        else:
            print("Please try again and answer either 'yes' or 'no")
    
    
#Function to ask the user if they are ready
def readyQuiz():
    user_input = input("Are you ready for the quiz?(yes or no): \n >")
    user_input = cleanText(user_input)
    #Check whether the user promts yes, no, or nothing and the program will give different responses
    while True:
        if user_input in ["yes", "y"]:
            print("Great! This quiz will progressively get harder as you move onto the questions! \n Good luck!!!!!!")
            time.sleep(1.5)
            clearText()
            runQuiz()
            break
        elif user_input in ["no", "n"]:
            print("It's okay user. You can play this quiz whenever you are ready ")
            exit()
            break
        else:
            time.sleep(1.5)
            clearText()
            user_input = input("Please try again and answer either 'yes' or 'no \n >")
            continue
        


def displayInstructions():
    #Display the chess pieces
    print("""                                                       .::.
                                            _()_       _::_
                                  _O      _/____\_   _/____\_
           _  _  _     ^^__      / //\    \      /   \      /
          | || || |   /  - \_   {     }    \____/     \____/
          |_______| <|    __<    \___/     (____)     (____)
    _     \__ ___ / <|    \      (___)      |  |       |  |
   (_)     |___|_|  <|     \      |_|       |__|       |__|
  (___)    |_|___|  <|______\    /   \     /    \     /    \
  _|_|_    |___|_|   _|____|_   (_____)   (______)   (______)
 (_____)  (_______) (________) (_______) (________) (________)
 /_____\  /_______\ /________\ /_______\ /________\ /________\
                                             __By Alefith 22.02.95__
""")
    print("""𝖂𝖊𝖑𝖈𝖔𝖒𝖊 𝖙𝖔 𝖙𝖍𝖎𝖘 𝖈𝖍𝖊𝖘𝖘 𝖖𝖚𝖎𝖟!""")
    #Ask the user their name
    #The user must input something
    while True:
        user_input = input("What is your name? \n >")
        user_input = cleanText(user_input)
        user_attributes["userName"] = user_input
        #if no user input, promt the user to try again.
        if not user_input:
            print("Sorry, you need to enter something. Please try again")
            time.sleep(1.5)
            clearText()
            continue
        else:
            print(f"Welcome {user_input}! Before you partake in this quiz, we need to verify your age.")
        try:
            #Ask for the user input where it only expects an int
            #Accept the user if only they are within the min age and max age.
            user_input = int(input("What is your age? \n >"))
            if user_input < MIN_AGE or user_input > MAX_AGE:
                print("Sorry, you are not within the age group. Have a nice day!!!")
                time.sleep(1.5)
                exit()
                break
            else:
                print("Welcome to this quiz!!!")
                time.sleep(1.5)
                clearText()
                readyQuiz()
                break
        except ValueError:
            user_input = input("Sorry, you must enter a valid integer. \n What is your age? \n >")

displayInstructions()

       

