from _collections import *
# from typing import List
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ##YMU, you almost forgot that in order for this to work sequentially, the array must be SORTED FIRST by length
        words.sort(key=len)
        ##dictionary/hash map for various entries
        dict_word = defaultdict(int)
        cur_max = 0

        for word in words:
            ##YMU, didn't make this into a range
            for c in range(len(word)):
                ##This chunk includes all of the letters except for the character you're trying to omit
                ##This is meant to represent the word -1 letter, searching for maatching predecessor
                ##YMU, you put the second chunk incorrectly
                chunk = word[:c] + word[c+1:]
                ##the new "word" can potentially be the new final max (it's +1 letter more)
                ##but the chunk represents the predecessor
                ##so you take the max of chunk+1/word
                ##YMU, you assigned everything back to the array, and NOT THE DICTIONARY
                dict_word[word] = max(dict_word[chunk] + 1,dict_word[word])
            ##override the current max because it should be the running total of all previous max
            ##see kadane's algorithm https://www.youtube.com/watch?v=86CQq3pKSUw
            cur_max = max(cur_max,dict_word[word])

        return cur_max




d = Solution().longestStrChain
print(d(["ab","ba","aba","baa","baca","bacda"]))
