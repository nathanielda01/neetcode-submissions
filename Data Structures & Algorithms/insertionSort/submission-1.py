# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return []
        if len(pairs) == 1:
            return [list(pairs)]
            
        output = [list(pairs)]

        i = 1
        while i < len(pairs):
            j = i
            while j > 0 and pairs[j - 1].key > pairs[j].key:
                pairs[j - 1], pairs[j] = pairs[j], pairs[j - 1]
                j -= 1
            output.append(list(pairs))
            i += 1
        return output
        
        