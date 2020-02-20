##Welcome to your holy grail
##https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb
from _collections import *
import operator
# from typing import List
from typing import List


class Solution:
    def longestStrChain(self, source: str):

        input = source.split(",")
        count = defaultdict(int)

        for word in input:
                count[word] += 1
        ##YMU by not knowing that you can sort via a parameter, remember to use lambda
        ##also remember reverse option
        ##Also count.items() lists it essentially
        a = sorted(count.items(), key=lambda x: x[1], reverse=True)
        print(a)




d = Solution().longestStrChain
print(d("pay,1on1,bp development,squads,process,om,celebration,holidays, team communication,building,building,development,benefits,education"))
