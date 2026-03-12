#Version 2.0
# This program will be about a chess quiz that ranges from difficulty--easy, medium, or hard.
#Github commit: Start the backbone of the structure and work on the welcomeText and defiining the constants and dictionaries

#TODO Fix the displayInstructions to accept the user to try again with the input

#modules
import time
import os
import string

#Constants
MIN_AGE = 11
MAX_AGE = 18

RANKS = ["beginner", "intermediate", "advanced"]

#Begginner thresholds


#Dictionaries

#user attributes define various things the user has
user_attributes = {
    "isCompletedQuiz": False,
    "userAnswrs": [], #The user answers will display in a list
    "correctAnswers": [], #correct answers will be empty for now
    "wrongAnswers": [], #wrong answers will be empty for you.
    "userName": "", #The userName will initially be an empty string
    "rank": RANKS, #Ranks defined as beginner, intermediate, advanced
}

#Questions of the quiz
quiz_questions = {
    1 : 	"How do you win in chess?",
    2 :	"True or False: The knight can jump over pieces.",
    3 : 	"What directions can the queen go in? A: Up, B: Down, C: side to side, D: Diagonal, E: all of the above",
    4 :	"What is a check?",
    5 :	"Can you block a check with another piece?",
    6 :	"Which side goes first, white or black?",
    7 :	"What pieces can the pawn change if it reaches the end of the rank?",
    8 :	"True or false: The king can move more than one space.",
    9 :	"Can the pawn move up two spaces after it’s moved from its starting position?",
    10:	"True or False: You can capture a pawn if the pawn has moved two squares from its starting position.",
    11:	"What is a stalemate?",
    12:	"Can the king castle after it was checked?"

}

#key words or answers of the quiz:
quiz_answers = {}


# This function will clear the console
def clearText():
    os.system("cls" if os.name == "nt" else "clear")
    
#Clean the text input and it only accepts a string
def cleanText(user_input: str)-> str:
    cleanedText = user_input.lower().strip() #Strip any spaces and all lowercase
    cleanedText = user_input.replace(" ", "") #Replce any spaces with no spaces
    cleanedText = user_input.strip(string.punctuation) #remove special characters
    return cleanedText
    
    
#Function to ask the user if they are ready
def readyQuiz():
    print("This is the ready quiz function running!!")    


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
        #Set the isNotEmpty to true for now
        user_input = input("What is your name? \n >")
        user_input = cleanText(user_input)
        user_attributes["userName"] = user_input
        if not user_input:
            print("Sorry, you need to enter something. Please try again")
            break
        else:
            print(f"Welcome {user_input}! Before you partake in this quiz, we need to verify your age.")
        try:
            user_input = int(input("What is your age? \n >"))
            if user_input < MIN_AGE or user_input > MAX_AGE:
                print("Sorry, you are not within the age group. Have a nice day!!!")
                time.sleep(1.5)
                exit()
            else:
                print("Welcome to this quiz!!!")
                displayInstructions()
        except ValueError:
            print("Sorry, you must enter a valid integer.")
            break
        #Ask for the user input where it only expects an int

displayInstructions()

       

