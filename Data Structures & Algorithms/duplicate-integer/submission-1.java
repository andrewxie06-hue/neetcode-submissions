class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> a = new HashSet<>();
        for(int i : nums){
            if(a.contains(i)) return true;
            a.add(i);
        }
        return false;
    }
}