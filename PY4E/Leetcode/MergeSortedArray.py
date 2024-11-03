def merge(nums1, nums2):
    m =  len(nums1) - len(nums2)
    n = len(nums2)
    r1, r2= m - 1, n - 1
    for w in range(m + n - 1, -1, -1):
        if r2 < 0:
            break
        if r1 >= 0 and nums1[r1] > nums2[r2]:
            nums1[w] = nums1[r1]
            r1 -= 1
        else:
            nums1[w] = nums2[r2]
            r2 -= 1
    return nums1    

print(merge([1,2,3,0,0,0], [2,5,6]), [1,2,2,3,5,6])