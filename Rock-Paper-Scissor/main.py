from random import randint

title = "Rock-Paper-Scissor Game"
print(title)
print(f"{'=' * len(title)}")

weapon = ("rock", "paper", "scissor")

player = input("Chose your weapon(rock | paper | scissor): ")
compter = weapon[randint(0,2)]

if player == computer:
    print("Player uses", player)
    print("computer uses", computer)
    print("Nobody wins!")
elif player == "rock":
    if computer == "paper":
        print("Player uses", player)
        print("computer uses", computer)
        print("computer wins!")
    elif computer == "scissor":
        print("Player uses", player)
        print("computer uses", computer)
        print("player wins!")
elif player == "paper":
    if computer == "rock":
        print("Player uses", player)
        print("computer uses", computer)
        print("computer wins!")
    elif computer == "scissor":
        print("Player uses", player)
        print("computer uses", computer)
        print("player wins!")
elif player == "scissor":
    if computer == "rock":
        print("Player uses", player)
        print("computer uses", computer)
        print("computer wins!")
    elif computer == "paper":
        print("Player uses", player)
        print("computer uses", computer)
        print("player wins!")
else:
    print("Wrong Weapon")



