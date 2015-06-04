#coding=utf-8
#在右上角打印字符
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open('cat.jpg')
(width,height)=img.size #get the picture size with PIL?
draw = ImageDraw.Draw(img)

txt = "G"
fontsize=1
img_fraction = 0.05
font = ImageFont.truetype("ABeeZee-Italic.otf",fontsize)
while font.getsize(txt)[0] < img_fraction*width:
    fontsize += 1
    font = ImageFont.truetype("ABeeZee-Italic.otf",fontsize)

# print fontsize
# print width*0.8
# print width-fontsize
#字体大小和像素大小不一样
draw.text((width*0.9,0),txt,(255,0,0),font=font)
img.save('cat2.jpg')