from typing import List

class Solution:
    # 내 풀이
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-1 - i] = s[-1 - i], s[i]

    # 투 포인터
    # 변수 선언해서 사용하니 훨씬 가독성이 좋아진다
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    # 파이써닉한 방식
    # s = s[::-1]가 안 먹히길래 이것도 안 먹힐 줄 알았는데 이건 된다...
    def reverseString(self, s: List[str]) -> None:
        s.reverse()