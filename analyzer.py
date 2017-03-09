import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives=set()
        filePos=open("positive-words.txt","r")
        for line in filePos:
            if(not line.startswith(";")): #!check if the word has begin of ";"
                self.positives.add(str.strip(line)) #!remove unnesscessary parts of string
        filePos.close()
        self.negatives=set()
        fileNeg=open("negative-words.txt","r")
        for line in fileNeg:
            if(not line.startswith(";")):
                self.negatives.add(str.strip(line))
        fileNeg.close()
    
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        score=0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        for token in tokens:
            if token in self.positives:
                score+=1
            elif token in self.negatives:
                score-=1
        return score