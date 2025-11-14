import random
while True:
    input_1 = input("heads or tails: ").replace(" ", "").lower().strip()
    AI = random.choice(["heads" , "tails"])

    if input_1 not in ["heads" , "tails"]:
        print("heads or tails")
        continue

    if input_1 == AI:
        print(f"you voted for {input_1}, the coin is showing {AI}")
        print("you won")
        break

    else:
        print(f"you voted for {input_1}, the coin is showing {AI}")
        print("you lost")
import random
player_input = input(" 'HEADS' or 'TAILS' : ").replace(" ", "").lower().strip()
while True:

    AI =random.choice(["heads", "tails"])

    if player_input not in ["heads" , "tails"]:
        print("don't waste my time")
        continue
    if player_input == AI:
        print(" you evade the enemy's attack")
        break
    else:
        print("you are caught by the enemy")
        break


