#coding: gbk
import chardet
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("C:\\Users\\fyc\\Desktop\\json.txt", "r") as f:
    text = f.read()
type = chardet.detect(text)
text1 = text.decode(type["encoding"])
text2 = text1.encode("utf-8")


wc1 = WordCloud(
    background_color="white",
    width=1000,
    height=860,
    margin=2)
wc2 = wc1.generate(text2)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
#WordCloud.to_file("C:\\Users\\fyc\\Desktop\\myCloud.png")