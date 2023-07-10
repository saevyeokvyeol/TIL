from typing import List

class Solution:
    # 내 풀이
    def trap(self, height: List[int]) -> int:
        water = 0
        max_left, max_right = height[0], height[-1]
        left, right = 0, len(height) - 1

        while left < right:
            if max_left < max_right:
                left += 1
                if max_left < height[left]:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
            else:
                right -= 1
                if max_right < height[right]:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
        return water
    # 투 포인터 응용해서 풀긴 했는데 if-else 부분이 마음에 안 듦
    # 더 줄이고 싶다.

    # 투 포인터를 최대로 이용
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            # 더 높은 쪽으로 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right += 1
        
        return volume
    
    # 스택 쌓기
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼내기
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            
            stack.append(i)
        return volume