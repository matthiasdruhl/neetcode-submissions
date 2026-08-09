class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        a = Counter(tasks)

        high = 0
        amount = 0

        for key, item in a.items():
            if item > high:
                amount = 1
                high = item
            elif item == high:
                amount += 1
            
        return max(len(tasks), ((high - 1) * (n + 1)) + amount)
                