from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pyperclip

text=str(pyperclip.paste())
stop_words=set(stopwords.words('English'))
#print(stop_words)

filtered_words=[]
extra_words=[]

for w in word_tokenize(text):
    if w not in stop_words:
        filtered_words.append(w)
    else:
        extra_words.append(w)

print('Printing filtered words:')
for w in filtered_words:
    if w=='.':
        continue
    else:
        print(w)
print('Printing unfiltered words:')
for w in extra_words:
    if w=='.':
        continue
    else:
        print(w)
