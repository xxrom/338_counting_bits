from typing import List


class Solution:

  def countBits(self, num: int) -> List[int]:
    '''
      (80ms)
      URL: https://leetcode.com/problems/counting-bits/discuss/527806/4-line-python-solution
      Dynamic programming solution, example could be

      0 -> 0, num_bits[0] = 0
      1 -> 1, num_bits[1] = 1
      2 -> 10, num_bits[2] = num_bits[2//2] + 2%2 = 1
      3 -> 11
      6 -> 110, 6//2 = 3, 6%2 = 0, num_bits[6] = num_bits[3] + 0 = 2
    '''

    num_bits = [0]
    for i in range(1, num + 1):
      num_bits.append(num_bits[i // 2] + i % 2)
    return num_bits

    # (84ms)
    # Not so bad solution either =)
    # return [bin(i).count('1') for i in range(0, num + 1)]


my = Solution()

n = 5

ans = my.countBits(n)
print('ans', ans)

# Runtime: 84 ms, faster than 70.01% of Python3 online submissions for Counting Bits.
# Memory Usage: 19.7 MB, less than 5.00% of Python3 online submissions for Counting Bits.

# 0     0     0
# 1     1     1
# 2    10     1
# 3    11     2
# 4   100     1
# 5   101     2
# 6   110     2
# 7   111     3
# 8  1000     1
# 9  1001     2
# 10 1010     2

# dynamic programming solution faster on 4 ms =)))))))))))))
# Runtime: 80 ms, faster than 84.16% of Python3 online submissions for Counting Bits.
# Memory Usage: 19.7 MB, less than 5.00% of Python3 online submissions for Counting Bits.