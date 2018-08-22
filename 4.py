#虽然用c过了但还是写一下python 还不太会用python的列表
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        mid = int((n + m) / 2)
        tmp = [0]
        i = 0
        j = 0
        while  i < n and j < m:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else :
                tmp.append(nums2[j])
                j += 1
        while i < n:
            tmp.append(nums1[i])
            i += 1
        while j < m:
            tmp.append(nums2[i])
            j += 1
        if (n + m) % 2:
            return tmp[mid + 1]
        else :
            return (tmp[mid] + tmp[mid+1]) / 2
        