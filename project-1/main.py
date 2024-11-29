from functions import introduction, userChoice, AI, detWinner, playAgain, acceptOrDecline, MainMenu

def main():
    introduction()
    MainMenu()

    pWins = 0  # Player's wins
    cWins = 0  # AI's wins
    ties = 0   # Tie count
    player_choices = []  # Store player's previous choices

    while True:
        # TODO: Call acceptOrDecline() to check if the player accepts the AI challenge
        # If they decline, break out of the loop

        while True:
            # TODO: Get player's choice by calling userChoice()

            # TODO: Get AI's choice by calling AI() and passing the player_choices

            # TODO: Determine the winner by calling detWinner() with player and AI choices

            # TODO: Update the scores based on the winner

            # TODO: Display the current scores

            # TODO: Ask if the player wants to play again using playAgain()
            # If they decline, break the loop

            pass #NOTE: REMOVE THIS "pass" WHEN YOU START WORKING ON IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        break  # Break out of the main loop if the player doesn't accept the challenge

    # TODO: Display the final scores

    # TODO: Display a final message based on who won more games (player or AI)

if __name__ == "__main__":
    main()