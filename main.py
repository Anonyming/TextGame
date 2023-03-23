import EntytyOrientedGameEngine.EntytyOrientedGameEngine as engine

def initPlayer():
    iam = engine.Player()
    engine.mes("Creating your player ...")

def main():

    initPlayer()

    while True:

        i = 0

        while i <= len(engine.Entytes):
            engine.Entytes(i).cheklive

        action = input()

        if action == "join":
            iam = engine.Player()

        elif action == "add entyty":
            added = engine.Player()

        elif action == "attack":
            engine.text("Enter target:")
            target = input()
            engine.text("Enter power of attack:")
            damage = int(input())
            engine.Entytes(iam).attack(damage, target)

        elif action == "move":
            engine.text("Enter distance x:")
            xn = int(input())
            engine.text("also y:")
            yn = int(input())
            engine.Entytes(iam).move(iam.x, iam.y, xn, yn)

        elif action == "exit":
            quit(0)

        elif action == "set block":
            engine.text("Enter location")
            engine.text("x:")
            blockx = int(input())
            engine.text("y:")
            blocky = int(input())
            if engine.Entytes(iam).x + 1 or - 1 == blockx and engine.Entytes(iam).y + 1 or - 1 == blocky:
                new = engine.Block()
                engine.Blocks(len(engine.Blocks)).y = blocky
                engine.Blocks(len(engine.Blocks)).x = blockx
            elif engine.Entytes(iam).x == blockx and engine.Entytes(iam).y == blocky:
                engine.text("You can't create block at youself")
                main()
            else:
                engine.text("It not near")
                main()

        else:
            engine.text("incoorrect action")
            main()

if __name__ == "__main__":
    main()