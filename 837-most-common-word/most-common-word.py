class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [w for w in re.split(r"[., ?!;']+",paragraph.lower()) if w]
        d=Counter(words)
        m=0
        banned = set(banned)
        most_frequent_word=""
        for word, count in d.items():
            if word not in banned and count > m:
                m = count
                most_frequent_word = word
        return most_frequent_word