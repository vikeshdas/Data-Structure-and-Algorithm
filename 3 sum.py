class Solution(object):
    def threeSum(self, nums):

        nums=sorted(nums)
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if sum<0:
                    j+=1
                elif sum>0:
                    k-=1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(nums[j]==nums[j-1] and j<k):
                        j+=1
                    while(nums[k]==nums[k+1] and j<k):
                        k-=1
        return result