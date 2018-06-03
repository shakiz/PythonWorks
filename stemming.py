from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pyperclip as pp

#copying text by pyperclip module
sentence=str(pp.paste())
#initalizing the porter stemmer
ps=PorterStemmer()
#dividing the whole text into group of words
words=word_tokenize(sentence)

#storing the stop words of english
stop_words=set(stopwords.words('english'))

filtered_words=[]
unfiltered_words=[]

for w in words:
    if w not in stop_words:
        if w!='.' or w!='!' or w!=':':
            filtered_words.append(w)
    else:
        if w!='.' or w!='!' or w!=':':
            unfiltered_words.append(w)
print('Printing filtered words:')
for w in filtered_words:
    print(w)
    
print('Printing unfiltered words:')
for w in unfiltered_words:
    print(w)

print('Printing stem words:')
for w in words:
    print(ps.stem(w))
