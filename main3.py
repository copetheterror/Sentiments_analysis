import string
import matplotlib.pyplot as plt
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#reading the text file:
text = open('read.txt', encoding='utf-8').read()

#converting to lowercase:
lower_case = text.lower()

#removing punctuations:
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

#splitting text into words(Tokenizing):
tokenized_words = word_tokenize(cleaned_text,"english")

#removing stopwords from tokenized words list:
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

#creating emotion list to count no. of each emotions :
emotion_list =[]
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", "").replace("'" ,"").strip()
        word, emotion = clear_line.split(": ")
        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)

#Counting the no. of each emotions in Emotional list & seperating into keys and values:
w = Counter(emotion_list)
x = list(w.keys())
y = list(w.values())
max_ = sum(y)

#Analyzing the sentiment of a text:
score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
print(score)
if score['neg']> score['pos']:
    print("Negative Sentiment")
elif score['pos'] > score['neg']:
    print("Positive Sentiment")
else:
    print("Neutral Vibe")

#Counting the percentage of values of x(Emotions):
for i, val in enumerate(y):
    y[i] = (val/max_)*100

#plotting the graph
plt.bar(x, y)
plt.savefig('graph.png')
plt.show()

