class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #two pointer

        #if not alnum, move leftright and continue
        #if both alnum and both match move pointers
        #else return false

        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        
        return True

        #O(n)
