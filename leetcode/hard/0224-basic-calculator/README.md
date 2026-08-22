# Basic Calculator

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return  *the result of the evaluation*.

 **Note:**  You are  **not**  allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

 

 **Example 1:** 

```
Input: s = "1 + 1"
Output: 2

```

 **Example 2:** 

```
Input: s = " 2-1 + 2 "
Output: 3

```

 **Example 3:** 

```
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

```

 

 **Constraints:** 

- 1 <= s.length <= 3 * 105
- s consists of digits, '+', '-', '(', ')', and ' '.
- s represents a valid expression.
- '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
- '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

## Solution

**Language:** Python  
**Runtime:** 119 ms (beats 5.09%)  
**Memory:** 23.9 MB (beats 5.17%)  
**Submitted:** 2026-08-22T11:08:44.739Z  

```py
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
        
```

---

[View on LeetCode](https://leetcode.com/problems/basic-calculator/)