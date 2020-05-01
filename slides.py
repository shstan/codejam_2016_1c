import numpy as np
def build_slides(B, M):
    if M > 2**(B-2):
        return None
    adj_mat = np.zeros((B, B))
    M_ = M
    for i in range(1 ,B):
        # connect all the paths that are not connected to the source
        adj_mat[i, i+1:] = 1
    """
    1. no cycles, since that would create infinite number of paths
    Notice that when only manipulating the 1st row, the number of path corresponds to the binary rep. of the num.
    this is because between 1 - j - ... - B, the number of path we can take from j to B is
        2**(# of points in between which can be taken or not), thus if B=5 and j=3, 1-3-5 and 1-3-4-5 can be taken.
    thus, just put in bin rep in between 0th and last index, exclusively.
    """
    if M == 2**(B-2):
        adj_mat[0,1:]=1
        return adj_mat
    bin_arr = [int(x) for x in bin(M)[2:]]
    adj_mat[0, -len(bin_arr)-1:-1] = bin_arr
    return adj_mat


if __name__ == "__main__":
    T = int(input())
    for t in range(1, 1+T):
        B, M = [int(x) for x in input().split()]
        res = build_slides(B, M)
        pos = 'POSSIBLE' if res is not None else 'IMPOSSIBLE'
        print("Case #{}:".format(t), pos)
        if res is not None:
            for line in res:
                print(''.join([str(int(x)) for x in line]))