# Binary Search

int binarySearch(int[] nums, int target) {
    // 一左一右两个指针相向而行
    int left = 0, right = nums.length - 1;
    while(left <= right) {
        int mid = (right + left) / 2;
        if(nums[mid] == target)
            return mid; 
        else if (nums[mid] < target)
            left = mid + 1; 
        else if (nums[mid] > target)
            right = mid - 1;
    }
    return -1;
}

# python
# Binary Search 2 pointers
def binarySearch(self, nums,target):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left+right)/2
        if nums[mid] == target:
            return mid
        elif: 
            nums[mid] < target
            left = mid +1
        else:
            nums[mid] > target
            right = mid -1
    return -1
    
    