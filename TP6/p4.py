from pawn import Pawn
from grid import Grid


def main():
    try:
        while True:
            print('Enter dimension of the game.')
            row_num = input('Input number of row: ')
            column_num = input('Input number of column: ')

            g = Grid(int(row_num), int(column_num))
            p1 = Pawn('X')
            p2 = Pawn('O')

            i = 0
            try:
                while True:

                    if i % 2 == 0:
                        print('Player 1 go:')
                        chosen_column = input('Choose column to drop: ')
                        g.drop(int(chosen_column)-1, p1)
                    if i % 2 == 1:
                        print('Player 2 go:')
                        chosen_column = input('Choose column to drop: ')
                        g.drop(int(chosen_column)-1, p2)

                    i += 1
            except KeyboardInterrupt:
                pass

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
