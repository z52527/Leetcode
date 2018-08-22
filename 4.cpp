//觉得像归并排序就先用C试了一下结果a了 yeah， 但不是动态数组，随便开了个范围，还是不稳
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i = 0, j = 0, tot = 0;
    double tmp[10010];
    while(i < nums1Size&&j < nums2Size){
        if(nums1[i] <= nums2[j]){
            tmp[++tot] = nums1[i++];
        }
        else{
            tmp[++tot] = nums2[j++];
        }
    }
    while(i < nums1Size)tmp[++tot] = nums1[i++];
    while(j < nums2Size)tmp[++tot] = nums2[j++];
    if((nums1Size + nums2Size) % 2)
        return tmp[((nums1Size + nums2Size) / 2) + 1];
    else 
        return (tmp[(nums1Size + nums2Size) / 2] + tmp[((nums1Size + nums2Size) / 2) + 1]) / 2;
}