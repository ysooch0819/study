class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        li = list(s)
        if len(li) %2 == 1: return False
        
        stack = []
        for s in li:
            if s == '[' or s=='(' or s=='{': stack.append(s)
            elif len(stack) == 0: return False
            else:
                if (s==']' and stack[-1] == '[') or (s==')' and stack[-1] == '(') or (s=='}' and stack[-1] == '{'): stack.pop()
                else: return False
        if len(stack) != 0: return False
        return True