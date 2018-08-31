# SRCNN-keras

* [Image Super-Resolution Using Deep Convolutional Networks](https://arxiv.org/abs/1501.00092)

* Ubuntu 18.04.1 LTS
* python2.7
* tensorflow_gpu-1.10.0

### Training

SRCNN-keras is training on the 91 images. I use 91 as the batch_size, just random crop from each image. An epoch has 100 steps, and 1000 epochs is trained, 100k steps. matlab's imresize(bicubic) is used. It takes about an hour to train the model on my GTX1060 6G GPU.

![Image text](https://github.com/InsightDev/SRCNN-keras/blob/master/SRCNN/docs/loss.png)  

### Result

Origin - Bicubic(resize with cv2) - SRCNN
![Image text](https://github.com/InsightDev/SRCNN-keras/blob/master/SRCNN/docs/butterfly_GT.png)  
Origin - Bicubic(resize with PIL) - SRCNN
![Image text](https://github.com/InsightDev/SRCNN-keras/blob/master/SRCNN/docs/butterfly_GT.bmp)  


### Performance

* PSNR, training on the 91 images. f1 = 9, f2 = 5, f3 = 5, n1 = 64, n2=32  

| Dataset | Scale | Bicubic | SRCNN-paper | SRCNN-keras |
| :------ | :---- | :------ | :---------- | :---------- |
| Set5    | 2x    | 33.66   | 36.66       | 36.36       |
|         | 3x    | 30.39   | 32.75       |             |
|         | 4x    | 28.42   | 30.49       |             |
| Set14   | 2x    | 30.23   | 32.45       | 32.265233   |
|         | 3x    | 27.54   | 29.30       |             |
|         | 4x    | 26.00   | 27.50       |             |

The result is lower then the paper, because the SRCNN-paper is trained on ImageNet.

>We adopt the model with good performance-speed trade-off: a three-layer network with f1 = 9, f2 = 5, f3 = 5, n1 = 64, and n2 = 32 trained on the ImageNet. For each upscaling factor, we train a specific network for that factor.

### Trick
The resize function in python is different from Matlab. So far, only using the bicubic of Matlab could achieve the best PSNR score, because it has anti-aliasing function. Please take a look at this [link](https://www.reddit.com/r/MachineLearning/comments/6vdo51/p_matlab_bicubic_imresize_implemented_in_python).  
Origin - Bicubic(resize with cv2) - Bicubic(resize with PIL)  

