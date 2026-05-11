from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_map = defaultdict(int)
        heap = []

        for i in nums:
            num_map[i] += 1
        print(num_map)

        for key, value in num_map.items():
            heapq.heappush(heap, (value, key))
        
            if (len(heap) > k):
                heapq.heappop(heap)

        result = []

        for value, key in heap:
            result.append(key)

        return result

        #boom