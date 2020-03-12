from typing import List


class Solution:

  def countBits(self, num: int) -> List[int]:
    return [len('{0:b}'.format(i).replace('0', '')) for i in range(0, num + 1)]


my = Solution()

n = 5

ans = my.countBits(n)
print('ans', ans)
