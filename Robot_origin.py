
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Description:
            There is a robot starting at the position (0, 0), the origin, on a 2D plane. 
            Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

             Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
             
             Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right 
                once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is
                the same for each move.

        Inputs: 
        moves : string, it represents the move sequence of the robot where moves[i] represents
            its ith move.

        Outpout:
        True if robot returns to origin after it finishes all of its moves
        False otherwise
        
        """
        x = 0
        y = 0
        assert 1 <= len(moves) <= 2 * 104, "The length of the moves sequence must be from 1 to 208."
        for move in moves:
            assert move in ['R', 'L', 'U', 'D'], f"Moves can only contains the characters 'U', 'D', 'L' and 'R' not {move}."
            if move == 'R':
                x += 1
            if move == 'L':
                x -= 1
            if move == 'U':
                y += 1
            if move == 'D':
                y -= 1
        
        if x == 0 and y == 0:
            return True
        return False