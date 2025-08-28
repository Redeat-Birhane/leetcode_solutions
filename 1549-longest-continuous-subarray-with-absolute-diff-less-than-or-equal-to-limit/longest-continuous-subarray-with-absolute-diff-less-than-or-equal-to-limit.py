class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing_deque = deque()
        decreasing_deque = deque()
        left = 0
        max_length = 0
        for i in range(len(nums)):
            while increasing_deque and nums[i] < increasing_deque[-1]:
                increasing_deque.pop()
            while decreasing_deque and nums[i] > decreasing_deque[-1]:
                decreasing_deque.pop()
            increasing_deque.append(nums[i])
            decreasing_deque.append(nums[i])
            while decreasing_deque and increasing_deque and decreasing_deque[0] - increasing_deque[0] > limit:
                if nums[left] == increasing_deque[0]:
                    increasing_deque.popleft()
                if nums[left] == decreasing_deque[0]:
                    decreasing_deque.popleft()
                left +=1
            max_length = max(max_length, i - left + 1)
        return max_length
            
                



            
    

        
        