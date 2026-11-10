class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> ans = new HashMap<>();
        for(int i = 0; i < strs.length; i++){
            char[] p = strs[i].toCharArray();
            Arrays.sort(p);
            if(ans.containsKey(new String(p))){
                ans.get(new String(p)).add(strs[i]);
            }
            else{
                List<String> w = new ArrayList<>();
                w.add(strs[i]);
                ans.put(new String(p), w);
            }
        }
        List<List<String>> a = new ArrayList<>();
        for (List<String> value : ans.values()) {
            a.add(value);
        }
        return a;
    }
}
