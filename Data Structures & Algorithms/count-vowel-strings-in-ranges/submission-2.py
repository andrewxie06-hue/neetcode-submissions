class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        d = {}
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(len(words)):
            if words[i][len(words[i])-1] in vowels and words[i][0] in vowels:
                d[i] = True
            else:
                d[i] = False
        ans = []
        count = 0
        print(d)
        for i in range(len(queries)):
            for j in range(queries[i][0], queries[i][1] + 1):
                if d[j] == True:
                    count+= 1
                
            ans.append(count)
            count = 0
        return ans