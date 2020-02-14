##https://leetcode.com/problems/shortest-way-to-form-string/
##Dynamic Programming, greedy
##like i get it now, i just don't know how you can ever reason through these types of problems...
##This might be how i would approach the problem
##https://leetcode.com/problems/shortest-way-to-form-string/discuss/463068/java-greedy-solution

##Thought process, you want to run through the different cases first, how do you get a count result of -1,1,2.... etc.
##No storing shit, you want to use two pointers and increment them in a way that makes sense
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ## The initial value of this is pretty perplexing, but you neeed a word counter, its initial value makes sense
        # When you go through the count result of 1 case
        word_ct = 1
        # Your two pointers, for each word
        src_ct, tar_ct = 0, 0

        # Iterate until you have gone through the entire target string
        while tar_ct < len(target):
            #Now the hardest part of this is understanding how to use the search function CORRECTLY
            #Keep in mind that it is sequential, so that means if part of the string is found, you must check the remainder of the string for the rest of the right answer
            #best practice would be to set a pos var = source.find(target[tar_ct], src_ct)
            #but aside from that, setting up the base case is useful because you do them in order of failure, success, and if failure then what
            #DO NOT BE AFRAID TO PSEUDO AT SOME POINT
            if (source.find(target[tar_ct], src_ct) == -1):
                #1 FIRST CASE SOLVED, what happens if there is no such string in the source that matches the target character, and you searched the whole source string
                if (src_ct == 0):
                    return -1
                else:
                #3 THIRD CASE SOLVED (Skipped initially), it's not intuitive to think to increment count yet, it is intuitive to reset src count to try again
                #after finishing the second case, you realize you cannnot increment the count there, you have to do it here because it implies
                #that you ran out of source space looking for the next target character in sequence (i.e. next char could be there, just out of sequence)
                #increase the word count (for your success, you still need to see if you can find the last remaining character)
                #when you succeed ON THE LAST CASE, you actually overrun the target count due to success (see last case)
                    src_ct = 0
                    word_ct += 1
            else:
                #2 SECOND CASE SOLVED, you find the location of the next character, increment FROM THAT LOCATION by 1
                # increment from location because it implies everything prior to that position you already found for, or it didn't contain the right char
                #successfully found a character, increment the target count by one
                src_ct = source.find(target[tar_ct], src_ct) + 1
                tar_ct += 1

        return word_ct

d = Solution().shortestWay
print(d("xyz","xyz"))
