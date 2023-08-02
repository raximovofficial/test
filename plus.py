s = []
def getDegree(n: str):
    def nDegree(i: str):
        nonlocal n
        if len(n)>len(i):
            return sorted(n)
        #     for x in n:
        #         return s.append(x)
        #     # return s.append(n)
        
        else:
            # for z in i:
            #     return z
            return sorted(i)
    return nDegree

a = getDegree("HEllloass")
print(a("nasa"))
# print(s)