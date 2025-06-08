def min_num_solution(n):
    if n == 0:
        return 0
    bin_N = bin(n)[2:]
    j = 0
    max_zero = 0
    for i in range(len(bin_N)):
        if bin_N[i] == '1':
            max_zero = max(max_zero, i-j-1)
            j = i
    return max_zero

if __name__ == "__main__":
    result = min_num_solution(529)
    print(result)