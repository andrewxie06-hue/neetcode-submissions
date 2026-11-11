class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        one = 1
        two = 2
        no = 3
        for i in range(2, n-1):
            
            temp = no
            no = two + no
            one = two
            two = temp
            print(one, two, no)
        return no
