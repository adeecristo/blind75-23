from typing import List, Tuple


# ----------------------------------------------------------------- #


class Solution:
    """program holder """

    def spider(self, pos: Tuple[int, int], board: List[List[str]], walked: List[Tuple[int, int]], dir: str, word: str):
        """create a recursive spider"""
        if pos in walked:
            return False  # checks if already walked here

        (x, y) = pos
        if board[y][x] != word[0]:
            return False  # this field is not the correct next letter
        if len(word) == 1:
            return True  # this is the last letter of the word

        if pos[0] > 0 and dir != "right":
            if self.spider((pos[0] - 1, pos[1]), board, [*walked, pos], "left", word[1:]):
                return True
        if (pos[0]+1) < len(board[0]) and dir != "left":
            if self.spider((pos[0] + 1, pos[1]), board, [*walked, pos], "right", word[1:]):
                return True
        if pos[1] > 0 and dir != "down":
            if self.spider((pos[0], pos[1] - 1), board, [*walked, pos], "up", word[1:]):
                return True
        if (pos[1]+1) < len(board) and dir != "up":
            if self.spider((pos[0], pos[1] + 1), board, [*walked, pos], "down", word[1:]):
                return True

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        """checks if a board holds the word"""

        # check for possible starts where a possible end is within a valid distance
        possible_starts = []  # list of word[0] positions
        possible_ends = []   # list of word[-1] positions
        y = 0
        for row in board:
            x = 0
            for item in row:
                if item.upper() == word[0].upper():
                    possible_starts.append((x, y))
                if item.upper() == word[-1].upper():
                    possible_ends.append((x, y))
                x += 1
            y += 1

        # check for ends in valid range of starts
        word_len = len(word)
        valid_starts = []  # list of starts with 1+ end in valid range
        for start in possible_starts:
            for end in possible_ends:
                if word_len > 1 and start == end:
                    continue
                distance = abs(end[0] - start[0]) + abs(end[1] - start[1])
                if distance % 2 != word_len % 2:
                    valid_starts.append(start)
                    break

        # perform recursive search
        for lz in valid_starts:
            agent = self.spider(pos=lz, board=board,
                                walked=[], dir="spawn", word=word)
            if agent:
                return True

        return False


# ----------------------------------------------------------------- #
if __name__ == "__main__":
    newsolution = Solution()

    print(newsolution.exist(board=[["A", "B", "C", "E"], [
          "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
    print(newsolution.exist(board=[["A", "B", "C", "E"], [
          "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))
