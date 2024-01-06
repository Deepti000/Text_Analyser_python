####  Step-1 Define a string. #####

givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."


class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        ftext = text.replace('.','').replace('!','').replace('?','').replace(',','')
        # make text lowercase
        self.fmtText = ftext.lower()
        
    def freqAll(self):        
        # split text into words
        word = self.fmtText.split()
        # Create dictionary
        dic = {}
        for i in word:
            if not(i in dic):
                dic[i] = 1
            else:
                dic[i] += 1
        return dic
           
    def freqOf(self,word):
        # get frequency map
        dic = self.freqAll()
        if( word in dic):
            return dic[word]
        else:
            return 0


obj1 = TextAnalyzer(givenstring)
print("Formatted Text:", obj1.fmtText)
obj1.freqAll()
obj1.freqOf("lorem")
