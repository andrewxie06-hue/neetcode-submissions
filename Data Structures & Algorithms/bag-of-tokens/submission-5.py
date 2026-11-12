class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        token = sorted(tokens)
        best = 0
        t = 0
        right = len(token) - 1
        left = 0
        print(token)
        while left <= right:
            if power >= token[left]:
                t += 1
                power -= token[left]
                best = max(best,t)
                left += 1
            elif t > 0:
                power += token[right]
                right -= 1
                t -= 1
            else:
                break
            print(t, power)

           
        return best

