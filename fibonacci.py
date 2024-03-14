class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur=0
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            last=1
            secondLast=0
            for i in range(2,n+1):
                # print(i)
                cur=last+secondLast
                secondLast=last
                last=cur
        return cur
                
            