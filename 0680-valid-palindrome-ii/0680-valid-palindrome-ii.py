class Solution(object):
    def validPalindrome(self, s):
        
        def isPalidrome(left , right):
            while left < right:
                if s[left] != s[right]:
                    return False


                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                return(
                    isPalidrome(left + 1 , right)
                    or 
                    isPalidrome(left , right - 1)
                )



        return True
