#Imports

from random import randint

# Step 1: Display empty grid

def minesweeper(num):
    listt = [[0 for row in range(num)] for column in range(num)]
    counter = 0
    rns_with_bomb = []
    cns_with_bomb = []
#Randomly place bombs
    while counter < 2:
        counter += 1
        counter2 = 0
        while counter2 == 0:
            cn = randint(0,8)
            cns_with_bomb.append(cn)
            rn = randint(0,8)
            rns_with_bomb.append(rn)
            if (len(cns_with_bomb) > 1 and len(rns_with_bomb) > 1) and (cns_with_bomb[1] == cns_with_bomb[0] and rns_with_bomb[1] == rns_with_bomb[0]):
            
                del cns_with_bomb[-1]
                del rns_with_bomb[-1]
            else:
                listt[rn][cn] = "X"
                counter2 += 1

    #top left corner
        if rn == 0 and cn == 0:
            if listt[rn+1][cn] != "X":
                listt[rn+1][cn] += 1
            if listt[rn][cn+1] != "X":
                listt[rn][cn+1] += 1
            if listt[rn+1][cn+1] != "X":
                listt[rn+1][cn+1] +=1
    #bottom left corner
        elif cn == 0 and rn == 8:
            if listt[rn][cn+1] != "X":
                listt[rn][cn+1] += 1
            if listt[rn-1][cn] != "X":
                listt[rn-1][cn] += 1
            if listt[rn-1][cn+1] != "X":
                listt[rn-1][cn+1] += 1
    #bottom right corner
        elif cn == 8 and rn == 8:
            if listt[rn][cn-1]!= "X":
                listt[rn][cn-1] += 1
            if listt[rn-1][cn]!= "X":
                listt[rn-1][cn] += 1
            if listt[rn-1][cn-1]!= "X":
                listt[rn-1][cn-1] += 1
    #top right corner
        elif cn == 8 and rn == 0:
            if listt[rn][cn-1]!= "X":
                listt[rn][cn-1] += 1
            if listt[rn+1][cn-1]!= "X":
                listt[rn+1][cn-1] += 1
            if listt[rn+1][cn]!= "X":
                listt[rn+1][cn] += 1
    #left side
        elif cn == 0 and (rn > 0 and rn < 8):
            if listt[rn][cn+1]!= "X":
                listt[rn][cn+1] += 1
            if listt[rn-1][cn]!= "X":
                listt[rn-1][cn] += 1
            if listt[rn+1][cn]!= "X":
                listt[rn+1][cn] += 1
            if listt[rn-1][cn+1]!= "X":
                listt[rn-1][cn+1] += 1
            if listt[rn+1][cn+1]!= "X":
                listt[rn+1][cn+1] += 1
    #right side
        elif cn == 8 and (rn > 0 and rn < 8):
            if listt[rn][cn-1]!= "X":
                listt[rn][cn-1] += 1
            if listt[rn-1][cn]!= "X":
                listt[rn-1][cn] += 1
            if listt[rn+1][cn]!= "X":
                listt[rn+1][cn] += 1
            if listt[rn-1][cn-1]!= "X":
                listt[rn-1][cn-1] += 1
            if listt[rn+1][cn-1]!= "X":
                listt[rn+1][cn-1] += 1
    #top side
        elif (cn > 0 and cn < 8) and rn == 0:
            if listt[rn][cn+1] != "X":
                listt[rn][cn+1] += 1
            if listt[rn][cn-1] != "X":
                listt[rn][cn-1] += 1
            if listt[rn+1][cn]!= "X":
                listt[rn+1][cn] += 1
            if listt[rn+1][cn-1] != "X":
                listt[rn+1][cn-1] += 1
            if listt[rn+1][cn+1] != "X":
                listt[rn+1][cn+1] += 1
    #bottom side
        elif (cn > 0 and cn < 8) and rn == 8:
            if listt[rn][cn+1] != "X":
                listt[rn][cn+1] += 1
            if listt[rn][cn-1]!= "X":
                listt[rn][cn-1] += 1
            if listt[rn-1][cn] != "X":
                listt[rn-1][cn] += 1
            if listt[rn-1][cn+1] != "X":
                listt[rn-1][cn+1] += 1
            if listt[rn-1][cn-1] != "X":
                listt[rn-1][cn-1] += 1
    # other sides
        elif((cn != 0) and (cn != 8)) and ((rn != 0) and (rn != 8)):
            if listt[rn][cn+1] != "X":
                listt[rn][cn+1] += 1
            if listt[rn][cn-1] != "X":
                listt[rn][cn-1] += 1
            if listt[rn-1][cn] != "X":
                listt[rn-1][cn] += 1
            if listt[rn+1][cn] != "X":
                listt[rn+1][cn] += 1
            if listt[rn+1][cn+1] != "X":
                listt[rn+1][cn+1] += 1
            if listt[rn+1][cn-1] != "X":
                listt[rn+1][cn-1] += 1
            if listt[rn-1][cn-1] != "X":
                listt[rn-1][cn-1] += 1
            if listt[rn-1][cn+1] != "X":
                listt[rn-1][cn+1] += 1
    return listt    
#for row in listt:
#        print(" ".join(str(cell) for cell in row))
#        print("")
def player_map_generator(num):
    ls=[['-' for row in range(num)] for column in range(num)]
    return ls
    
def display_generator(ls):
    for row in ls:
        print(" ".join(str(cell) for cell in row))
        print("")
def check_if_won(ls):
    number_of_bombs = 2
    for row in ls:
        for cell in row:
            if cell == "-":
                number_of_bombs -= 1
    if number_of_bombs == 0:
        return True
    else:
        return False

def end_of_game(score):
    print("Game over! Your score: " + str(score)
    )
    counter = 0
    while counter < 1:
        replay_status = input("Do you want to play again? (y/n): ").lower()
        if replay_status == "y":
            counter += 1
            return True
        elif replay_status == "n":
            counter += 1
            return False
        else:
            print("Please type in a valid answer.")


def Game():
    game_status = True

    while game_status == True:
        logic_map = minesweeper(8)
        player_map = player_map_generator(8)
        display = display_generator(player_map)
        score = 0
        x = True
        while x == True:
            if check_if_won(player_map) == False:
                print("Which cell do you want to open?: ")
                rn = int(input("Row number: "))-1
                cn = int(input("Column number: "))-1

                if logic_map[rn][cn] == "X":
                    display_generator(player_map)
                    game_status = end_of_game(score)
                    x = False
                else:
                    player_map[rn][cn] = logic_map [rn][cn]
                    display_generator(player_map)
                    score += 1
            else:
                display_generator(player_map)
                print("You have Won!")
                game_status = end_of_game(score)
                x = False
if __name__ == "__main__":
    try:
        Game()
    except KeyboardInterrupt:
        print('\nEnd of Game. Bye Bye!')
