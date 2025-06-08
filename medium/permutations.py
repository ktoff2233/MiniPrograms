class Solution:
    def permute(self, arr):
        def backtrack(start, end):
            if start == end:
                result.append(arr[:])  # Make a copy of the current permutation
            else:
                for i in range(start, end):
                    # Swap the current element with the start
                    arr[start], arr[i] = arr[i], arr[start]

                    # Recur to generate all permutations with the new first element
                    backtrack(start + 1, end)

                    # Backtrack (undo the swap)
                    arr[start], arr[i] = arr[i], arr[start]

        result = []
        backtrack(0, len(arr))
        return result

# Example usag


if __name__ == "__main__":
    solution = Solution()
    result = solution.permute([1,2,3,4])
    for perm in result:
        print(perm)