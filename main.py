import numpy as np
import cv2
from PIL import Image
from matplotlib import pyplot as plt
import os
from os import listdir
from os.path import isfile, join
import pandas as pd

def load_images_from_folder(folder):
    train_data=[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),cv2.IMREAD_GRAYSCALE)
        img=~img
        if img is not None:
            ret,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
            ret,ctrs,ret=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
            cnt=sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
            w=int(28)
            h=int(28)
            maxi=0
            for c in cnt:
                x,y,w,h=cv2.boundingRect(c)
                maxi=max(w*h,maxi)
                if maxi==w*h:
                    x_max=x
                    y_max=y
                    w_max=w
                    h_max=h
            im_crop= thresh[y_max:y_max+h_max+10, x_max:x_max+w_max+10]
            im_resize = cv2.resize(im_crop,(28,28))
            im_resize=np.reshape(im_resize,(784,1))
            train_data.append(im_resize)
    return train_data


data=[]
path="D:\Projects\Python\Temp\Handwritten-Equation-Solver-master\Training Images\\"

# assign '-'=10
data = load_images_from_folder(path+'-')
len(data)
for i in range(0, len(data)):
    data[i] = np.append(data[i], ['10'])

print(len(data))

#assign + = 11
data11=load_images_from_folder(path+'+')

for i in range(0,len(data11)):
    data11[i]=np.append(data11[i],['11'])
data=np.concatenate((data,data11))
print(len(data))

data0=load_images_from_folder(path+'0')
for i in range(0,len(data0)):
    data0[i]=np.append(data0[i],['0'])
data=np.concatenate((data,data0))
print(len(data))

data1=load_images_from_folder(path+'1')

for i in range(0,len(data1)):
    data1[i]=np.append(data1[i],['1'])
data=np.concatenate((data,data1))
print(len(data))


data2=load_images_from_folder(path+'2')

for i in range(0,len(data2)):
    data2[i]=np.append(data2[i],['2'])
data=np.concatenate((data,data2))
print(len(data))

data3=load_images_from_folder(path+'3')

for i in range(0,len(data3)):
    data3[i]=np.append(data3[i],['3'])
data=np.concatenate((data,data3))
print(len(data))


data4=load_images_from_folder(path+'4')

for i in range(0,len(data4)):
    data4[i]=np.append(data4[i],['4'])
data=np.concatenate((data,data4))
print(len(data))

data5=load_images_from_folder(path+'5')

for i in range(0,len(data5)):
    data5[i]=np.append(data5[i],['5'])
data=np.concatenate((data,data5))
print(len(data))


data6=load_images_from_folder(path+'6')

for i in range(0,len(data6)):
    data6[i]=np.append(data6[i],['6'])
data=np.concatenate((data,data6))
print(len(data))

data7=load_images_from_folder(path+'7')

for i in range(0,len(data7)):
    data7[i]=np.append(data7[i],['7'])
data=np.concatenate((data,data7))
print(len(data))

data8=load_images_from_folder(path+'8')

for i in range(0,len(data8)):
    data8[i]=np.append(data8[i],['8'])
data=np.concatenate((data,data8))
print(len(data))


data9=load_images_from_folder(path+'9')

for i in range(0,len(data9)):
    data9[i]=np.append(data9[i],['9'])
data=np.concatenate((data,data9))
print(len(data))

#assign * = 12
data12=load_images_from_folder(path+'times')

for i in range(0,len(data12)):
    data12[i]=np.append(data12[i],['12'])
data=np.concatenate((data,data12))
print(len(data))

#assign / = 13
data13 = load_images_from_folder(path+'div')
for i in range(0, len(data13)):
    data13[i] = np.append(data13[i], ['13'])
data=np.concatenate((data,data13))
print(len(data))

#assign ( = 14
data14 = load_images_from_folder(path+'(')
for i in range(0, len(data14)):
    data14[i] = np.append(data14[i], ['14'])
data=np.concatenate((data,data14))
print(len(data))

#assign ) = 15
data15 = load_images_from_folder(path+')')
for i in range(0, len(data15)):
    data15[i] = np.append(data15[i], ['15'])
data=np.concatenate((data,data15))
print(len(data))

#assign sqrt= 16
data16 = load_images_from_folder(path+'sqrt')
for i in range(0, len(data16)):
    data16[i] = np.append(data16[i], ['16'])
data=np.concatenate((data,data16))
print(len(data))

#assign x=17
data17 = load_images_from_folder(path+'times')
for i in range(0, len(data17)):
    data17[i] = np.append(data17[i], ['17'])
data=np.concatenate((data,data17))
print(len(data))

#y=18
data18 = load_images_from_folder(path+'y')
for i in range(0, len(data18)):
    data18[i] = np.append(data18[i], ['18'])
data=np.concatenate((data,data18))
print(len(data))

#z=19
data19 = load_images_from_folder(path+'z')
for i in range(0, len(data19)):
    data19[i] = np.append(data19[i], ['19'])
data=np.concatenate((data,data19))
print(len(data))

#= = 20
data20 = load_images_from_folder(path+'=')
for i in range(0, len(data20)):
    data20[i] = np.append(data20[i], ['20'])
data=np.concatenate((data,data20))
print(len(data))


df=pd.DataFrame(data,index=None)
df.to_csv('train_final.csv',index=False)
fp=open("length.txt",'w')
fp.write(str(len(data)))
fp.close()