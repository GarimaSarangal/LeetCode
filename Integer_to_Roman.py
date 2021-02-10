class Solution:
    def intToRoman(self, num: int) -> str:
        # https://leetcode.com/problems/integer-to-roman/
        # https://www.youtube.com/watch?v=yzB4M-UXqgI&ab_channel=MichaelMuinos
        
        digits = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V")
                 ,(4,"IV"),(1,"I")]
        
        ans = []
        
        for val, sym in digits:
            if num == 0: break
            
            count = num//val #getting first number
            num = num%val # getting remaining
            
            # we can use divmod funciton of python here as well count, num = divmod(num, value)
            
            ans.append(sym * count) #multiplying the respective symbol by count times check video
            
        return "".join(ans)
        
        
        
#Time complexity : O(1)

#As there is a finite set of roman numerals, there is a hard upper limit on how many times the loop can iterate. This upper limit is 15 times, and it occurs for the number 3888, which has a representation of MMMDCCCLXXXVIII. Therefore, we say the time complexity is constant, i.e. O(1)O(1).

#Space complexity : O(1)

#The amount of memory used does not change with the size of the input integer, and is therefore constant.


            
            
    
       
