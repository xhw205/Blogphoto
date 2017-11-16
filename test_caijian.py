# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 22:52:41 2017

@author: xhwshuai
"""

#coding: utf-8
from PIL import Image
import os
import sys
import json
from datetime import datetime


# 定义压缩比，数值越大，压缩越小
SIZE_normal = 1.0
SIZE_small = 1.5
SIZE_more_small = 2.0
SIZE_more_small_small = 3.0


def make_directory(directory):
    """创建目录"""
    os.makedirs(directory)

def directory_exists(directory):
    """判断目录是否存在"""
    if os.path.exists(directory):
        return True
    else:
        return False

def list_img_file(directory):
    """列出目录下所有文件，并筛选出图片文件列表返回"""
    old_list = os.listdir(directory)
    # print old_list
    new_list = []
    for filename in old_list:
        name, fileformat = filename.split(".")
        if fileformat.lower() == "jpg" or fileformat.lower() == "png" or fileformat.lower() == "bmp":
            new_list.append(filename)
    # print new_list
    return new_list


#def print_help():
#    print("""
#    This program helps compress many image files
#    you can choose which scale you want to compress your img(jpg/png/etc)
#    1) normal compress(4M to 1M around)
#    2) small compress(4M to 500K around)
#    3) smaller compress(4M to 300K around)
#    """)

def compress(choose, des_dir, src_dir, file_list):
    
    if choose == '1':
        scale = SIZE_normal
    if choose == '2':
        scale = SIZE_small
    if choose == '3':
        scale = SIZE_more_small
    if choose == '4':
        scale = SIZE_more_small_small
    for infile in file_list:
        img = Image.open(src_dir+infile)
        # size_of_file = os.path.getsize(infile)
        w, h = img.size
        img.thumbnail((int(w/scale), int(h/scale)))
        img.save(des_dir + infile)
def compress_photo():
    src_dir, des_dir = "D:/Blogphoto/photos/", "D:/Blogphoto/min_photos/"
    file_list_src = list_img_file(src_dir)#原来的图片
    print(file_list_src)
    file_list_des = list_img_file(des_dir)
    for i in range(len(file_list_des)):#遍历目标图片
        if file_list_des[i] in file_list_src:#原始图片中还用目标图片
            file_list_src.remove(file_list_des[i])#原始图片删去目标
            print(file_list_des[i])
    print(file_list_src)
    compress('4', des_dir, src_dir, file_list_src)
#
def handle_photo():

    src_dir, des_dir = "D:/Blogphoto/photos/", "D:/Blogphoto/min_photos/"
    file_list = list_img_file(src_dir)
    list_info = []
    for i in range(len(file_list)):
        filename = file_list[i]
        date_str, info = filename.split("_")
        info, _ = info.split(".")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        year_month = date_str[0:7]            
        if i == 0:  # 处理第一个文件
            new_dict = {"date": year_month, "arr":{'year': date.year,
                                                                   'month': date.month,
                                                                   'link': [filename],
                                                                   'text': [info],
                                                                   'type': ['image']
                                                                   }
                                        } 
            list_info.append(new_dict)
        elif year_month != list_info[-1]['date']:  # 不是最后的一个日期，就新建一个dict
            new_dict = {"date": year_month, "arr":{'year': date.year,
                                                   'month': date.month,
                                                   'link': [filename],
                                                   'text': [info],
                                                   'type': ['image']
                                                   }
                        }
            list_info.append(new_dict)
        else:  # 同一个日期
            list_info[-1]['arr']['link'].append(filename)
            list_info[-1]['arr']['text'].append(info)
            list_info[-1]['arr']['type'].append('image')
    list_info.reverse()  # 翻转
    final_dict = {"list": list_info}
    with open("D:/blog/source/photos/data.json","w") as fp:
        json.dump(final_dict, fp)
#D:\blog\source\photos
def cut_photo():
    
    src_dir = "D:/test/photos/"
    beifen_dir = "D:/test/min_photos/"
    file_list = list_img_file(src_dir)
    print (file_list)

    for infile in file_list:
        img = Image.open(src_dir+infile)
        (x, y) = img.size  
        print(img.size)
        if x > y:  
            region = (int(x/2-y/2), 0, int(x/2+y/2), y)  
     
            crop_img = img.crop(region)  
 
            crop_img.save(beifen_dir+infile)             
        elif x < y:  
            region = (0, int(y/2-x/2), x, int(y/2+x/2))
          
            crop_img = img.crop(region)  
         
            crop_img.save(beifen_dir+infile)           

def git_operation():

    os.system('git add --all')
    os.system('git commit -m "add photos"')
    os.system('git push origin master')

if __name__ == "__main__":
    cut_photo()        
    compress_photo()  
    handle_photo()  
    git_operation()
# 
    
    
    