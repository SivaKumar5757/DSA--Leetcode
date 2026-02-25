class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=deque()
        for i,char in enumerate(s):
            if char==')' and stack and stack[-1][0]=='(':
                stack.pop()
            elif char=='(' or  char==')':
                stack.append((char,i))
        st=""
    
        for i,char in enumerate(s):
            if stack and stack[0][1]==i:
                stack.popleft()
            else:
                st+=char
        return st