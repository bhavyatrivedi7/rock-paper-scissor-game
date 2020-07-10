from random import randint
val = 0
vals = 0
rounds=int(input("select rounds from 1 to 5"))
if(rounds>5):
    print("not valid..anyways play for 5 rounds")
for i in range(1,6):
    if(rounds+1==i):
        print("match over")
        if vals > val:
            print("bhavya win:", vals)
        elif vals < val:
            print("computer win", val)
        else:
            print("game is tie")
        break
    t = ['rock', 'paper', 'scissor']
    computer = t[randint(0, 2)]
    player = False
    while player == False:
        player = input("Rock,Paper,Scissor?")
        print("computer choice is :", computer)
        if player == computer:
            print("the game is tie")
        elif player == 'rock':
            if computer == 'paper':
                print("computer wins!!!!!!!!")
                val = val + 1

            else:
                print("bhavya wins!!!!!!!!!")
                vals = vals + 1


        elif player == 'scissor':
            if computer == 'rock':
                print("computer wins!!!!!!")
                val = val + 1


            else:
                print("bhavya wins!!!!!!!!")
                vals = vals + 1

        elif player == 'paper':
            if computer == 'scissor':
                print("computer wins!!!!!!!!")
                val = val + 1

            else:
                print("bhavya wins!!!!!!!!")
                vals = vals + 1

        else:
            print("Something went wrong")
    player = False
    computer = t[randint(0, 2)]

print("thanks for playing")
