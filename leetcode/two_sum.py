class Solution: # nums가 정렬상태라는 가정 하에 가능
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
                # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
                if nums[left] + nums[right] < target:
                    left += 1
                # 합이 타겟보다 크면 왼쪽 포인터를 왼쪽으로
                elif nums[left] + nums[right] < target:
                    right -= 1
                else:
                    return [left, right]
