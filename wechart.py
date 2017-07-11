import itchat
import pickle
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

myFriends = []

def getFriendstofile():
    itchat.login()
    friendsTmp = itchat.get_friends(update=True)[0:]
    with open("friend", "w") as f:
        pickle.dump(friendsTmp, f)


def loadFriendtobuffer():
    with open("friend", 'r') as f:
        friendsTmp = pickle.load(f)
    return friendsTmp

def friendSex():
    male = 0
    female = 0
    for i in myFriends[1:]:
        if i["Sex"] ==1:
            male += 1
        if i["Sex"] == 2:
            female += 1

def friendCity():
    city = {}
    tmp = 0
    for i in myFriends[1:]:
        if city.has_key(i["City"]):
            city[i["City"]] += 1
        else:
            city[i["City"]] = 1
    '''for i in city.values():
        tmp += i
    pass'''

def friendCloud():
    siglist = []
    for i in myFriends:
        signature = i["Signature"].strip().replace("span","").replace("class", "").replace("emoji", "")
        rep = re.compile("1f\d+\w*|[<>/=]")
        signature = rep.sub("", signature)
        siglist.append(signature)
    text = "".join(siglist)
    wordlist = jieba.cut(text, cut_all=True)
    word_space_split = "".join(wordlist)

    my_wordcloud = WordCloud(
        font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",
        max_words=3000,
        scale=1.5,
        relative_scaling=1,
        max_font_size=400,
        background_color="white",
        width=7000,
        height=7000,
        margin=2).generate(text)
    plt.imshow(my_wordcloud)
    plt.axis("off")

    plt.show()








if __name__ == '__main__':
    #getFriendstofile()
    myFriends = loadFriendtobuffer()
    friendSex()
    friendCity()
    friendCloud()
    pass

