class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in nums:
            hashmap[i] += 1

        maxHeap = []

        for num, count in hashmap.items():
            maxHeap.append((count, num))

        heapq.heapify_max(maxHeap)

        result = []

        for i in range(k):
            count, num = heapq.heappop_max(maxHeap)
            result.append(num)

        return result