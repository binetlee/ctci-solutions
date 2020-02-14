##https://leetcode.com/problems/shortest-way-to-form-string/
##O(m*n), worst case is the last string is definitely the one you need
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ##for your target, understand you need the count, two pointers, count min 1 for the initial total pass
        cnt = 1
        src_ct, tar_ct = 0, 0

        while tar_ct < len(target):
            ##it might not hurt to actually check to see if you can set extra variables
            ##this is the indicator of whether or not the source string contains the target char
            ##if the target char does not exist, then it cannot work
            ##this checks the target for the target character, but it also is modified by the count of the src_ct
            pos = source.find(target[tar_ct], src_ct)
            if pos == -1:
                if src_ct == 0:
                    return -1
                else:
                    ##if it has failed to this point, it means that either src_ct > len(source)
                    ##or you've exhausted the number of matching letters in this sequential pattern
                    ##either way, it's been a success
                    ##you have to reset the source pointer to 0
                    src_ct = 0
                    ##and increment count
                    cnt += 1
            else:
                ##character found, increment target
                ##the source has to change to increment to the last point that the it was found in the source
                tar_ct += 1
                src_ct = pos + 1
        ##YMU by tabbing count wrong
        return cnt


d = Solution().shortestWay
print(d("xyz","xyz"))


