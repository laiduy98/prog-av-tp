import column
import pawn
import grid

print('ex1----')

# ex1
c = column.Column(2)
print(c)

print('ex2----')

# ex2
c.drop(pawn.Pawn('X'))
c.drop(pawn.Pawn('X'))

print('ex3----')

# ex3
g = grid.Grid(2, 3)
p1 = pawn.Pawn('X')
g.drop(0, p1)
