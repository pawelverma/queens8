
from queens8_gen_algo import Chess,GeneticChess

'''Single GA solution ---------------------------------'''
# dimension = int(input("Enter board dimension: "))
chess = GeneticChess(8)
solution = chess.solveGA()
board = chess.createBoard(chess.size)
chess.setBoard(board,solution)
print("Solution:")
print(solution)


        

