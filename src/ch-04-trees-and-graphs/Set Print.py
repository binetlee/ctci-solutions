##Welcome to your holy grail
##https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb
from _collections import *
import operator
# from typing import List
from typing import List


class Solution:
    def longestStrChain(self, input: List[str]):

        feed = defaultdict(int)

        for word in input:
                feed[word] += 1
        a = sorted(feed.items(), key=lambda x: x[1], reverse=True)
        print(a)




d = Solution().longestStrChain
print(d(["pay","development","squads","daily process","education","celebration","vacation","cross team","building","wfh","wfh","benefits","benefits","education","leadership communication", "development"]))
