import numpy as np

INITIAL_STATE = [2, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 5, -5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, -2]


class Board:
    def __init__(self):
        self.state = INITIAL_STATE
        self.height = 12

    def __str__(self):
        arr = np.array([[" " for _ in range(12)] for i in range(12)])
        indices = [(0, 11-i) for i in range(12)] + [(self.height - 1, i) for i in range(12)]
        for i, (x, y) in enumerate(indices):
            num = self.state[i]
            if val := np.abs(num):
                char = "W" if num > 0 else "B"
                for j in range(val):
                    if i < 12:
                        arr[j, y] = char
                    else:
                        arr[x - j, y] = char
        return str(arr)


def main():
    board = Board()
    print(board)
    # [['W' ' ' ' ' ' ' 'B' ' ' 'B' ' ' ' ' ' ' ' ' 'W']
    #  ['W' ' ' ' ' ' ' 'B' ' ' 'B' ' ' ' ' ' ' ' ' 'W']
    #  ['W' ' ' ' ' ' ' 'B' ' ' 'B' ' ' ' ' ' ' ' ' ' ']
    #  ['W' ' ' ' ' ' ' ' ' ' ' 'B' ' ' ' ' ' ' ' ' ' ']
    #  ['W' ' ' ' ' ' ' ' ' ' ' 'B' ' ' ' ' ' ' ' ' ' ']
    #  [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
    #  [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
    #  ['B' ' ' ' ' ' ' ' ' ' ' 'W' ' ' ' ' ' ' ' ' ' ']
    #  ['B' ' ' ' ' ' ' ' ' ' ' 'W' ' ' ' ' ' ' ' ' ' ']
    #  ['B' ' ' ' ' ' ' 'W' ' ' 'W' ' ' ' ' ' ' ' ' ' ']
    #  ['B' ' ' ' ' ' ' 'W' ' ' 'W' ' ' ' ' ' ' ' ' 'B']
    #  ['B' ' ' ' ' ' ' 'W' ' ' 'W' ' ' ' ' ' ' ' ' 'B']]


if __name__ == "__main__":
    main()
