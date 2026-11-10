class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> checker = new HashSet<>();
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                
                char val = board[i][j];
                if(val == '.'){
                    continue;
                }
                else{
                    String r = "row" + i + val;
                    String c = "col" + j + val;
                    String b = "box" + (i / 3) + (j / 3) + val;
                    if(!checker.add(r) || !checker.add(c) || !checker.add(b)){
                        return false;
                    }
                }
            }
        }
        return true;
    }
}