class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordP = abbrP = 0
    
        while wordP < len(word) and abbrP < len(abbr):
            if word[wordP] == abbr[abbrP]:
                wordP, abbrP = wordP + 1, abbrP + 1
            else:
                if abbr[abbrP] == "0":
                    return False
                elif abbr[abbrP].isnumeric():
                    numS = ""
                    # while abbrP < len(abbr) and self.isInteger(abbr[abbrP]):
                    while abbrP < len(abbr) and abbr[abbrP].isnumeric():
                        numS += abbr[abbrP]
                        abbrP += 1
                    num = int(numS)
                    wordP = wordP + num
                else:
                    return False
        
        return abbrP == len(abbr) and wordP == len(word)

    # def isInteger(self, s):
    #     try:
    #         int(s)
    #         return True
    #     except ValueError:
    #         return False


        