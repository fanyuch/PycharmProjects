#coding: gbk
import chardet
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("C:\\Users\\fyc\\Desktop\\virgo.txt", "r") as f:
    text = f.read()
type = chardet.detect(text)
text1 = text.decode(type["encoding"])


pass



wc1 = WordCloud(
    background_color="white",
    width=1000,
    height=860,
    font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",#不加这一句显示口字形乱码
    margin=2)
wc2 = wc1.generate(text1)         #我们观察到generate()接受一个Unicode的对象，所以之前要把文本处理成unicode类型

plt.imshow(wc2)
plt.axis("off")
plt.show()
#WordCloud.to_file("C:\\Users\\fyc\\Desktop\\myCloud.png")