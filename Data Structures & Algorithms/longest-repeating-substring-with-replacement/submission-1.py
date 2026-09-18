class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r= 0,0
        freq={}
        res = 0

        while(r < len(s)):
            c = s[r]
            freq[c] = freq.get(c, 0) + 1

            maxV = max(freq.values())
            print((r - l+1) - maxV > k)
            if (r - l+1) - maxV > k:
                freq[s[l]]-=1
                l+=1
            
            res = max(res,r-l+1)
            
            r=r+1
        
        return res





        