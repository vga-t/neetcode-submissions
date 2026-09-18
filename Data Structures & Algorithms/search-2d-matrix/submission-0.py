class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left+right)//2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                left, right = 0, len(matrix[0])-1
                while left <= right:
                    inner_mid = (left + right)//2
                    if matrix[mid][inner_mid] == target:
                        return True
                    elif matrix[mid][inner_mid]<target:
                        left = inner_mid + 1
                    else:
                        right = inner_mid - 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

            