class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sorting
            # nlogn * mlogm to sort
        # hashmap and sort each word
            
        from collections import defaultdict

        check = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            check[tuple(sorted_word)].append(word)
        return list(check.values())

        
            
        