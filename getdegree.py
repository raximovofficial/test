def getDegree(n: int):
    def nDegree(i: int):
        nonlocal n
        return n ** i
    return nDegree

a = getDegree(2)
for i in range(10):
    print(a(i))
