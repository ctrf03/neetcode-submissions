class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        maxHeap = []

        for n, c in count.items():
            maxHeap.append((c, n))

        heapq.heapify_max(maxHeap)

        res = []

        for i in range(k):
            c, n = heapq.heappop_max(maxHeap)
            res.append(n)

        return res