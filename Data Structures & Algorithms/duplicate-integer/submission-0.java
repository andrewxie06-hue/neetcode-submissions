class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> a = new HashSet<>();
        for(int i : nums){
            a.add(i);
        }
        return a.size() != nums.length;
    }
}