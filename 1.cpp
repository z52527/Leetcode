class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        map <int, int > dic;
        for(int i = 0; i < n; i++){
            if(dic.count(nums[i]))
                return {dic[nums[i]], i};
            else dic[target - nums[i]] = i;
        }
        return {};
    }
    
};