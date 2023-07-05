from typing import List
from collections import defaultdict

class Solution:
    # 내 풀이
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for str in strs:
            key = ''.join(sorted(list(str)))
            if key in dic:
                dic[key].append(str)
            else:
                dic[key] = [str]
        
        return dic.values()
    
    # 정렬하여 딕셔너리에 추가
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # 정렬해 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()
    # defaultdict을 쓰면 if-else 문이 필요없어져서 간결하게 쓸 수 있음