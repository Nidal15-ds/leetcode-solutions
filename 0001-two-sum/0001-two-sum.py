class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Première boucle : parcourt chaque élément de la liste
        for i in range(len(nums)):
            # Deuxième boucle : parcourt les éléments suivants
            for j in range(i + 1, len(nums)):
                # Si la somme des deux nombres est égale à la cible
                if nums[i] + nums[j] == target:
                    return [i, j]
