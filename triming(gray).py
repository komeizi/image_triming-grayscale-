import os
import re
import glob
from unicodedata import name
import cv2
import time
import sys

def split_do(c,base,x,y,n,size):
    #file_create
    dir_path = os.getcwd() 
    make_dir_split_image = dir_path + os.sep + 'split_images_'+f'{size}'
    print(make_dir_split_image)
    
    s1 = 0
    s2 = -1

    if c == False:

        while  base.shape[0]>=size+y:       
            img = base[y:size+y,x:size+x]
            
            s1+=1
            print(img.shape)
            if img.shape[0]==size and img.shape[1] == size:
                cv2.imwrite(make_dir_split_image+os.sep+f'{n}_imagesplit{s1}.png',img)#
            time.sleep(1)

            x += size
            if img.shape[1]<size:
                a = size-img.shape[1]
                s1+=1
                if img.base[y:size+y,x-size-a:].shape[0]==size and base[y:size+y,x-size-a:].shape[1] == size: 
                    cv2.imwrite(make_dir_split_image+os.sep+f'{n}_imagesplit{s1}.png',base[y:size+y,x-size-a:])
                time.sleep(1)
                x=0
                y += size

        return x,y

    if c == True:
        while  base.shape[1]>=x:
            img = base[:,x:size+x]
            s2 -= 1
            if img.shape[0]==size and img.shape[1] == size: 
                cv2.imwrite(make_dir_split_image+os.sep+f'{n}imagesplit{s2}.png',img)#
            time.sleep(1)
            x+=size
            if img.shape[1]<size:
                a = size-img.shape[1]
                test = base[:,x-size-a:]
                s2 -= 1
                if test.shape[0]==size and test.shape[1] == size: 
                    cv2.imwrite(make_dir_split_image+os.sep+f'{n}imagesplit{s2}.png',test)#
                time.sleep(1)

        return



def image_split(img,i,size):
    
    x = 0
    y = 0
    c = 0
    number = (str(i).split('.')[0]).split('/')[-1]
    dir_path = os.getcwd()
    make_dir_split_image = dir_path + os.sep + 'split_images_'+f'{size}'
    os.makedirs(make_dir_split_image,exist_ok=True)
    x,y=split_do(c,img,x,y,number,size)
    c=1
    a = size-img[y:size+y,x:size].shape[0]
    test=img[y-a:size+y,x:]
    if y!=0:
        split_do(c,test,x,y,number,size)


def main(dir,size):
    image_path=[p for p in glob.glob(dir+os.sep+'**', recursive=True) if os.path.isfile(p)]
    
    for i in image_path:#tpdm
        img=cv2.imread(i)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        image_split(img,i,size)

if __name__ == '__main__':
    args = sys.argv
    print(args)
    if len(args)==3:

        if os.path.isdir(args[1]):
            main(args[1],int(args[2]))

        else:
            print("Error")
     else:
        print("Error")
