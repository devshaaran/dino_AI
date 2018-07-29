import pyautogui
import os
import random as rand
from time import sleep
import keyboard
import torch
if os.path.exists(os.getcwd()+'\\dino_AI'):
    pass
else:
    os.mkdir(os.getcwd()+'\\dino_AI')
    os.mkdir(os.getcwd()+'\\dino_AI'+'\\jump')
    os.mkdir(os.getcwd()+'\\dino_AI'+'\\duck')
    os.mkdir(os.getcwd()+'\\dino_AI'+'\\nothing')
    os.mkdir(os.getcwd()+'\\dino_AI'+'\\space')

jump_path = os.getcwd()+'\\dino_AI'+'\\jump'+'\\'
duck_path = os.getcwd()+'\\dino_AI'+'\\duck'+'\\'
nothing_path = os.getcwd()+'\\dino_AI'+'\\nothing'+'\\'
space_path = os.getcwd()+'\\dino_AI'+'\\space'+'\\'

def collect_data():
    while True:
        img = pyautogui.screenshot(region=(66,168,858,213))
        img_name_number_1 = rand.randint(0,999999999999)
        some_text = ['a','b','c','d','e','f','g','h','i','j','k']
        img_name_number_2 = rand.randint(0,99)
        chose_text_3 = rand.choice(some_text)
        final_name = str(img_name_number_1)+chose_text_3+str(img_name_number_2)+'.png'

        if keyboard.is_pressed('up arrow'):
            img.save(jump_path+final_name)
            sleep(0.6)
            print(final_name)
        elif keyboard.is_pressed('down arrow'):
            img.save(duck_path+final_name)
            sleep(0.3)
            print(final_name)
        elif keyboard.is_pressed('space'):
            img.save(space_path+final_name)
            sleep(0.3)
            print(final_name)
        else:
            try:
                #img.save(nothing_path+final_name)
                print('nothing')
            except Exception as e :
                print(e)

def split_data():
    primary_loc_list = os.listdir('C:\\Users\Acer\PycharmProjects\om\\dino_AI')
    primary_loc = 'C:\\Users\Acer\PycharmProjects\om\\dino_AI'

    if os.path.exists(primary_loc + '\\' + 'train'):
        pass
    else:
        os.mkdir(primary_loc+'\\'+'train')
    if os.path.exists(primary_loc + '\\' + 'valid'):
        pass
    else:
        os.mkdir(primary_loc+'\\'+'valid')



    for i in primary_loc_list:
        if i == 'train' or i =='valid':
            pass
        else:
            count = 0
            secondary_loc_list = os.listdir(primary_loc+'\\'+i)
            secondary_loc = primary_loc + '\\' + i
            amount_of_data = len(secondary_loc_list)
            if os.path.exists(primary_loc + '\\' + 'train' + '\\' + i):
                pass
            else:
                os.mkdir(primary_loc + '\\' + 'train' + '\\' + i)
            if os.path.exists(primary_loc + '\\' + 'valid' + '\\' + i):
                pass
            else:
                os.mkdir(primary_loc + '\\' + 'valid' + '\\' + i)



            for j in secondary_loc_list:
                if count<(amount_of_data*0.25):
                    os.rename(secondary_loc+'\\'+j,primary_loc+'\\'+'valid'+'\\'+i+'\\'+j)
                else:
                    os.rename(secondary_loc + '\\' + j, primary_loc + '\\' + 'train' + '\\' + i + '\\' + j)
                count += 1

def play_game():
    from keras.models import load_model
    import cv2
    import numpy as np
    import time

    model = load_model('C:\\Users\\Acer\\PycharmProjects\\om\\dino_AI\\model\\all.h5')

    start = time.time()

    def predict():
        img = pyautogui.screenshot(region=(66, 168, 858, 213))
        # model prediction
        y_prob = model.predict(img)
        prediction = y_prob.argmax(axis=-1)
        print(prediction)


    predict()


play_game()

