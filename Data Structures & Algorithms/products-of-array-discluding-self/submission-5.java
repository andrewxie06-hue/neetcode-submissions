class Solution {
    public int[] productExceptSelf(int[] nums) {
        int tot=1;
        int count = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0){
                tot *= nums[i];
            }
            else{
                count++;
            }
            
        }
        int[] ans = new int[nums.length];
        for(int i =0 ;i < nums.length; i++){
            if(count > 1){
                ans[i]=0;
            }
            else if(count == 1 && nums[i] != 0){
                ans[i] = 0;
            }
            else if(count == 1 && nums[i] == 0){
                ans[i] = tot;
            }
            else if(count == 0){
                ans[i] = tot/nums[i];
            }
        }
        return ans;
    }
}  
