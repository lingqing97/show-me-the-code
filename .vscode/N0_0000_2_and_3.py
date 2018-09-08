from PIL import ImageDraw,Image,ImageFont
import random
fontstr=str(random.randint(0,99))
def imagestr(img):
    draw=ImageDraw.Draw(img)
    width,height=img.size
    strfont=ImageFont.truetype("./arial.ttf",40)
    draw.text((width-40,0),fontstr,"#ff0000",strfont)
    img.save("./0000_result_2.jpg","jpeg")
    return 0
if __name__=="__main__":
    img=Image.open("./image.jpg")
    imagestr(img)