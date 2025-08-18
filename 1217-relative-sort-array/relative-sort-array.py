class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3, result = [], []
        for num in arr1:
            if num not in arr2:
                arr3.append(num)
        arr3.sort()

        for i in range(len(arr2)):
            curr = [num for num in arr1 if num == arr2[i]]
            result += curr
        result += arr3
        return result

    

            


        