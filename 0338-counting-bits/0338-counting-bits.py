class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        tmp = [i for i in range(0, n+1)]
        for i in range(0, n+1):
            t = tmp[i]
            cnt = 0
            while t != 0:
                t &= (t-1)
                cnt+=1
            tmp[i] = cnt

        return tmp