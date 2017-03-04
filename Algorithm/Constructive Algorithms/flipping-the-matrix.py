#!/usr/bin/env python


class Matrix:
    matrix = list()

    def __init__(self, args):
        self.matrix = args

    def get_matrix(self):
        return self.matrix

    def cornermax(self, row, col):
        idx1 = len(self.matrix[row]) - 1 - col
        idx2 = len(self.matrix[row]) - 1 - row
        return max(self.matrix[row][col], self.matrix[row][idx1], self.matrix[idx2][col], self.matrix[idx2][idx1])

queries = int(raw_input().strip())
total = []
for i in xrange(queries):
    matrx = []
    n = input()
    for j in xrange(2 * n):
        matrx.append(map(int, raw_input().split()))
    myMatrix = Matrix(matrx)
    gen = list()
    for row in xrange(n):
        for col in xrange(n):
            gen.append(myMatrix.cornermax(row, col))
    total.append(sum(gen))
print "\n".join(map(str, total))
