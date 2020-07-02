
from Queen_Board import Chess,GeneticChess

'''Single GA solution ---------------------------------'''
# dimension = int(input("Enter board dimension: "))
chess = GeneticChess(8)
solution = chess.solveGA()
board = chess.createBoard(chess.size)
chess.setBoard(board,solution)
print("Solution:")
print(solution)

def solveProblem():
    if choice.get() == 1:
        chess = Chess(int(n.get()))
        chess.solveBackTracking(0)
        solution = chess.solutions[0]
        for solution in chess.solutions:
            for row in solution:
                print(row)
            print("")
        chess.showBoardGui(solution)
    elif choice.get() == 2:
        chess = GeneticChess(int(n.get()))
        solution = chess.solveGA()
        board = chess.createBoard(chess.size)
        chess.setBoard(board,solution)
        print("Solution:")
        print(solution)
        

