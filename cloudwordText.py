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
    font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",#������һ����ʾ����������
    margin=2)
wc2 = wc1.generate(text1)         #���ǹ۲쵽generate()����һ��Unicode�Ķ�������֮ǰҪ���ı������unicode����

plt.imshow(wc2)
plt.axis("off")
plt.show()
#WordCloud.to_file("C:\\Users\\fyc\\Desktop\\myCloud.png")