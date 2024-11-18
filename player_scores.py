"""
A group of friends is playing a video game, where each player earns points. At the end of a round, players who achieve
at least rank k can "level up" their characters. Given the scores of players at the end of the round, determine
how many players will level up.
Notes:
Players with equal scores share the same rank, and the next player with a lower score takes the subsequent rank
position. For instance, if four players finish with scores that rank them as 1, 1, 1, and 4, then the first three
players tie for first place, and the next player is ranked fourth.
No player with a score of 0 can level up, regardless of rank.

Example

n = 4

k = 3

scores = [100, 50, 50, 25]

These players' ranks are [1, 2, 2, 4]. Because the players need to have a rank of at least k = 3 to level up,
only the first three players qualify. Therefore, the answer is 3.
"""

import numpy as np
def rank_up(k, n, scores):
    if n != len(scores):
        print("not valid scores list")
        return False

    ranks = scores_to_rank(scores)
    ans = 0
    for i in ranks:
        if i <= k:
            ans += 1
    return ans

def scores_to_rank(sc):

    ranks = np.array(sc)
    #score_array = np.array(sc)
    sc.sort(reverse=True)

    for i, el in enumerate(sc):
        if sc.count(el) > 1:
            counts = np.where(ranks == el)
            for r in counts:
                ranks[r] = i+1
                #print(ranks)
        else:
            ranks[i] = i+1
            #print(ranks)

    return ranks


print(rank_up(k=3,n=4,scores=[100, 50, 50, 25]))