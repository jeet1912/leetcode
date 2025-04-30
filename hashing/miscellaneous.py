from collections import defaultdict, Counter

class Miscellaneous:
    
    def returnAnagramsFromArray(self, strs: list[str]) -> list[list[str]]:
        hashMap = defaultdict(list)
        for str in strs:
            sortedSt = "".join(sorted(str))
            hashMap[sortedSt].append(str)
        return list(hashMap.values())
            
    
m = Miscellaneous()
print(m.returnAnagramsFromArray(strs = ["eat","tea","tan","ate","nat","bat"]))
