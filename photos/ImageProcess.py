# coding=utf-8  
from PIL import Image  
import shutil  
import os  

class Graphics:  

    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile

    def fixed_size(self, width, height):  
        """按照固定尺寸处理图片"""  
        im = Image.open(self.infile)  
        out = im.resize((width, height),Image.ANTIALIAS)  
        out.save(self.outfile)  


    def resize_by_width(self, w_divide_h):  
        """按照宽度进行所需比例缩放"""  
        im = Image.open(self.infile)  
        (x, y) = im.size   
        x_s = x  
        y_s = x/w_divide_h  
        out = im.resize((x_s, y_s), Image.ANTIALIAS)   
        out.save(self.outfile)  


    def resize_by_height(self, w_divide_h):  
        """按照高度进行所需比例缩放"""  
        im = Image.open(self.infile)  
        (x, y) = im.size   
        x_s = y*w_divide_h  
        y_s = y  
        out = im.resize((x_s, y_s), Image.ANTIALIAS)   
        out.save(self.outfile)  


    def resize_by_size(self, size):  
        """按照生成图片文件大小进行处理(单位KB)"""  
        size *= 1024  
        im = Image.open(self.infile)  
        size_tmp = os.path.getsize(self.infile)  
        q = 100  
        while size_tmp > size and q > 0:  
            print (q)  
            out = im.resize(im.size, Image.ANTIALIAS)  
            out.save(self.outfile, quality=q)  
            size_tmp = os.path.getsize(self.outfile)  
            q -= 5  
        if q == 100:  
            shutil.copy(self.infile, self.outfile)  

  
    def cut_by_ratio(self):  
        """
		把图片规整成正方形
        """  
        im = Image.open(self.infile)  
        (x, y) = im.size  
        print (im.size)
        if x > y:  
            print (11)
            region = (int(x/2-y/2), 0, int(x/2+y/2), y)  
            #裁切图片  
            crop_img = im.crop(region)  
            #保存裁切后的图片  
            crop_img.save(self.outfile)             
        elif x < y:  
            region = (0, int(y/2-x/2), x, int(y/2+x/2))
            #裁切图片  
            crop_img = im.crop(region)  
            #保存裁切后的图片  
            (x,y) = crop_img.size
            print  (x,y)
            fp = "D:\test\min_photos"
            crop_img.save("3.jpg")
        

if __name__ == "__main__":
    Graphics("D:/test/photos/1.jpg").cut_by_ratio()