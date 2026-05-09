class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score=0
        counter=0
        for i in events:
            if counter>=10:
                return[score,counter]
            if i in {"1","NB","WD"}:
                score+=1
            elif i in {"2","3","4","6"}:
                score+=int(i)
            elif i == "W":
                counter+=1
        return [score,counter]
        