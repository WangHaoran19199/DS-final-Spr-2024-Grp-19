from AlphaBetaChessTree import AlphaBetaChessTree

import chess
from TreeNode import TreeNode

def main():
    fen = "4k2r/6r1/8/8/8/8/3R4/R3K3 w Qk - 0 1"
    fen="r1bq1rk1/ppp2ppp/2n5/1B6/1Q6/4P3/2N2PPP/R1B1K2R b KQ - 1 1"
    chess_tree = AlphaBetaChessTree(fen)
    #print(chess_tree.get_supported_evaluations())
    #print(chess_tree.rboard)
    #print (chess_tree._get_legal_moves(chess_tree.root))

    #tboard=chess.Board(fen)
    #tnd=TreeNode(tboard,True)
    #print(tnd._board)
    #print()
    #chess_tree._apply_move(chess_tree._get_legal_moves(tnd)[0],tnd,"UCI")
    #print(tnd._board)

    #print(chess_tree._evaluate_board(chess_tree.rboard))

    best = chess_tree.get_best_next_move(chess_tree.fenstr, 3)
    print("Best move:", best)

    # Please implement your own main function to test the AlphaBetaChessTree class.
    # Try various FEN strings and different depths to see how your algorithm performs.
    # You can also implement your own evaluation functions to test the algorithm with different strategies.
    # For example, you could implement a simple evaluation function that counts the material value of the pieces.
    # (optional) It is recommended to implement methods to visualize your board state and moves.
    # (optional) It is recommended to support the export of tree statistics to understand tree pruning.

    # Feel free to add additional FEN strings and test cases to further evaluate your algorithms below.


if __name__ == "__main__":
    main()
