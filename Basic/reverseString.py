from typing import List
class Solution(object):

    def bruteForce(self, s: List[str]) -> None:
        for i in range(int(len(s)/2)) :
            temp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = temp

        print(s)

    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)-1):
            n = s.pop()
            s.insert(i,n)
        print(s)


temp = Solution()
temp.reverseString(["h", "e", "l", "l", "o"])
temp.bruteForce(["h", "e", "l", "l", "o"])
