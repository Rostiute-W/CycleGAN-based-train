## 基于CycleGAN对抗生成网络训练自己的数据集

#### <span style="color:red;">仅支持含有src和dst的数据集</span>

### step 1：训练数据生成

#### 首先准备自己的数据集以及测试样本，数据集格式如下：

#### root

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- - - -label1

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- - - -label2

#### 测试样本：将需要测试的图像放入test-sample(可自定义)文件夹，请注意需要的是图像文件夹，而不是单张图像
#### 准备好后运行 main.py 文件，只需要设置root、label1、label2等参数（test=False），详情请查看具体文件

### step 2：下载开源项目CycleGAN

#### 方式一：git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git

#### 方式二：百度网盘：pytorch-CycleGAN-and-pix2pix

#### 链接: https://pan.baidu.com/s/1WC-kEonwm7bFujO72GZAcQ 提取码: jsw2

### step 3：配置训练环境

#### 将pytorch-CycleGAN-and-pix2pix放到自己的环境中，在终端打开该文件

- 输入：pip install -r ./pytorch-CycleGAN-and-pix2pix/requirements.txt

#### 其中 ./pytorch-CycleGAN-and-pix2pix/requirements.txt是requirements.txt 文件所在路径，不会的直接复制该文件的绝对路径就好

### step 4：开始训练
#### 在终端打开该项目文件

- 输入：python ./pytorch-CycleGAN-and-pix2pix/train.py --dataroot ./dataset --name dehaze_cyclegan --model cycle_gan
#### --name 是模型名字，可自定义，修改后一定要与测试时的name一致

#### 运行过程中如果出现 <span style="color:red;">“OSError: [WinError 1455] 页面文件太小，无法完成操作。”</span> 等报错是由于当前环境所在磁盘的虚拟内存不足导致的，解决方式请自行查阅

### step 5：模型测试
### 进行测试之前准备好自己的测试样本test-sample

- 终端输入：cp ./checkpoints/dehaze_cyclegan/latest_net_G_A.pth ./checkpoints/dehaze_cyclegan/latest_net_G.pth
- python ./pytorch-CycleGAN-and-pix2pix/test.py --dataroot ./test-sample --name dehaze_cyclegan --model test --no_dropout --direction AtoB
#### --dataroot 是测试样本，可以自己调整路径；请查看name是否与训练的一致，不一致请修改

### step 6：可视化结果
#### 运行main.py文件，需要设置3个参数：test、test_data_path、results_path(test=True)，详情请查看具体文件
