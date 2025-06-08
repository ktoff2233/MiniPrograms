from typing import List


class Solution:
    def cars(self,inp):
        zeros = 0
        count = 0
        for i in inp:
            if i == 0:
                zeros += 1
            if i == 1:
                count += zeros
        return count

if __name__ == "__main__":
    solution = Solution()
    A = [0, 1, 0, 1, 1]
    print(solution.cars(A))  # Expected output: 5

    # Test case 2: No passing cars, all cars go east (0s)
    A = [0, 0, 0, 0]
    print(solution.cars(A))  # Expected output: 0

    # Test case 3: No passing cars, all cars go west (1s)
    A = [1, 1, 1, 1]
    print(solution.cars(A))  # Expected output: 0

    # Test case 4: All cars go in a pattern that causes maximum passing pairs
    A = [0, 1, 0, 1, 0, 1]
    print(solution.cars(A))  # Expected output: 9 (all cars pass)

    # Test case 5: Maximum number of passing cars without exceeding the limit
    A = [0] * 50000 + [1] * 50000
    print(solution.cars(A))  # Expected output: 2500000000 (but should be limited to 1000000000)

    # Test case 6: Passing cars are only a few in large array
    A = [0] + [1] * 99999
    print(solution.cars(A))