from Xlib import display, X
from PIL import Image #PIL
import time
from fastai.conv_learner import *
from fastai.dataset import *
from fastai.plots import *
import pyautogui
 def main():
     os.chdir('/home/shaaran/PycharmProjects/dino_AI/')
    PATH = '/home/shaaran/PycharmProjects/dino_AI'
    sz = 224
    arch = resnet34
    tfms = tfms_from_model(sz=sz, f_model=arch)
    data = ImageClassifierData.from_paths(PATH,tfms=tfms)
    print(data.classes)
    learn = ConvLearner.pretrained(arch, data, precompute=True)
    print('loading requirements......')
    print('This has been made by shaaran alias devshaaran, if you are using this code anywhere for research or educational purposes, please give reference.ENJOY!')
    learn.precompute = False
    learn.fit(1e-1, 1)
    learn.load('all')
    print('loading done !')
    while True:
        st_time = time.time()
        W,H = 630,150
        dsp = display.Display()
        root = dsp.screen().root
        raw = root.get_image(163,169, W,H, X.ZPixmap, 0xffffffff,)
        image = Image.frombytes("RGB", (W, H), raw.data, "raw", "BGRX")
        image.save('/home/shaaran/PycharmProjects/dino_AI/0.png')
        time.sleep(0.2)
        try:
            trn_tfms, val_tfms = tfms_from_model(arch, sz)
            im = val_tfms(open_image('/home/shaaran/PycharmProjects/dino_AI/0.png'))
            learn.precompute = False
            preds = learn.predict_array(im[None])
            print(data.classes[np.argmax(preds)])
        except Exception as e:
            print(e)
 def pointer_check():
    while True:
        x,y = pyautogui.position()
        print(x,',',y)
 def im_check():
     st_time = time.time()
    W, H = 630, 150
    dsp = display.Display()
    root = dsp.screen().root
    raw = root.get_image(163, 169, W, H, X.ZPixmap, 0xffffffff, )
    image = Image.frombytes("RGB", (W, H), raw.data, "raw", "BGRX")
    image.save('/home/shaaran/PycharmProjects/dino_AI/0.png')
 main()
