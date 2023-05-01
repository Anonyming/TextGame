import EntytyOrientedGameEngine as EOGE  # import game engine

def main():

    EOGE.initPlayer()  # init the player

    i = 30
    for i in range(0, 30):  # the main game

        i = 0  # check death entytes
        while i <= len(EOGE.Entytes):
            EOGE.Entytes[i].checklive

        print(f'You have {i} turns')
        print("Enter action")
        action = input()  # input, that player wanna do

        if action == "add entyty":  # add a passive entyty
            added = EOGE.Player()

        elif action == "attack":  # attack an entyty
            print("Enter target:")
            target = input()
            print("Enter power of attack:")
            damage = int(input())
            EOGE.Entytes(EOGE.iam.name).attack(damage, target)

        elif action == "move":  # go to some coordinates
            print("Enter distance x:")
            xn = int(input())
            print("also y:")
            yn = int(input())
            EOGE.Entytes(EOGE.iam.name).move(EOGE.iam.x, EOGE.iam.y, xn, yn)

        elif action == "exit":  # leave the game
            quit(0)

        elif action == "set block":  # set a block
            print("Enter location")
            print("x:")
            blockx = int(input())
            print("y:")
            blocky = int(input())
            if EOGE.Entytes(EOGE.iam.name).x + 1 or - 1 == blockx and EOGE.Entytes(EOGE.iam.name).y + 1 or - 1 == blocky:  # all's good
                new = EOGE.Block(x=blockx, y=blocky)
            elif EOGE.Entytes(EOGE.iam.name).x == blockx and EOGE.Entytes(EOGE.iam).y == blocky:  # tried create a block on self
                print("You can't create block at yourself")
                main()
            else:  # tried to create block not near with self
                print("It not near")
                main()

        else:  # not understand action
            print("incorrect action")
            main()

        i = i - 1
    print("YOU HAVEN'T TURNS")
    menu()

def menu():
    print("MENU")
    print("1) NEW GAME")
    print("2) EXIT")
    print("ENTER NUMBER OF CHOSEN")
    __chose = int(input())
    if __chose == 1:
        main()
    elif __chose == 2:
        quit(1)
    else:
        print("Action is not supported")
        menu()

if __name__ == "__main__":
    menu()

