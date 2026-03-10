#Version "1".0
# This pro"g"ram will be about a chess quiz that ranges from difficulty--easy, medium, or hard.
#Github commit: Start the backbone of the structure and work on the welcomeText and defiining the constants and dictionaries

#modules
import time
import os



#Constants
MIN_AGE = 11
MAX_AGE = 18

RANKS = ["beginner", "intermediate", "advanced"]

#Dictionaries

#user attributes define various things the user has
user_attributes = {
    "isCompletedQuiz": False,
    "userAnswrs": [], #The user answers will display in a list
    "userName": "", #The userName will initially be an empty string
    "rank": RANKS #Ranks defined as beginner, intermediate, advanced
}

#Questions of the quiz
quiz_questions = {
    "1." : 	"How do you win in chess?",
    "2." :	"True or False: The knight can jump over pieces.",
    "3." : 	"What directions can the queen go in? A: Up, B: Down, C: side to side, D: Diagonal, E: all of the above",
    "4." :	"What is a check?",
    "5." :	"Can you block a check with another piece?",
    "6." :	"Which side goes first, white or black?",
    "7." :	"What pieces can the pawn change if it reaches the end of the rank?",
    "8." :	"True or false: The king can move more than one space.",
    "9." :	"Can the pawn move up two spaces after it’s moved from its starting position?",
    "10.":	"True or False: You can capture a pawn if the pawn has moved two squares from its starting position.",
    "11.":	"What is a stalemate?",
    "12.":	"Can the king castle after it was checked?"

}

#key words or answers of the quiz:
quiz_answers = {}

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


displayInstructions()
