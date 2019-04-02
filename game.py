import string
import random

class Game:

    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        l = self.grid.copy() # Consume letters from the grid
        for l in word:
            if l in ls:
                ls.remove(l)
            else:
                return False
        return True
