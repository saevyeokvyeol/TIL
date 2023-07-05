from typing import List
import collections
import re

class Solution:
    # 초기 풀이: 기호와 알파벳이 공백 없이 나열될 경우 오답
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = ''.join(s for s in paragraph.lower() if s.isalpha() or s.isspace())
        words = [s for s in paragraph.split() if s not in banned]
        return collections.Counter(words).most_common(1)[0][0]
    
    # 리스트 컴프리헨션, Counter 객체 사용
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        return max(counts, key=counts.get)

    # 수정 풀이
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = ''.join(s for s in paragraph.lower() if s.isalpha() or s.isspace())
        words = [s for s in paragraph.split() if s not in banned]
        return collections.Counter(words).most_common(1)[0][0]