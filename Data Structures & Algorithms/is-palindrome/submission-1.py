class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for char in s:
            if (ord(char) >= 65 and ord(char) <= 90) or (97 <= ord(char) and ord(char) <= 122) or (ord(char) >= 48 and ord(char) <= 57 ):
                st+=char
        return st.lower() == st[::-1].lower()
        