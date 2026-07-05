class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = 1 + counts.get(nums[i], 0)

        arr = []
        for num, count in counts.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res
        


        


            
            

