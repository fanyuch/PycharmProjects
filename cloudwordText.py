from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("C:\\Users\\fyc\\Desktop\\json.txt", "r") as f:
    text = f.read()
wordcloud = WordCloud(
    background_color="white",
    width=1000,
    height=860,
    margin=2).generate(text)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
#WordCloud.to_file("C:\\Users\\fyc\\Desktop\\myCloud.png")