#os.listdir(path):打开某个文件夹下的文件,以列表的形式返回
#os.path.splitext(path):分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作；索引0对应文件名，索引1对应扩展名；
#Image.thumbnail((size_x,size_y)):将图片裁剪成size_x*size_y大小的图片
import os
import os.path
from PIL import Image
def image_nail(infiles,size_x,size_y):
    f_list=os.listdir(infiles)
    for file in f_list:
        if os.path.splitext(file)[1]=='.jpg':
            im = Image.open(os.path.join(infiles, file))#不要使用文件的相对路径，需要使用绝对路径?
            im.thumbnail((size_x,size_y))
            im.save(infiles+os.path.splitext(file)[0]+ "_thumbnail.jpg", "JPEG")
if __name__=="__main__":
    image_nail(r'D:\360Downloads\GitHub客户端code\show-me-the-code\.vscode\No_0005_test_images',128,128)