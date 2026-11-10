class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Arrays.sort(nums);
        int count = 1;
        Map<Integer, Integer> a = new HashMap<>();
        for(int i= 1;i < nums.length; i++){
            if(nums[i] == nums[i-1]){
                count++;
            }
            else{
                System.out.println("asdasd");
                a.put(nums[i-1], count);
                count= 1;
            }
        }
        a.put(nums[nums.length-1], count);
        List<int[]> arr = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : a.entrySet()) {
            arr.add(new int[] {entry.getValue(), entry.getKey()});
        }
        arr.sort((c, b) -> b[0] - c[0]);
        int[] ans = new int[k];
        for(int i = 0; i<k;i++){
            ans[i] = arr.get(i)[1];
        }
        return ans;
    }
}
