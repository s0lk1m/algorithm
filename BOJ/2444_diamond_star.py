'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
#
N = int(input())
# 총 2 * N - 1

# 1 ~ N-1 삼각형 1, 3, 5, 7
#  N        9
# N + 1 ~ 2 * N - 1 역삼각형 7, 5, 3, 1

for n in range(1, N):
    # 별의 갯수 2 * n - 1
    print(" " * (N-1-n), '*' * (2 * n - 1))
for _ in range(1):
    print('*' * (2*N-1))
for n in range(N, 0, -1):
    print(" " * (N-n-2), '*' * (2 * n - 1))
