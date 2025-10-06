class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
      dp, maxx = {}, 0
      for i in range(len(arr)):  
        if arr[i] - difference in dp: #look up in a dict is o(1)
            dp[arr[i]] = dp[arr[i] - difference] + 1
        else:
            dp[arr[i]] = 1

        maxx = max(maxx, dp[arr[i]])

      return maxx

      
