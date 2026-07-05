class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #build a hashmap of all of the values and their corresponding pairs and check if the counterpart is in the hashmap

        nums_map = {}
        for i in range(len(nums)):
            nums_map[nums[i]] = i
            
        for i in range(len(nums)):
            counterpart = target - nums[i]
        
            if counterpart not in nums_map:
                continue
            
            if nums_map[counterpart] == i:
                continue
            
            return [min(i, nums_map[counterpart]), max(i, nums_map[counterpart])]
