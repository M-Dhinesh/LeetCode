class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans=[]
        deck.sort(reverse=True)
        for i in deck:
            ans=[i]+ans[-1:]+ans[:-1]
        return ans
