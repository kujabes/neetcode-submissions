class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board

        # check each row
        for row in range(len(board)):
            if not self.isValidRow(row):
                return False
        
        # validate each column
        for col in range(len(board[0])):
            if not self.isValidCol(col):
                return False

        # construct sub_boxes
        box_range = [(0, 3), (3, 6), (6, 9)]
        sub_boxes = []
        for row_range in box_range:
            for col_range in box_range:
                sub_box = [row_range, col_range]
                if not self.isValidSubBox(sub_box):
                    return False

        return True
        
        

    def isValidRow(self, row: int) -> bool:
        seen = set()
        for num in self.board[row]:
            if not self.isValidNum(num, seen):
                return False

        return True
    
    def isValidCol(self, col: int) -> bool:
        seen = set()
        for i in range(len(self.board)):
            num = self.board[i][col]
            if not self.isValidNum(num, seen):
                return False

        return True

    def isValidSubBox(self, box: list[tuple, tuple]) -> bool:
        seen = set()
        row_range = box[0]
        col_range = box[1]
        for row in range(*row_range):
            for col in range(*col_range):
                num = self.board[row][col]
                if not self.isValidNum(num, seen):
                    return False
        
        return True

    def isValidNum(self, num: str, seen: set):
        if num == '.':
            return True
        elif num not in seen:
            seen.add(num)
            return True
        else:
            return False




