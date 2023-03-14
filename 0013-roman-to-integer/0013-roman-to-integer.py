class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_set = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        li = list(s)
        res = 0
        i = 0
        while i < len(li):
            if li[i] == 'I':
                if len(li[i:]) >1 and li[i+1] == 'I': 
                    if len(li[i:]) >2 and li[i+2] == 'I': 
                        res+=3
                        i+=3
                    else: 
                        res+=2
                        i+=2
                elif len(li[i:]) >1 and li[i+1] == 'V': 
                    res += 4
                    i+=2
                elif len(li[i:]) >1 and li[i+1] == 'X': 
                    res += 9
                    i +=2
                else:
                    res +=1
                    i +=1
            elif li[i] == 'X':
                if len(li[i:]) > 1 and li[i+1] == 'L': 
                    res += 40
                    i+=2
                elif len(li[i:]) > 1 and li[i+1] == 'C': 
                    res += 90
                    i +=2
                else: 
                    res+= 10
                    i +=1
            elif li[i] == 'C':
                if len(li[i:]) > 1 and li[i+1] == 'D': 
                    res += 400
                    i+=2
                elif len(li[i:]) > 1 and li[i+1] == 'M': 
                    res += 900
                    i +=2
                else:
                    res+=100
                    i+=1
            else:
                res += roman_set[li[i]]
                i +=1

        return res