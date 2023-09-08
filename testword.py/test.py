from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ""
with open("testword.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[:]:
        text += line
        #if '] [' in line:
        #    text+=line.split('] ')[2].replace('ㅋ','').replace('ㅠ','').replace('ㅜ','').replace('사진\n','').replace('이모티콘\n','').replace('삭제된 메시지입니다','').replace('저도','').replace('ㅎ','').replace('제가','').replace('넹','').replace('저는','')


font_path = 'C:/Windows/Fonts/malgun.ttf'

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path=font_path, background_color="white", mask = mask)
wc.generate(text)
wc.to_file("result_review.png")