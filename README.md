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

* an upscaling factor of 4  

| Dataset | Bicubic | SRCNN-paper | SRCNN-keras |
| :------ | :------ | :---------- | :---------- |
| Set5    | 28.42   | 30.49       | 33.10 ?     |
| Set14   | 26.00   | 27.50       | 29.45 ?     |
| B100    | *1 *    | 00.00       | 00.00 ?     |


### Other

* https://github.com/InsightDev/SRDenseNet-keras  
