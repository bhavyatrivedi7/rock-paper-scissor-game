from random import*
rounds=int(input("select rounds from 1 to 5"))
for i in range(1,6):
    if(rounds+1==i):
        print("match over")
        break
    t = ["rock", "paper", "scissors"]
    computer = t[randint(0,2)]
    player = False
    while player == False:
        player = input("rock, paper, scissors?..Choose one: ")
        if player == computer:
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "paper":
            if computer == "scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "scissors":
            if computer == "rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")
            player = False
