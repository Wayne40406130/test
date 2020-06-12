nums1=[0,0,3,0,0,0,0,0,0]
nums2=[-1,1,1,1,2,3]

m=3
n=6

while n>=1:
    print(m)
    print(nums2[n-1])
    if m==0:
        nums1.insert(0,nums2[n-1])
        n -= 1
    elif nums2[n-1]>=nums1[m-1]:
        nums1.insert(m,nums2[n-1])
        n-=1
        nums1.pop(-1)
        print(nums1)
    else:
        m-=1
