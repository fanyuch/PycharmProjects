import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

if __name__ == '__main__':
    with open("C:\\Users\\fyc\\Desktop\\json.txt", "rb") as f:
        text = f.read()
    text_jieba = jieba.cut(text, cut_all=True)
    text_split = "".join(text_jieba)

    my_wordcloud = WordCloud().generate(text_split)


    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
    pass

pass
pass



