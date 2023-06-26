import collections
from typing import Deque
import re

class Solution:
    # 내 풀이
    def isPalindrome(self, s: str) -> bool:
        # isalnum()으로 if문 조건 축약 가능
        s = "".join([i for i in s.lower() if 'a' <= i <= 'z' or '0' <= i <= '9'])
        
        # == 자체가 boolean 값을 반환하므로 삼항 연산자 불필요
        return True if s == s[::-1] else False

    # 리스트로 변환해 풀기
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # isalnum(): 영문자, 숫자 판별 함수
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True
    
    # 데크 자료형을 이용해 풀기
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
            
        return True
    
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]