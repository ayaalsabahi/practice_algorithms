class Solution(object):
    def reverseString(self, s):
         for i in range(len(s)):
                temp = s[i]
                s[i]= s[len(s) - 1 - i]
                s[len(s) - 1 - i] = temp
                
                if len(s)%2==1:
                    if i == len(s)/2:
                        break
                else:
                     if i == len(s)/2-1:
                        break
        