class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted(dictionary,key = lambda ele: len(ele))
        lst = []
        for i in sentence.split():
            temp = 0
            for j in dictionary:
                if i.startswith(j):
                    temp = 1
                if temp == 1:
                    lst.append(j)
                    break
            if temp == 0:
                lst.append(i)
        return " ".join(lst)
