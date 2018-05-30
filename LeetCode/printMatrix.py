class Printer:
    def printMatrix(self, mat, n, m):

        res = []
        flag = False
        for x in mat:
            if flag == False:
                res.extend(x)
                flag = True
            else:
                res.extend(x[::-1])
                flag = False
        return res


if __name__ == "__main__":
    a = Printer()
    print(a.printMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], 4, 3))