import random
import time


#NOTE: DONT FORGET TO REMOVE THE "pass" KEYWORDS!!!!


def introduction():
    # TODO: Add an introduction message for the game (optional)
    pass


def MainMenu():
    # TODO: Ask the player for their name and display the main menu 
    # (i.e 'Welcome! [name]! ==== main menu prompt(s))
    pass
 

def acceptOrDecline():
    # TODO: Ask the player if they accept or decline the challenge (a/d or accept/decline) alongside making sure it repeats UNTIL a valid answer is recognized (such as the ones provided in the list) 
    choices2 = ["a", "d", "accept", "decline"]
    while True:
        pass
        

def userChoice():
    # TODO: Prompt the player to enter rock, paper, or scissors and validate the input (WHILE ALSO MAKING SURE A VALID ANSWER IS INPUTTED)
    choices = ["rock", "paper", "scissors"]
    while True:
        pass


def AI(player_choices):
    # TODO: Implement AI logic to choose based on the player's past choices
    # If there are fewer than 2 player choices, choose randomly
    # Otherwise, counter the player's most common choice
    choices = ["rock", "paper", "scissors"]

    def AIChoice():
        if len(player_choices) < 2:
            return random.choice(choices)
        else:
            rock_count = player_choices.count("rock")
            paper_count = player_choices.count("paper")
            scissors_count = player_choices.count("scissors")

            # TODO: Implement several conditional statements for the counter aspect of the AI.  (i.e. HINT: if _ is greater than or equal to and _ and its also greater than or equal to _ then _. )
            pass

    
    # AI thinking animation
    print("\nThe AI is thinking", end="", flush=True)
    for i in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        print("\b\b\b   \b\b\b", end="", flush=True)
    time.sleep(1)

    
    # TODO: Return AI's final choice while also printing it out.
    computerChoice = AIChoice()
    pass


def detWinner(user_choice, computerChoice):
    # TODO: Implement the logic to determine the winner
    # Return "Player" if the player wins, "Computer" if the AI wins, or "Tie" if it's a tie
    pass



def playAgain():
    # TODO: Ask the player if they want to play again and validate the input
    options = ["y", "n", "yes", "no"]
    while True:
        pass