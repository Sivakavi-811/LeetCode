class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score=0
        counter=0
        for i in events:
            if counter == 10:
                break
            if i == "W":
                counter+=1
            elif i ==  "WD" or i == "NB":
                score+=1
            else:
                score+=int(i)
        return [score,counter]