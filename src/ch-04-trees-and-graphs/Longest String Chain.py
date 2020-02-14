##https://leetcode.com/problems/longest-string-chain/

##Given a list of words, each word consists of English lowercase letters.

##Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

##A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

##Return the longest possible length of a word chain with words chosen from the given list of words.

##right off the bat, you have to be aware of parts of the question that make it easier
##i.e EXACTLY one letter anywhere in word1

##https://leetcode.com/problems/longest-string-chain/discuss/506861/Python-or-Time-5-Space-100-using-Kadane's
##https://www.youtube.com/watch?v=86CQq3pKSUw


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
