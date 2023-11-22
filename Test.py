import random

def roll_dice():
    return random.randint(1, 6)

def additional_roll(total):
    if total < 8:
        print("Computer decides to roll again.")
        return roll_dice()
    else:
        return 0

def play_game():
    while True:
        player_total = sum([roll_dice() for _ in range(2)])
        player_total *= 1.5 if player_total % 11 == 0 else 1

        computer_total = sum([roll_dice() for _ in range(2)])
        computer_total *= 1.5 if computer_total % 11 == 0 else 1

        print(f"You rolled: {player_total}")
        print(f"Computer rolls: {computer_total}")

        if player_total >= 12:
            print("You win with a total of 12!")
            return "Player"

        if computer_total >= 12:
            print("Computer wins with a total of 12!")
            return "Computer"

        choice = input("Would you like to roll again or stick (roll/stick): ").lower()
        if choice == 'roll':
            player_add_dice = roll_dice()
            player_total += player_add_dice
            print(f"You rolled additional dice: {player_add_dice} - New Total: {player_total}")
            if player_total == 12:
                print("You win with a total of 12!")
                return "Player"
            elif player_add_dice == player_total / 1.5:
                print("You win with a triple!")
                return "Player"
        else:
            print(f"You stick with - Total: {player_total}")

        computer_add_dice = additional_roll(computer_total)
        if computer_add_dice > 0:
            computer_total += computer_add_dice
            print(f"Computer rolls additional dice: {computer_add_dice} - New Total: {computer_total}")

        if player_total >= 12:
            print("You win!")
            return "Player"
        elif computer_total >= 12:
            print("Computer wins!")
            return "Computer"

# Play the game
winner = play_game()
print(f"The winner is {winner}!")

