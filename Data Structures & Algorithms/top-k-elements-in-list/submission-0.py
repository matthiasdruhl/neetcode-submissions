class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #buckets
        check = {}

        freq = [[] for i in range(len(nums) + 1)]
        
        ans = []

        for num in nums:
            check[num] = 1 + check.get(num, 0)

        for num, count in check.items():
            freq[count].append(num)
        
        for arr in reversed(freq):
            for num in arr:
                ans.append(num)
                if len(ans) == k:
                    return ans



        


            
        

        
        
            



        