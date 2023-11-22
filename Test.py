import random


def roll_dice():
    return random.randint(1, 6)


def play_game():
    player_score = 0
    computer_score = 0
    draws = 0

    while True:
        #   Roll dice for player and computer
        player_dice1 = roll_dice()
        player_dice2 = roll_dice()
        computer_dice1 = roll_dice()
        computer_dice2 = roll_dice()

        player_total = player_dice1 + player_dice2
        if player_dice1 == player_dice2:
            player_total = player_dice1 + player_dice2 / 0.5

        computer_total = computer_dice1 + computer_dice2
        if computer_dice1 == computer_dice2:
            computer_total = computer_dice1 + computer_dice2 / 0.5

        print(f"You rolled: {player_dice1}, {player_dice2} - Total: {player_total}")
        print(f"Computer rolls: {computer_dice1}, {computer_dice2} - Total: {computer_total}")

        #   Check if player or computer wins or loses
        #   If both scores are greater than 12 or both equal to 12, it is a draw.
        if player_total >= 12 and computer_total >= 12:
            print("You both rolled a 12 or higher. Draw")
            return "Draw"

        #   If one of the scores is greater than 12 the other player automatically wins.
        if player_total > 12:
            print("You rolled higher than 12. Computer wins!")
            return "Computer"
        elif computer_total > 12:
            print("Computer rolled higher than 12. Player wins!")
            return "Player"

        #   If one of the scores is equal to twelve, that player wins.
        if player_total == 12:
            print("You win with a total of 12!")
            return "Player"
        elif computer_total == 12:
            print("Computer wins with a total of 12!")
            return "Computer"

        if player_total == computer_total and player_total < 12:
            print("It's a draw. Roll again.")
            continue

        # Additional dice time
        player_add_dice = roll_dice()
        computer_add_dice = roll_dice()

        if computer_total != player_total and player_total < computer_total:
            if computer_total < 8:
                print("Computer decides to roll again.")
                computer_total += computer_add_dice
                print(
                    f"Computer rolls an additional dice: {computer_add_dice} - New total: {computer_total}")
            else:
                print("Computer sticks.")
            choice = input("Would you like to roll again or stick (roll/stick): ").lower()
            if choice == 'roll':
                player_total += player_add_dice
                print(f"You rolled additional dice: {player_add_dice} - New Total: {player_total} ")
            else:
                print(f"You stick with - Total: {player_total}")

        if computer_total != player_total and player_total > computer_total:
            choice = input("Would you like to roll again or stick (roll/stick): ").lower()
            if choice == 'roll':
                player_total += player_add_dice
                print(f"You rolled additional dice: {player_add_dice} - New Total: {player_total} ")
            else:
                print(f"You stick with - Total: {player_total}")
            if computer_total < 8:
                print("Computer decides to roll again.")
                computer_total += computer_add_dice
                print(
                    f"Computer rolls an additional dice: {computer_add_dice} - New total: {computer_total}")
            else:
                print("Computer sticks.")

        # Check for triple for the player
        if player_add_dice == player_dice1 == player_dice2:
            print("You win with a triple!")
            return "Player"
        elif computer_add_dice == computer_dice1 == computer_dice2:
            print("The computer wins with a triple!")
            return "Computer"

        #   If both scores are greater than 12 or both equal to 12, it is a draw.
        if player_total >= 12 and computer_total >= 12:
            print("You both rolled a 12 or higher. Draw")
            return "Draw"

        #   If both scores are equal and less than 12
        if player_total == computer_total and computer_total < 12:
            print("You both rolled the exact number. Draw")
            return "Draw"

        #   If one of the scores is equal to twelve, that player wins.
        if player_total == 12:
            print("You win with a total of 12!")
            return "Player"
        elif computer_total == 12:
            print("Computer wins with a total of 12!")
            return "Computer"

        #   If one of the scores is greater than 12 the other player automatically wins.
        if player_total > 12:
            print("You rolled higher than 12. Computer wins!")
            return "Computer"
        elif computer_total > 12:
            print("Computer rolled higher than 12. Player wins!")
            return "Player"

        # Check for final win condition
        if player_total < computer_total:
            print("You lose!")
            return "Computer"
        elif computer_total < player_total:
            print("You win!")
            return "Player"

        if player_total == computer_total and player_total <= 12:
            print("It's a draw.")
            return "Draw"


# Play the game
winner = play_game()
print(f"The winner is {winner}!")
