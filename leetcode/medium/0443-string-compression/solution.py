class Solution:
    def compress(self, chars: List[str]) -> int:
        l=0
        r=0
        k=0

        while r<len(chars):
            count=0
            char=chars[l]
            while(r<len(chars) and chars[l]==chars[r]):
                count+=1
                r+=1
            
            chars[k]=char
            k+=1
            if(count>1):
                for digit in str(count):
                    chars[k]=digit
                    k+=1
            l=r
        return k