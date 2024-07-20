from random import randint

def update_score(score, die_value):
    if die_value == 1:
        return 0
    else:
        return score + die_value
    
def display_scoreboard(player_core, computer_score):
    print()
    print("#" * 20)
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    print("#" * 20)
    print()

def player_turn(username):
    turn_score = 0
    while True:
        roll = input(f"Press 'Enter' to roll the die, {username}, or type 'hold' to hold your turn")
        if roll.lower() == 'hold':
            break
        die_value = randint(1, 6)
        print(f"{username} rolls a {die_value}")
        if die_value == 1:
            print(f"Oh no! {username} rolled a 1 and loses all points for this turn")
            turn_score = 0
            break
        else:
            turn_score += die_value
            print(f"{username} current turn score: {turn_score}")
    return turn_score

def computer_turn():
    turn_score = 0
    while turn_score < 10:
        die_value = randint(1, 6)
        print(f"Computer rolls a {die_value}")
        if die_value == 1:
            print("Computer rolled a 1  and loses all points for this turn!")
            turn_score = 0
            break
        else:
            turn_score += die_value
            print(f"Computer current turn score: {turn_score}")
            return turn_score

player_score = 0
computer_score = 0

welcome_message = """ Welcome to 'Bones', a dice game! In this game, a user and a computer opponent roll a 6-sided die each
round. If the value of the die is a 1, the player that rolled the 1 loses all of their points for that turn. Otherwise, the player 
gets the value of the die added to their turn points. The player can decide to roll again or hold. the first player to reach
300 points wins !!1"""

print(welcome_message)
username = input("what is your name? : ")
round_number = 1

while True:
    print(f"\nRound {round_number}")
    print(f"{username}'s turn")
    player_turn_score = player_turn(username)
    player_score = update_score(player_score, player_turn_score)
    if player_score >= 300:
        display_scoreboard(player_score, computer_score)
        print(f"{username} wins!")
        break
    print("Computer's Turn")
    computer_turn_score = computer_turn()
    computer_score = update_score(computer_score, computer_turn_score)

    display_scoreboard(player_score, computer_score)

    if computer_score >= 300:
        print("Computer wins!!")
        break

    round_number += 1
