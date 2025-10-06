class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
      dp, maxx = {}, 0
      for i in range(len(arr)):
        if arr[i] - difference in dp:
            dp[arr[i]] = dp[arr[i] - difference] + 1
        else:
            dp[arr[i]] = 1
        maxx = max(maxx, dp[arr[i]]) #there may be multiple subsequences that fulfill the condition so this helps to take the longest one.(a new subsequnce can start from any index)

      return maxx


      
