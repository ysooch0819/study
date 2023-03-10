class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = []
        if x < 0:
            res.append('-')
        s = list(str(abs(x)))
        for i in range(len(s)):
            res.append(s.pop())

        if -2**31 <= int(''.join(res)) <= 2**31-1:
            return int(''.join(res))
        else: return 0