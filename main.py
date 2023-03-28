from EntytyOrientedGameEngine import *


def main():

    initPlayer()

    while True:

        i = 0

        while i <= len(Entytes):
            Entytes(i).cheklive

        action = input()

        if action == "join":
            iam = Player()

        elif action == "add entyty":
            added = Player()

        elif action == "attack":
            mes("Enter target:")
            target = input()
            mes("Enter power of attack:")
            damage = int(input())
            Entytes(iam.name).attack(damage, target)

        elif action == "move":
            mes("Enter distance x:")
            xn = int(input())
            mes("also y:")
            yn = int(input())
            Entytes(iam.name).move(iam.x, iam.y, xn, yn)

        elif action == "exit":
            quit(0)

        elif action == "set block":
            mes("Enter location")
            mes("x:")
            blockx = int(input())
            mes("y:")
            blocky = int(input())
            if Entytes(iam.name).x + 1 or - 1 == blockx and Entytes(iam.name).y + 1 or - 1 == blocky:
                new = Block(x=blockx, y=blocky)
            elif Entytes(iam.name).x == blockx and Entytes(iam).y == blocky:
                mes("You can't create block at youself")
                main()
            else:
                mes("It not near")
                main()

        else:
            mes("incoorrect action")
            main()

if __name__ == "__main__":
    main()