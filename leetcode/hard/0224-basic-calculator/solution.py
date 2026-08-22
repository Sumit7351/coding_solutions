import re
class Solution:
    def eval(self,a,b,op):
        match op:
            case "+":
                return a+b
            case "-":
                return a-b

    def convert_postfix(self,s):
        stack=[]
        output=[]
        i=0
        prev=None
        while(i<len(s)):
            if s[i]=="(":
                stack.append("(")
                prev="("

            elif s[i].isdigit():
                num=""
                while(i<len(s) and s[i].isdigit()):
                    num+=s[i]
                    i+=1
                output.append(num)
                prev="num"
                continue
            
            elif s[i] in "+-":
                if(s[i]=="-" and (prev==None or prev=="(" or prev=="op")):
                    output.append("0")
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                stack.append(s[i])
                prev="op"

            elif s[i]==")":
                while(stack and stack[-1]!="("):
                    output.append(stack.pop())
                stack.pop()
            i+=1
        while stack:
            output.append(stack.pop())
        
        return output

    def calculate(self, s: str) -> int:
        new=self.convert_postfix(s)
        stack=[]
        ans=0
        for ch in new:
            if ch.isdigit():
                stack.append(int(ch))
            elif ch in "+-":
                val1=stack.pop()
                val2=stack.pop()

                ans=self.eval(val2,val1,ch)
                stack.append(ans)

        return int(stack[-1])
        