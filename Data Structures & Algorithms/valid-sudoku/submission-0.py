"""
INTERVIEW ROUTINE

1. UNDERSTAND
   - Restate in own words. Input/output types? Constraints? Edge cases?

    - input is a 2d array 9*9 matrix (board) of elements of nums 1-9 or .
    - output is true/false


2. DRY RUN EXAMPLE
   - Trace given example by hand. Make one edge case.

3. PATTERN
   - Count something? → Counter/hashmap
   - Fast lookup? → hashset/hashmap
   - Need order? → sort/heap
   - Sorted input? → binary search/two pointers
   - Running window? → sliding window
   - Explore paths? → BFS/DFS

   Each row, each col, each 3x3 MUST:
    1. add up to 45 (cant => doesnt need to be filled)
    2. have unique numbers ->
            hashmap

            

4. APPROACH + COMPLEXITY (before coding)
   - "I'll use X because Y"
   - Brute force first, then optimize
   - Rough T(n) and space guess

5. PSEUDOCODE
   # step 1
   # step 2
   # step 3

6. CODE IT
   - Talk through each line. Good variable names. Flag edge cases.

7. DRY RUN YOUR CODE
   - Trace actual code with real values. Don't just eyeball it.

8. COMPLEXITY (confirm)
   - Time: dominant operation?
   - Space: extra structures created?

    Input: board =
   [["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]

"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_seen = collections.defaultdict(set)
        col_seen = collections.defaultdict(set)
        box_seen = collections.defaultdict(set)

        for row in range(9):

            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                if board[row][col] in row_seen[row] or board[row][col] in col_seen[col]  or board[row][col] in box_seen[(row//3, col//3)]:
                    return False

                row_seen[row].add(board[row][col])
                col_seen[col].add(board[row][col])
                box_seen[(row//3, col//3)].add(board[row][col])

        return True
                










             