#安装第三方模块
#下载对应的源码，往往都是.tar.gz，.zip的压缩包，解压后，打开windows的cmd，切换到对应目录，运行：
#setup.py install
#即可去安装。
#python查看指令
#eg:
#>>help()
#help>PIL
#python查看.py文件指令
#help(math)
#dir指令查看python模块内置方法
#关于PIL:
#ImageDraw.draw(img)->创建要处理的图片对象
#PIL.ImageFont.truetype（font = None，size = 10，index = 0，encoding ='' ）—>创建tts字体格式对象
#font:字体格式文件(.tts后缀)  // size 定义字体大小（单位为磅） // encoding 要定义的字体编码格式
#PIL.ImageDraw.Draw.text（xy，text，fill = None，font = None，anchor = None ）->在图片的给定位置绘制字符串
#xy:字符串定位的左上角坐标(图片的左上角为（0,0）) // text:要填充的字符串 // font:设置字符串的字体格式（使用定义好的字体格式对象） // fill:字符串填充颜色
#关与Image
#img=Image.open(positon)定义图片对象
#img.size获取图片对象的大小，返回元组
#img.save(position,class)将图片另保存（第一个参数设置图片保存的位置，第二个参数设置图片保存的格式，一般为"jpg"或"jpeg"）


#**第 0000 题：** 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import ImageDraw,ImageFont,Image
import random
num=str(random.randint(1,99))
def addstr(img):
    draw=ImageDraw.Draw(img)
    strfont=ImageFont.truetype("./arial.ttf",size=40)
    width,height=img.size #注意不是img.size()
    fill="#ff0000"
    draw.text((width-40,0),num,fill,strfont)
    img.save("./0000_result.jpg","jpeg") 
    return 0
if __name__=="__main__":
    img=Image.open("./image.jpg")
    addstr(img)
