class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        true_list = [False] * 3
        for triplet in triplets:
            if (triplet[0] > target[0] or 
            triplet[1] > target[1] or
            triplet[2] > target[2]):
                continue
            for i in range(len(triplet)):
                if triplet[i] == target[i]:
                    true_list[i] = True
        return all(true_list)