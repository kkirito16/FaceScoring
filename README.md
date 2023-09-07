# FaceScoring环境搭建

**核心环境：**

- face-recognition-1.0.0
- keras-2.1.2

**在anaconda上：**

```shell
conda create -n fc python=3.7
conda activate fc
conda install -c conda-forge cmake
pip install D:\Download\dlib-19.19.0-cp37-cp37m-win_amd64.whl
pip install face-recognition==1.0.0
pip install opencv-python
pip install keras==2.1.2
pip install protobuf==3.20.0
```

注意第4个D:\Download\应当改成自己文件对应的存储位置

因为face-recognition包非常难装，这里就采用了本地安装部分依赖包的方式

**在pycharm中：**

将报错中的decode（utf-8）删除即可

![1694069052480](https://cdn.jsdelivr.net/gh/kkirito16/ImgPicGo/img/1694069052480.png)