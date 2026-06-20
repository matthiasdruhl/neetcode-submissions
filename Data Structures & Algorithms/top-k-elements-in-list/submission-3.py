class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort into buckets with n elements
        count = {}
        high = 1
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] = count[num] + 1
                high = max(high, count[num])

        buckets = [[] for i in range(high + 1)]

        

        for num, freq in count.items():
            buckets[freq].append(num)
            print(buckets)
       
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res



        

        


        