class Solution:
    def firstUniqChar(self, s:str) -> int:
        hashMap = {}
        n = len(s)

        for character in s:
            hashMap[character] = hashMap.get(character, 0) + 1
        
        for i in range(n):
            if hashMap[s[i]] == 1:
                return i

        return -1