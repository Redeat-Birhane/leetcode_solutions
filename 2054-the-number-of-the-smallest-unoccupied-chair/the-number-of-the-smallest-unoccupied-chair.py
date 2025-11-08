class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        target_arrival = times[targetFriend][0]
        friends = sorted(enumerate(times), key=lambda x: x[1][0])
        
        available = []
        occupied = []  
        next_chair = 0

        for friend_index, (arr, leave) in friends:
            while occupied and occupied[0][0] <= arr:
                leave_time, chair = heapq.heappop(occupied)
                heapq.heappush(available, chair)

            if available:
                chair = heapq.heappop(available)
            else:
                chair = next_chair
                next_chair += 1

            heapq.heappush(occupied, (leave, chair))

            if friend_index == targetFriend:
                return chair
