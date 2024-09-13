# main.py

import os
import shutil
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
from tqdm import tqdm

# ----------------------训练数据路径-----------------------#
#   仅支持包含src和dst的数据集（图像对）
# -------------------------------------------------------#
root = r'O-HAZY NTIRE 2018'
# --------------------------------------------------------#
#       label1:src的路径名  |  label2:dst的路径名
# --------------------------------------------------------#
label1 = 'GT'
label2 = 'hazy'
# -------------------------生成图像可视化-------------------------#
#   ！！！ 在训练和测试均完成后进行结果检查时仅可设置为True，否则报错  ！！！
#   该部分只是对结果的可视化，预测阶段请查看README
# -------------------------------------------------------------#
test = False
# ------------------------测试样本------------------------------#
test_data_path = './test-sample'
# ------------------------测试结果图像保存路径---------------------#
# ！！！   里面是已经得到的测试结果和原图     ！！！
# -------------------------------------------------------------#
results_path = './results/dehaze_cyclegan/test_latest/images/'


def make_data(src_path, dst_path, label):
    src_path = src_path + f'/{label}/'
    image_files = [f for f in os.listdir(src_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
    
    with tqdm(total=len(image_files)) as pbar:
        for filename in image_files:
            file_path = os.path.join(src_path, filename)
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                image = Image.open(file_path)
                target_file = os.path.join(dst_path, filename)
                image.save(target_file)
                
            pbar.update(1)



if __name__ == '__main__':
    if not test:
        # -------------------创建CycleGAN的训练数据路径-----------------------#
        if not os.path.exists('dataset'):
            os.makedirs('dataset')
        if not os.path.exists('dataset/trainA'):
            os.makedirs('dataset/trainA')
        if not os.path.exists('dataset/trainB'):
            os.makedirs('dataset/trainB')

        # --------------------------检查图像对数量----------------------------#
        num_images = len(os.listdir(root + f'/{label1}/'))
        idx = np.arange(1, num_images + 1)
        print(f'查找到{num_images}个图像对')

        make_data(root, 'dataset/trainA/', label1)
        make_data(root, 'dataset/trainB/', label2)

    # ----------------------可视化阶段-----------------------------------#
    else:
        for f in os.listdir(test_data_path):
            fake = f.split('.')[0] + '_fake.png'
            real = f.split('.')[0] + '_real.png'

            fig = plt.figure()
            ax = plt.subplot(1, 2, 1)
            img1 = Image.open(results_path + real)
            plt.imshow(img1)

            ax = plt.subplot(1, 2, 2)
            img2 = Image.open(results_path + fake)
            plt.imshow(img2)

            plt.show()
