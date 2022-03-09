# Cleaning text steps:
# 1) create a text file and take text from it
# 2) Convert the letter into lowercase ('Apple' is not equal to 'apple')
# 3) Remove punctuations like '.,?!' etc. (hi! This is built with python.)

import string
from collections import Counter
import matplotlib.pyplot as plt
#import matplotlib.ticker as mtick
#import pandas as pd
print(string)
text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
#print(lower_case)
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
#print(cleaned_text)

tokanized_words = cleaned_text.split()
print(tokanized_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokanized_words:
    if word not in stop_words:
        final_words.append(word)
#print(final_words)

# NLP emotion algorithm
# 1) check if the word in final words[] also present in emotion.txt
# -Open the emotion.txt file
# -Loop through each line and clear it
# -Extract the word and emotion using split
# 2) if the word is present -> Add the emotion to the emotion list
# 3) Finally count the each emotion in emotion list

emotion_list =[]
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", "").replace("'" ,"").strip()
        #print(clear_line)
        word,emotion = clear_line.split(": ")
        #print("Word: "+ word+" " + "Emotion: " + emotion)

        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w = Counter(emotion_list)
print(w)
######p = pd.DataFrame([w])

x = list(w.keys())
y = list(w.values())
max_ = sum(y)
for i, val in enumerate(y):
    y[i] = (val/max_)*100

plt.bar(x,y)
plt.savefig('graph.png')
plt.show()

#fig, ax1 = plt.subplots()
#ax1.bar(w.keys(), w.values())
#####ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
#fig.autofmt_xdate()
#plt.savefig('graph.png')
#plt.show()

