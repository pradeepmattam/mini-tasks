'''
traverse from top-left most to bottom-right most point in a given
mxn matrix.
paths allowed right and down
'''

from timeit import default_timer


def count_path_traverse_matrix(m, n):
    if m == 1 or n == 1:
        return 1
    return count_path_traverse_matrix(m-1, n) + count_path_traverse_matrix(m, n-1)


def dp_count_path_traverse_matrix(m, n, dp):
    if dp[m][n] != -1:
        return dp[m][n]
    if m == 1 or n == 1:
        dp[m][n] = 1
    else:
        dp[m][n] = dp_count_path_traverse_matrix(m-1, n, dp) + dp_count_path_traverse_matrix(m, n-1,dp)
    return dp[m][n]

start = default_timer()
dp = [[-1 for i in range(20)] for j in range(20)]
print(f"number of paths for 12X12 matrix (via dp) {dp_count_path_traverse_matrix(12,12,dp)}")
print(f"time take for dp solution : {default_timer()-start:.5f}")

start = default_timer()
print(f"number of paths for 12X12 matrix {count_path_traverse_matrix(12,12)}")
print(f"time take for non-dp solution : {default_timer()-start:.5f}")




