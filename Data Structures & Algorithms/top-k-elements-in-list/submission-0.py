class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for i in range(len(nums)+1)]
        for num in nums:
            if num in count:
                count[num] +=1
                continue
            count[num] = 1
        for num, freq in count.items():
            buckets[freq].append(num)
        res = []
        for i in range(len(nums), -1, -1):
            while buckets[i] and k>0:
                res.append(buckets[i][-1])
                buckets[i].pop()
                k-=1
        return res

