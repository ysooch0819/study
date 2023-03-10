class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        li = list(str(x))
        for i in range(0, len(li)//2):
            if li[i] != li[len(li)-i-1]:
                return False
            else:
                continue
        return True