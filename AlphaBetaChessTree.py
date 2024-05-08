from TreeNode import TreeNode
import chess

class AlphaBetaChessTree:
    def __init__(self, fen):
        """
        Initializes an AlphaBetaChessTree object with a board state.
        The board state is represented in FEN (Forsyth-Edwards Notation) format.
        :param fen: A string representing the chess board in FEN format.
        """
        #white moves first and is maximizing player, black is the opposite
        
        self.rboard=chess.Board(fen)
        
        self.root=TreeNode(self.rboard,1) #1 or white turn, 0 for black turn

    @staticmethod
    def get_supported_evaluations():
        """
        Static method that returns a list of supported evaluation methods.
        :return: A list of strings containing supported evaluation methods.
        """
        pass

    def _apply_move(self, move, node, notation="SAN"):
        """
        Applies a chess move to a given game state (node).
        :param move: The move to be applied.
        :param node: The game state to which the move is applied.
        :param notation: The notation system used for the move (default: "SAN" - Standard Algebraic Notation).
        """
        if notation=="SAN":
            node._board.push_san(move)
        elif notation=="UCI":
            node._board.push_uci(move)
        return

    def _get_legal_moves(self, node, notation="SAN"):
        """
        Returns a list of all legal moves from the given game state (node).
        :param node: The game state from which to get legal moves.
        :param notation: The notation system used for the moves (default: "SAN").
        :return: A list of strings representing all legal moves for a given node.
        """
        moves=list(node._board.legal_moves)
        res=[]
        for i in moves:
            res.append(i.uci())
        return res

    def get_best_next_move(self, node, depth, notation="SAN"):
        """
        Determines the best next move for the current player using the Alpha-Beta pruning algorithm.
        :param node: The current game state.
        :param depth: The depth of the search tree to explore.
        :param notation: The notation system for the move (default: "SAN").
        :return: The best next move in the format defined by the variable notation.
        """
        best_move=""
        best_score= float("-inf")
        for move in self._get_legal_moves(node):
            self._apply_move(move, node,"UCI")
            score=self._alpha_beta(node, depth, float("-inf"), float('inf'), False)
            if score>best_score:
                best_score=score
                best_move=move
        return best_move

    def _alpha_beta(self, node, depth, alpha, beta, maximizing_player):
        """
        The Alpha-Beta pruning algorithm implementation. This method is used to evaluate game positions.
        :param node: The current node (game state).
        :param depth: The depth of the tree to explore.
        :param alpha: The alpha value for the Alpha-Beta pruning.
        :param beta: The beta value for the Alpha-Beta pruning.
        :param maximizing_player: Boolean indicating if the current player is maximizing or minimizing the score.
        :return: The best score for the current player.
        """
        if depth==0:
            return self._evaluate_position(node,0)

        node._score=self._evaluate_position(node,0)
        
        if maximizing_player: #white turn
            if node._board._is_checkmate() or node._board.is_stalemate() or node._board.is_insufficient_material():
                return self._evaluate_position(node,0)
            else:
                for i in self._get_legal_moves(node):
                    new_board=chess.Board(node._board.fen())
                    res=TreeNode(new_board,1-node._turn)
                    self._apply_move(i,res,"UCI")
                    node._children.append(res)




        else:  #black turn
            pass

    def _evaluate_position(self, node, depth):
        """
        Evaluates the position at a given node, taking into account the depth of the node in the decision tree.
        :param node: The game state to evaluate.
        :param depth: The depth of the node in the game tree.
        :return: An evaluation score for the position.
        """
        res=self._evaluate_board(node._board)
        return res-depth*2

    def _evaluate_board(self, board):
        """
        Evaluates a provided board and assigns a score.
        :param board: The board to evaluate.
        :return: An evaluation score for the board.
        """
        pieces={"wpawn":0, "wknight":0, "wbishop":0, "wrook":0, "wqueen":0, "wking":0,
                "bpawn":0, "bknight":0, "bbishop":0, "brook":0, "bqueen":0, "bking":0}
        fenstr=board.fen()
        for i in fenstr:
            if i==" ":
                break
            elif i.isalpha():
                if i=="P":
                    pieces["wpawn"]+=1
                elif i=="N":
                    pieces["wknight"]+=1
                elif i=="B":
                    pieces["wbishop"]+=1
                elif i=="R":
                    pieces["wrook"]+=1
                elif i=="Q":
                    pieces["wqueen"]+=1
                elif i=="K":
                    pieces["wking"]+=1

                if i=="p":
                    pieces["bpawn"]+=1
                elif i=="n":
                    pieces["bknight"]+=1
                elif i=="b":
                    pieces["bbishop"]+=1
                elif i=="r":
                    pieces["brook"]+=1
                elif i=="q":
                    pieces["bqueen"]+=1
                elif i=="k":
                    pieces["bking"]+=1
            
            res=pieces["wpawn"]+pieces["wknight"]*3+pieces["wbishop"]*3+pieces["wrook"]*5+pieces["wqueen"]*9+pieces["wking"]*39
            -pieces["bpawn"]-pieces["bknight"]*3-pieces["bbishop"]*3-pieces["brook"]*5-pieces["bqueen"]*9-pieces["bking"]*39
            return res

                                    


    def get_board_visualization(self, board):
        """
        Generates a visual representation of the board.
        :param board: The board to visualize.
        :return: A visual representation of the board.
        """
        

    def visualize_decision_process(self, depth, move, notation="SAN"):
        """
        Visualizes the decision-making process for a particular move up to a certain depth.
        :param depth: The depth of the analysis.
        :param move: The move being analyzed.
        :param notation: The notation system for the move (default: "SAN").
        """
        pass

    def export_analysis(self):
        """
        Exports the analysis performed by the AlphaBetaChessTree.
        """
        pass
