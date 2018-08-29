# SRCNN-keras

* [Image Super-Resolution Using Deep Convolutional Networks](https://arxiv.org/abs/1501.00092)


### Training

* Ubuntu 18.04.1 LTS
* python2.7
* tensorflow_gpu-1.10.0

![Image text](https://github.com/InsightDev/SRCNN-keras/blob/master/src/data/loss.png)  

### Result

Origin - Bicubic(resize with cv2) - SRCNN
![Image text](https://github.com/InsightDev/SRCNN-keras/blob/master/src/data/butterfly_GT.png)  
Origin - Bicubic(resize with PIL) - SRCNN
![Image text](https://github.com/InsightDev/SRCNN-keras/blob/master/src/data/butterfly_GT.bmp)  


### Performance

* PSNR, training on the 91 images. f1 = 9, f2 = 5, f3 = 5, n1 = 64, n2=32  

| Dataset | Scale | Bicubic | SRCNN-paper | SRCNN-keras |
| :------ | :---- | :------ | :---------- | :---------- |
| Set5    | 2x    | 33.66   | 36.66       | 36.285788   |
|         | 3x    | 30.39   | 32.75       |             |
|         | 4x    | 28.42   | 30.49       |             |
| Set14   | 2x    | 30.23   | 32.45       | 32.61(13)   |
|         | 3x    | 27.54   | 29.30       |             |
|         | 4x    | 26.00   | 27.50       |             |

The result is lower then the paper, because the SRCNN-paper is trained on ImageNet, and it use matlab's imresize.

"We adopt the model with good performance-speed trade-off: a three-layer network with f1 = 9, f2 = 5, f3 = 5, n1 = 64, and n2 = 32 trained on the ImageNet. For each upscaling factor, we train a specific network for that factor."

### Trick
The resize function in python is different from Matlab. So far, only using the bicubic of Matlab could achieve the best PSNR score, because it has anti-aliasing function. Please take a look at this [link](https://www.reddit.com/r/MachineLearning/comments/6vdo51/p_matlab_bicubic_imresize_implemented_in_python).  
Origin - Bicubic(resize with cv2) - Bicubic(resize with PIL)  


### Other

* https://github.com/InsightDev/SRDenseNet-keras  
