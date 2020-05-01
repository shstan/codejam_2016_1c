import numpy as np
from itertools import product
def max_len_clothing(J, P, S, K):
    adj_mat = np.zeros((J, P, S))
    already_done = set()
    rtn = []
    for j, p, s in product(range(J), range(P), range(S)):
        if adj_mat[j, p, s] < K and (j, p, s) not in already_done:
            rtn.append((j, p, s))
            already_done.add((j, p, s))
            adj_mat[j, :, s] += 1
            adj_mat[:, p, s] += 1
            adj_mat[j, p, :] += 1
            adj_mat[j, p, s] -= 2
    return rtn

def max_len_clothing_2(J, P, S, K):
    """
    from official analysis:
    For instance, for an input of J = 1, P = 3, S = 3, K = 2, the following is a maximal set of outfits that is not maximum (the maximum size is 6): 1 1 1, 1 1 2, 1 2 2, 1 2 1, 1 3 3.

    So, if we just randomly choose outfits without violating the law, we are in danger of being trapped in a locally maximal set.

    Fortunately, there are several greedy approaches to achieve a set of size J × P × K outfits without angering the Fashion Police. As argued above, we know that J × P × K is the maximum possible size, so if we can find a set of that size, we are done!

    We cannot use a jacket-pants combination more than K times, so if we want to produce J × P × K outfits we are forced to use each combination exactly K times. To simplify the math, we use jacket, pants and shirt numbers between 0 and the appropriate total minus 1. We just need to remember to add 1 to every identifier when we print it to the output.

    Let us fix a combination with jacket number j and pants number p. Our proposal is assign to it shirts (j + p) % S, (j + p + 1) % S, ..., (j + p + K - 1) % S, where % stands for the modulo operation. Since S > K, these are all different, and by construction, the combination of jacket and pants is used exactly K times, as desired.

    What about jacket-shirt and pants-shirt combinations? Let us fix a jacket number j and a shirt number s. If the outfit (j, p, s) appears in the constructed set, then s = (j + p + d) % S for some d between 0 and K - 1, inclusive. Then, by modular arithmetic, and noticing that j % S = j, p % S = p, and s % S = s, it turns out that p = (s - j - d) % S. Then, each choice of d uniquely determines p, so there cannot be more ps to go with a given combination of j and s than choices of d, and there are K choices of d, which means the combination of j and s does not exceed the maximum.

    Since this is valid for any j and s, and a symmetrical proof is valid for each pants-shirt combination, we have proven that the proposed set of outfits does not break any of the rules of the Fashion Police.
    :param J:
    :param P:
    :param S:
    :param K:
    :return:
    """
    res = []
    for j, p, s in product(range(J), range(P), range(min(S, K))):
        res.append((j, p, (j + p + s) % S))
    return res



if __name__ == "__main__":
    T = int(input())
    for t in range(1, 1+T):
        J, P, S, K = [int(x) for x in input().split()]
        res = max_len_clothing_2(J, P, S, K)
        print("Case #{}:".format(t), len(res))
        for j, p, s in res:
            print(' '.join([str(j+1), str(p+1), str(s+1)]))
