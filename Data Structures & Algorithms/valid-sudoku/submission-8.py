class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        master_set = set([])
        master_n = 0
        if self.sudoku_final(master_n,master_set,board) is False:
            return False
        for i, value in enumerate(board):
            a = set(value[0:3])
            b = set(value[3:6])
            c = set(value[6:9])

            x = a.intersection(b)
            y = a.intersection(c)
            z = b.intersection(c)

            if x != set():
                if x != {"."}:
                    return False

            if y != set():
                if y != {"."}:
                    print("2")
                    return False

            if z != set():
                if z != {"."}:
                    return False

            y_axis = [board[0][i] ,board[1][i],board[2][i],board[3][i],board[4][i],board[5][i],board[6][i],board[7][i],board[8][i]]
            e = set(y_axis[0:3])
            f = set(y_axis[3:6])
            g = set(y_axis[6:9])

            x_ = e.intersection(f)
            y_ = e.intersection(g)
            z_ = f.intersection(g)

            if x_ != set():
                if x_ != {"."}:
                    return False

            if y_ != set():
                if y_ != {"."}:
                    return False

            if z_ != set():
                if z_ != {"."}:
                    return False
        return True

    
    def sudoku_set(self,board_num, mn,board,master_set):
        x = [board[mn][board_num], board[mn + 1][board_num], board[mn + 2][board_num]]
        for i in x:
            bool_ = self.master_check(i, master_set)
            if bool_ is False:
                return False

                


    def master_check(self,n,master):
        if n in master:
            return False
        else:
            if n != ".":
                master.add(n)


    def sudoku_final(self,master_n, master_set,board):
        while master_n != 9:
            for i in range(0, len(board)):
                if self.sudoku_set(i, master_n,board,master_set) is False:
                    return False
                if (i + 1) % 3 == 0:
                    master_set.clear()
            master_n += 3



            

