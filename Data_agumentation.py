from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img, img_to_array
import numpy as np
import glob

def agument_images_yes():
    path = r"C:\Users\jgkjh\Downloads\Garbage Project\Garbage\yes\*"
    data_gen = ImageDataGenerator(featurewise_center=True,
                                  samplewise_center=True, rescale=1. / 255,
                                  shear_range=0.2,
                                  zoom_range=0.2,
                                  horizontal_flip=True,
                                  width_shift_range=0.2,
                                  fill_mode='nearest'
                                  )
    for file in glob.glob(path):
        img = load_img(file)
        x = img_to_array(img)
        x = x.reshape((1,)+x.shape)
        i = 0
        for batch in data_gen.flow(x, batch_size=1,
                                   save_to_dir=r'C:\Users\jgkjh\Downloads\Train_agument_images\yes',
                                   save_prefix='Yes',
                                   save_format='.jpg'):
            i = i+1
            if i == 50:
                break

def agument_images_no():
    path = r"C:\Users\jgkjh\Downloads\Garbage Project\Garbage\no\*"
    data_gen = ImageDataGenerator(featurewise_center=True,
                                  samplewise_center=True, rescale=1. / 255,
                                  shear_range=0.2,
                                  zoom_range=0.2,
                                  horizontal_flip=True,
                                  width_shift_range=0.2,
                                  fill_mode='nearest'
                                  )
    for file in glob.glob(path):
        img = load_img(file)
        x = img_to_array(img)
        x = x.reshape((1,)+x.shape)
        i = 0
        for batch in data_gen.flow(x, batch_size=1,
                                   save_to_dir=r'C:\Users\jgkjh\Downloads\Train_agument_images\no',
                                   save_prefix='No',
                                   save_format='.jpg'):
            i = i+1
            if i == 50:
                break

if __name__ == '__main__':
    agument_images_yes()
    agument_images_no()
