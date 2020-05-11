
INFINITY = 9999

class AI:
    def __init__(self):
        pass

    def minimax(self, depth, board, white_turn, alpha, beta):
        if white_turn:
            best = [None, +INFINITY]
        else:
            best = [None, -INFINITY]

        if not depth:
            score = board.evaluate_board()
            return [None, score]
        
        moves = board.board.legal_moves
        for move in moves:
            board.board.push(move)
            value = self.minimax(depth-1, board, not white_turn, alpha, beta)
            board.board.pop()

            if white_turn:
                if value[1] < best[1]:
                    value[0] = move
                    best = value
                beta = min(beta, value[1])
                if beta <= alpha:
                    break
            if not white_turn:
                if value[1] > best[1]:
                    value[0] = move
                    best = value
                alpha = max(alpha, value[1])
                if beta <= alpha:
                    break
        return best