class Solution:
    def climbStairs(self, n: int) -> int:
        # if n < 0:
        #     return 0
        # if n == 0:
        #     return 1
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        num_1 = 0
        num_2 = 1

        for i in range(n):
            temp = num_1 + num_2
            num_1 = num_2
            num_2 = temp

        return temp





        

     
    