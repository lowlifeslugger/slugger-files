import random
name = input("name?: ").lower().strip()
while True:

    print("picks up gun")
    choice = input(f"SHOOT bot or {name}").lower().strip().replace(" ","")
    n = 6

    revolver = ["live"] + ["blank"]*(n-1)
    random.shuffle(revolver)
    gun = revolver.pop(0)


    if choice not in ["bot" , name]:
        print("pick one")
        continue

    if choice == "bot":
        if gun == "live":
            print(" bot is dead")
            break
    if choice == "bot":
        if gun == "blank":
            print(" bot is alive")
            continue
    if choice == name:
        if gun == "live":
            print(f"{name} is dead ")
            break
    if choice == name:
        if gun == "blank":
            print(f"{name} is alive")
            continue




------------------------------------------------------------------------------------------------------------------------------

import random
name = input("name?: ").lower().strip().replace(" ","")
n = 6
revolver = ["live"] + ["blank"]*(n-1)
random.shuffle(revolver)
while True:

    print("picks up gun")
    choice = input(f"SHOOT bot or {name}").lower().strip().replace(" ","")

    gun = revolver.pop(0)


    if choice not in ["bot" , name]:
        print("pick one")
        continue

    if choice == "bot":
        if gun == "live":
            print(" bot is dead")
            break
    if choice == "bot":
        if gun == "blank":
            print(" bot is alive")
            continue
    if choice == name:
        if gun == "live":
            print(f"{name} is dead ")
            break
    if choice == name:
        if gun == "blank":
            print(f"{name} is alive")
            continue
