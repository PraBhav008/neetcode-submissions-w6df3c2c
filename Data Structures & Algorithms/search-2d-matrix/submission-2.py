class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if target > arr[-1]:
                continue
            else:
                low = 0
                high = len(arr) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if arr[mid] == target:
                        return True
                    elif arr[mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1

        return False