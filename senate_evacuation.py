import numpy as np

def get_chr(n):
    return chr(ord('A') + n)

def evac_plan(P):
    res = []
    P = np.array(P)
    while np.any(P>0):
        if np.count_nonzero(P) == 2:
            a, b = np.where(P > 0)[0]
            while np.any(P>0):
                res.append(get_chr(a)+get_chr(b))
                P[a] -= 1
                P[b] -= 1
            break
        most_ind = np.argmax(P)
        P[most_ind] -= 1
        res.append(get_chr(most_ind))
    return res



if __name__ == "__main__":
    T = int(input())
    for t in range(1, 1+T):
        N = int(input())
        P = [int(x) for x in input().split()]
        res_ = evac_plan(P)
        print("Case #{}:".format(t), " ".join(res_))