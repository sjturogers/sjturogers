# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 10:06:49 2022

@author: apple
"""


import random

ans=random.randint(1,20)
counter=0

while counter<5:
    guess=input('請再1~20間猜一個數字(只能猜五次): ')
    guess=int(guess)
    if guess>20 or guess<0:
        print('輸入錯誤,請重新測試!')
        counter=counter+1
    else:
        if guess>ans:
            if counter==4:
                print("抱歉,您已經測試五次了!")
                break
            else:
               print('小一點')
               counter=counter+1
        elif guess<ans:
            if counter==4:
                print('"抱歉,您已經測試五次了!')
                break
            else:
                print('大一點')
                counter=counter+1
        else:
            print('Bingo!!!')
            counter=counter+1
            print('您猜了'+str(counter)+'次就答對了')
            break
            