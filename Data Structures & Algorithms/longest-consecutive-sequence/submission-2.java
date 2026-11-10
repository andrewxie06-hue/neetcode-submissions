class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> t = new HashSet<>();
        for(int i : nums){
            t.add(i);
        }
        int curr = 0;
        int longest = 0;
        for(int n : t){
            if(!t.contains(n-1)){
                for(int i = n; i >= n; i++){
                    if(t.contains(i)){
                        curr++;
                    }
                    else{
                        break;
                    }
                }
                longest = Math.max(longest, curr);
                curr = 0;
            }
        }
        return longest;
    }
}
