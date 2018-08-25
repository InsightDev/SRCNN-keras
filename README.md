# SRCNN-keras

* [Image Super-Resolution Using Deep Convolutional Networks](https://arxiv.org/abs/1501.00092)


### Training

* Ubuntu 18.04.1 LTS
* python2.7
* tensorflow_gpu-1.10.0


### Result

Origin - Bicubic(resize with cv2) - SRCNN
![Image text](https://github.com/InsightDev/SRCNN-keras/blob/master/src/data/butterfly_GT.png)  
Origin - Bicubic(resize with PIL) - SRCNN
![Image text](https://github.com/InsightDev/SRCNN-keras/blob/master/src/data/butterfly_GT.bmp)  


### Performance

* PSNR, training on the 91 images. n1=?, n2=?

| Dataset | Scale | Bicubic | SRCNN-paper | SRCNN-keras |
| :------ | :---- | :------ | :---------- | :---------- |
| Set5    | 2x    | 33.66   | 36.66       | 34.05 ?     |
|         | 3x    | 30.39   | 32.75       |             |
|         | 4x    | 28.42   | 30.49       |             |
| Set14   | 2x    | 30.23   | 32.45       | 30.19 ?     |
|         | 3x    | 27.54   | 29.30       |             |
|         | 4x    | 26.00   | 27.50       |             |

### Trick
The resize function in python is different from Matlab. So far, only using the bicubic of Matlab could achieve the best PSNR score, because it has anti-aliasing function. Please take a look at this [link](https://www.reddit.com/r/MachineLearning/comments/6vdo51/p_matlab_bicubic_imresize_implemented_in_python).  
Origin - Bicubic(resize with cv2) - Bicubic(resize with PIL)  


### Other

* https://github.com/InsightDev/SRDenseNet-keras  
