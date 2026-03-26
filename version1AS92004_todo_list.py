#Version 8.0
# This program will be about a chess quiz that ranges from difficulty--easy, medium, or hard.
#Github commit: Start the backbone of the structure and work on the welcomeText and defiining the constants and dictionaries
#Done the display insturctions and ready quiz. They run as usual
#Fixed the readyQuiz function and fixed some code on the runquiz function. Started on the displayscore functionn
#Fixed all of readyQuiz() runQuiz() welcomeText()
#Fixed the cleanText() and allows proper logic for yes, no or nothing
#Fixed the displayResults() and fixed some other bugs within the other functions
#Fixed the majority of the bugs and added some styling into the console

#TODO: Continue testing functions and search for small errors. Also add more styling to make it look pretty!!!!

#modules
import time
import os
import string
#redirect to website
import webbrowser

#Stylise
import rich
from rich.console import Console
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
)

#Stylising area

#Initialise the console
console = Console()

#This will add the progress bar that takes any message as long as its a string.
#Sourced from https://enerrio.bearblog.dev/beautiful-progress-bars-in-rich/
def progressBar(message):
    progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeRemainingColumn(),
    )
    progress_bar = progress.add_task(message, total=500)
    with progress:
        #Increment by 1 milisecond until complete (5 seconds to load)
        for _ in range(500):
            progress.update(progress_bar, advance=1)
            time.sleep(0.01)
            
#Constants
MIN_AGE = 11
MAX_AGE = 18

RANKS = ["beginner", "intermediate", "advanced"]

#Begginner thresholds
BEGINNER_THRESHOLD = 4 #This will be classified as beginner
INTERMEDIATE_THRESHOLD = 8 #This will be classified as intermediate
ADVANCED_THRESHOLD = 12 #This will be classified as advanced


#Dictionaries

#user attributes define various things the user has
user_attributes = {
    "correctAnswers": [], #correct answers will be empty for now
    "wrongAnswers": [], #wrong answers will be empty for you.
    "userName": "", #The userName will initially be an empty string
    "rank": RANKS, #Ranks defined as beginner, intermediate, advanced
    "userAnswers": {}, #This will store the users answers
    "userScore": 0 #Score is initially set as zero
}

#Questions of the quiz
quiz_questions = {
    1 : "How do you win in chess: A By Check, B: Capturing all pieces: C: Checkmate: D: Capturing the Queen",
    2 :	"True or False: The knight can jump over pieces.",
    3 : "What directions can the queen go in? A: Up, B: Down, C: side to side, D: Diagonal, E: all of the above",
    4 :	"What is a check: A: Attacking the king B: Attacking the Queen C: Attacking the pawn D: Doing nothing",
    5 :	"Can you block a check with another piece?(yes or no)",
    6 :	"Which side goes first, white or black?",
    7 :	"What pieces can the pawn change if it reaches the end of the rank: A: Queen, B: Bishop: C: Knight, D: Rook, E: All of the above",
    8 :	"True or false: The king can move more than one space.",
    9 :	"Can the pawn move up two spaces after it’s moved from its starting position?(yes or no)",
    10:	"True or False: You can capture a pawn if the pawn has moved two squares from its starting position.",
    11:	"What is a stalemate: A: Checking the king B: The king has no legal moves while not in check C: The king has nowhere to move but in check D: Just a random term.",
    12:	"Can the king castle after it was checked?(yes or no)"

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
    cleanedText = cleanedText.replace(" ", "") #Replce any spaces with no spaces
    cleanedText = cleanedText.strip(string.punctuation) #remove special characters
    return cleanedText #return the cleaned text


#Display the results
def displayResults():
    console.print("""[steel_blue3]████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗    ███████╗ ██████╗ ██████╗     ██████╗  █████╗ ██████╗ ████████╗██╗ ██████╗██╗██████╗  █████╗ ████████╗██╗███╗   ██╗ ██████╗     ██╗███╗   ██╗    ████████╗██╗  ██╗██╗███████╗     ██████╗ ██╗   ██╗██╗███████╗██╗██╗██╗
╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔════╝██╔═══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝██║██╔══██╗██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝     ██║████╗  ██║    ╚══██╔══╝██║  ██║██║██╔════╝    ██╔═══██╗██║   ██║██║╚══███╔╝██║██║██║
   ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║    █████╗  ██║   ██║██████╔╝    ██████╔╝███████║██████╔╝   ██║   ██║██║     ██║██████╔╝███████║   ██║   ██║██╔██╗ ██║██║  ███╗    ██║██╔██╗ ██║       ██║   ███████║██║███████╗    ██║   ██║██║   ██║██║  ███╔╝ ██║██║██║
   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║    ██╔══╝  ██║   ██║██╔══██╗    ██╔═══╝ ██╔══██║██╔══██╗   ██║   ██║██║     ██║██╔═══╝ ██╔══██║   ██║   ██║██║╚██╗██║██║   ██║    ██║██║╚██╗██║       ██║   ██╔══██║██║╚════██║    ██║▄▄ ██║██║   ██║██║ ███╔╝  ╚═╝╚═╝╚═╝
   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝    ██║     ╚██████╔╝██║  ██║    ██║     ██║  ██║██║  ██║   ██║   ██║╚██████╗██║██║     ██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝    ██║██║ ╚████║       ██║   ██║  ██║██║███████║    ╚██████╔╝╚██████╔╝██║███████╗██╗██╗██╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝     ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝╚═╝  ╚═══╝       ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚═╝╚═╝╚═╝
    [/steel_blue3]""")
                                                                                                                                                                                                                                                                                                    
    #Display the results
    console.print("[steel_blue3]Here are your results[/steel_blue3]")
    for question_number, question in quiz_questions.items():
        #display the user_answers or else return no answer
        #Get the user_answers, correct_answers, and wrong_answers
        user_answers = user_attributes.get("userAnswers", {})
        correct_answers = user_attributes.get("correctAnswers", [])
        wrong_answers = user_attributes.get("wrongAnswers", [])
        #Get the user answer from the  question number previously assigned.
        #If the user inputs no answer, give no answer.
        user_answer = user_answers.get(question_number, "No answer")
        #Get the user score. If there is no user score, set the score as zero.
        user_score = user_attributes.get("userScore", 0)

        #print out the questions
        print(f"{question_number}: {question}")
        
        #Correct answers
        if user_answer in correct_answers:
            result = "✅"
            console.print(f"[dark-sea-green]Your answer: {user_answer}: {result}[/dark-sea-green]")
        #wrong answers
        elif user_answer in wrong_answers:
            result = "❌"
            console.print(f"[red3]Your answer: {user_answer}: {result}[/red3]")
            console.print(f"[dark-sea-green]Correct answer: {quiz_answers[question_number]}[/dark-sea-green]")
        #No answers
        else:
            result = "😑"
            console.print(f"[yellow3]Your answer: {user_answer}: {result}[/yellow3]")
            console.print(f"[dark-sea-green]Correct answer: {quiz_answers[question_number]}[/dark-sea-green]")
    #Detemine the user's score
    #when the user score is less than or equal to the beginner threshold
    if user_score <= BEGINNER_THRESHOLD:
        console.print(f"[pink3]I'm sorry {user_attributes["userName"]}, you have a score of {user_score} out of {len(quiz_answers)}. It seems that you are a {RANKS[0]}. Have fun on your chess journey!!![/pink3]")
    #Display that they are intermediate when they score more than the beginner threshold but less than or equal to the intermediate threshold
    if BEGINNER_THRESHOLD < user_score <= INTERMEDIATE_THRESHOLD:
        console.print(f"[plum3]You seem to have a decent understanding {user_attributes["userName"]}, you have a score of {user_score} out of {len(quiz_answers)}. It seems that you are a {RANKS[1]}. You are so close to beating the quiz!!![/plum3]")
    if user_score >= ADVANCED_THRESHOLD:
        console.print(f"[violet]Good job {user_attributes["userName"]}!!! you have a score of {user_score} out of {len(quiz_answers)}. It seems that you are a {RANKS[2]}. Well done!!! You have a solid foundation of chess!!![/violet]")
    #Redirect them to the website
    while True:
        user_input = console.input("""[steel-blue3]
░██╗░░░░░░░██╗░█████╗░██╗░░░██╗██╗░░░░░██████╗░  ██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░██╗██╗░░██╗███████╗
░██║░░██╗░░██║██╔══██╗██║░░░██║██║░░░░░██╔══██╗  ╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██║██║░██╔╝██╔════╝
░╚██╗████╗██╔╝██║░░██║██║░░░██║██║░░░░░██║░░██║  ░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║█████═╝░█████╗░░
░░████╔═████║░██║░░██║██║░░░██║██║░░░░░██║░░██║  ░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║██╔═██╗░██╔══╝░░
░░╚██╔╝░╚██╔╝░╚█████╔╝╚██████╔╝███████╗██████╔╝  ░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗██║██║░╚██╗███████╗
░░░╚═╝░░░╚═╝░░░╚════╝░░╚═════╝░╚══════╝╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝╚═╝╚═╝░░╚═╝╚══════╝

███╗░░░███╗░█████╗░██████╗░███████╗
████╗░████║██╔══██╗██╔══██╗██╔════╝
██╔████╔██║██║░░██║██████╔╝█████╗░░
██║╚██╔╝██║██║░░██║██╔══██╗██╔══╝░░
██║░╚═╝░██║╚█████╔╝██║░░██║███████╗
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝

██╗███╗░░██╗███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██║██╔██╗██║█████╗░░██║░░██║██████╔╝██╔████╔██║███████║░░░██║░░░██║██║░░██║██╔██╗██║
██║██║╚████║██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║
██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

░█████╗░██████╗░░█████╗░██╗░░░██╗████████╗  ░█████╗░██╗░░██╗███████╗░██████╗░██████╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝  ██╔══██╗██║░░██║██╔════╝██╔════╝██╔════╝██╔══██╗
███████║██████╦╝██║░░██║██║░░░██║░░░██║░░░  ██║░░╚═╝███████║█████╗░░╚█████╗░╚█████╗░╚═╝███╔╝
██╔══██║██╔══██╗██║░░██║██║░░░██║░░░██║░░░  ██║░░██╗██╔══██║██╔══╝░░░╚═══██╗░╚═══██╗░░░╚══╝░
██║░░██║██████╦╝╚█████╔╝╚██████╔╝░░░██║░░░  ╚█████╔╝██║░░██║███████╗██████╔╝██████╔╝░░░██╗░░
╚═╝░░╚═╝╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░░░░╚═╝░░

░░██╗██╗░░░██╗███████╗░██████╗  ░█████╗░██████╗░  ███╗░░██╗░█████╗░██╗░░
░██╔╝╚██╗░██╔╝██╔════╝██╔════╝  ██╔══██╗██╔══██╗  ████╗░██║██╔══██╗╚██╗░
██╔╝░░╚████╔╝░█████╗░░╚█████╗░  ██║░░██║██████╔╝  ██╔██╗██║██║░░██║░╚██╗
╚██╗░░░╚██╔╝░░██╔══╝░░░╚═══██╗  ██║░░██║██╔══██╗  ██║╚████║██║░░██║░██╔╝
░╚██╗░░░██║░░░███████╗██████╔╝  ╚█████╔╝██║░░██║  ██║░╚███║╚█████╔╝██╔╝░
░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░  ░╚════╝░╚═╝░░╚═╝  ╚═╝░░╚══╝░╚════╝░╚═╝░░\n >[/steel-blue3]""")
        user_input = cleanText(user_input)
        #If yes, then redirect them towards the website. 
        # If no, then politely exit the program. 
        # Else ask them to reinput their thing
        if user_input in ["yes", "y"]:
            console.print("[dark_sea_green]Okay then!!! Here is lichess! This will help you understand more on chess!!!![/dark_sea_green]")
            webbrowser.open("https://lichess.org/")
            break
        elif user_input in ["no", "n"]:
            console.print("[orange3]Awww it's okay!!! Thank you for participating in this quiz!!! Have a nice day!!!!![/orange3]")
            exit()
            break
        else:
            console.print("[red3]Please enter either 'yes', or 'no'[/red3]")
        
#Function to run the quiz
def runQuiz():
    #Loop through the questions
    for question_number, questions in quiz_questions.items():
                user_input = input(questions +"\n >")
                user_input = cleanText(user_input)
                #Allow the user to input nothing and continue the program
                if user_input == "":
                    console.print("[orange3]Don't wory if you don't answer! It's fine if you don't know! We will move onto the next question.[/orange3]")
                    time.sleep(1.5)
                    clearText()
                #Check if the user input is correct and add towards the correct answers list
                elif user_input == quiz_answers[question_number]:
                    console.print("[dark_sea_green]You are correct!!!![/dark_sea_green]")
                    user_attributes["correctAnswers"].append(user_input)
                    #Add the answer to the user's answers and assign it to the question number
                    user_attributes["userAnswers"][question_number] = user_input
                    #Increment the score
                    user_attributes["userScore"] += 1
                    time.sleep(1.5)
                    clearText()
                #Check if the user input is incorrect and add towards the incorrect answers list
                elif user_input not in quiz_answers[question_number]:
                    console.print("[red3]You are incorrect!!![/red3]")
                    user_attributes["wrongAnswers"].append(user_input)
                    #Add the answer to the user's answers and assign it to the question number
                    user_attributes["userAnswers"][question_number] = user_input
                    time.sleep(1.5)
                    clearText()
    #Tell the user that they have done all the questions
    print("Well done!!! You have completed all of the questions!!!")
    #Check whether the user promts yes, no, or nothing and the program will give different responses
    while True:
        user_input = input("Would you like to see your results??? (yes: or no)")
        user_input = cleanText(user_input)
        #let the user see the results if they say yes
        if user_input in ["yes", "y"]:
            console.print("[dark_sea_green]Okay then, here are your results \n Hope you do well!!!!![/dark_sea_green]")
            progressBar("Loading results")
            time.sleep(1.5)
            clearText()
            displayResults()
            break
        #Exit the program if the user says no
        elif user_input in ["no", "n"]:
            print("It's okay user. You can view your results next time")
            exit()
            break
        #Ask the user for a valid input until they either say yes or no.
        else:
            print("Please try again and answer either 'yes' or 'no")
    
    
#Function to ask the user if they are ready
def readyQuiz():
    #Check whether the user promts yes, no, or nothing and the program will give different responses
    while True:
        user_input = input("Are you ready for the quiz?(yes or no): \n >")
        user_input = cleanText(user_input)
        if user_input in ["yes", "y"]:
            print("Great! This quiz will progressively get harder as you move onto the questions!")
            console.print("""[steel_blue3]
░██████╗░░█████╗░░█████╗░██████╗░  ██╗░░░░░██╗░░░██╗░█████╗░██╗░░██╗██╗██╗██╗██╗██╗██╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗  ██║░░░░░██║░░░██║██╔══██╗██║░██╔╝██║██║██║██║██║██║
██║░░██╗░██║░░██║██║░░██║██║░░██║  ██║░░░░░██║░░░██║██║░░╚═╝█████═╝░██║██║██║██║██║██║
██║░░╚██╗██║░░██║██║░░██║██║░░██║  ██║░░░░░██║░░░██║██║░░██╗██╔═██╗░╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝  ███████╗╚██████╔╝╚█████╔╝██║░╚██╗██╗██╗██╗██╗██╗██╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░  ╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝
[/steel_blue3]""")
            #Display the progress bar with the message loading quiz
            progressBar("Loading quiz")
            time.sleep(1.5)
            clearText()
            runQuiz()
            break
        elif user_input in ["no", "n"]:
            console.print("It's okay user. You can play this quiz whenever you are ready ")
            exit()
            break
        else:
            time.sleep(1.5)
            clearText()
            print("Please try again and answer either 'yes' or 'no")


def displayInstructions():
    #Display the chess pieces
    console.print("""
    [steel_blue3]
                  .::.
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
[/steel_blue3]""")
    console.print("""[medium_purple]𝖂𝖊𝖑𝖈𝖔𝖒𝖊 𝖙𝖔 𝖙𝖍𝖎𝖘 𝖈𝖍𝖊𝖘𝖘 𝖖𝖚𝖎𝖟![/medium_purple]""")
    #Ask the user their name
    #The user must input something
    while True:
        user_input = console.input("[dark_sea_green]What is your name? \n >[/dark_sea_green]")
        user_input = cleanText(user_input)
        user_attributes["userName"] = user_input
        #if no user input, promt the user to try again.
        if not user_input:
            console.print("[red3]Sorry, you need to enter something. Please try again[/red3]")
            time.sleep(1.5)
            clearText()
            continue
        else:
            console.print(f"[dark_sea_green]Welcome {user_input}! Before you partake in this quiz, we need to verify your age.[/dark_sea_green]")
            break
    while True:
        try:
            #Ask for the user input where it only expects an int
            #Accept the user if only they are within the min age and max age.
            user_input = int(console.input("[dark_sea_green]What is your age? \n >[/dark_sea_green]"))
            if user_input < MIN_AGE or user_input > MAX_AGE:
                console.print("[red3]Sorry, you are not within the age group. Have a nice day!!![/red3]")
                time.sleep(1.5)
                exit()
                break
            else:
                #Allow them to enter the quiz and break the while true loop
                console.print("[dark_sea_green]Welcome to this quiz!!![/dark_sea_green]")
                time.sleep(1.5)
                clearText()
                readyQuiz()
                break
        #Continue asking the user until it enters a valid int.
        except ValueError:
            console.print("[red3]Sorry, you must enter a valid integer[/red3]")

displayInstructions()