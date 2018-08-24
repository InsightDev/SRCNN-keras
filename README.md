# SRCNN-keras

* Ubuntu 18.04.1 LTS
* python2.7
* tensorflow_gpu-1.10.0

### Paper

* [Image Super-Resolution Using Deep Convolutional Networks](https://arxiv.org/abs/1501.00092)



### Train

### Result

![Image text](https://github.com/InsightDev/SRCNN-keras/blob/master/butterfly_GT.png)


### Performance

* PSNR Only

| Dataset | Scale | Bicubic | SRCNN-paper | SRCNN-keras |
| :------ | :---- | :------ | :---------- | :---------- |
| Set5    | 2x    | 33.66   | 36.66       | 33.10 ?     |
|         | 3x    | 30.39   | 32.75       |             |
|         | 4x    | 28.42   | 30.49       | 33.10 ?     |
| Set14   | 2x    | 30.23   | 32.45       |             |
|         | 3x    | 27.54   | 29.30       |             |
|         | 4x    | 26.00   | 27.50       | 29.45 ?     |


### Other

* https://github.com/InsightDev/SRDenseNet-keras  
