class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        
        String real = "";
        for(char a : s.toCharArray()){
            if(Character.isLetterOrDigit(a)){
                real += a;
            }
        }
        int right = real.length()-1;
        System.out.println(real);
        while(left < right){
            if(Character.toLowerCase(real.charAt(left)) != Character.toLowerCase(real.charAt(right))){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
