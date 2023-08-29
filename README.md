# FT300-sensor
This project can control FT300-sensor to get data in ur5 with python.
## 引言
本项目在ft300python的基础上修改，你可以前往该网站下载源代码：https://github.com/hygradme/ft300python

也可以去robotiq官网下载可视化界面和C++代码：https://robotiq.com/products/ft-300-force-torque-sensor?ref=nav_product_new_button

但是这些项目都不够完善，ft300python和官网的可视化界面可以查看数据流但是无法保存数据，官网C++代码可以保存数据但是不能对数据清零，因此我在ft300python的基础上增加了部分内容。
## 下载
直接下载code，目前所有项目都是通过usb进行rtu连接，后续会增加tcp/ip连接方式，
## 依赖
- pyserial
- pymodbus
- matplotlib
- numpy
- time
- keyboard
- os
- pandas
## 传感器连接
拔下ur机器人机箱内的usb接口并连接到电脑上，此时可以采用robotiq官网的可视化界面进行连接测试。本项目采用的接口为“COM3”，如果连接失败请确保“COM3”接口未被占用。

## 使用
### ft300python
存放使用到的函数。
#### ft300_modbusrtu.py
30hz数据采集函数库，用于测试。
#### ft300_stream.py
100hz数据流采集函数库，本项目主要采用ft300_stream数据流模式。
#### generate.py三个文件
数据生成图像函数库。
包括有：
1. 绘制力和力矩变化图
2. 单独绘制Fx的图
3. 单独绘制Fy的图
4. 单独绘制Fz的图
5. 单独绘制Fx、Fy、Fz的图
6. 单独绘制Mx的图
7. 单独绘制My的图
8. 单独绘制Mz的图
9. 单独绘制Mx、My、Mz的图
10. 绘制所有图像
### output
存放输出的数据文件及图像。
#### TEST
预先提供的几组用于测试的数据。
```
0.5 -0.110 -0.130 0.000 -0.005 0.001 0.003
1.0 -0.080 -0.140 -0.060 -0.004 0.000 0.001
1.5 -0.110 -0.160 -0.030 -0.003 0.002 0.001
2.0 -0.090 -0.040 0.020 -0.001 0.000 0.001
2.5 -0.070 -0.300 0.180 -0.021 0.011 0.004
3.0 -0.150 -0.050 0.010 -0.002 0.001 0.001
3.5 -0.080 -0.590 0.320 0.014 0.042 0.000
4.0 -0.120 -0.420 0.270 0.012 0.026 0.003
```
### run
存放运行的脚本。
#### run_ft300_modbusrtu.py
运行30hz数据采集，仅测试，不保存数据。
#### run_ft300_stream.py
1. 将获得的数据以时间作为文件名保存在output\TEST中，**需要修改文件保存地址**。
```
  # 修改文件夹目录
  filename1 = r"(your directory)\ft300-sensor\output\TEST\ "
```
2. 原数据流以100hz获取数据，在脚本中添加计时器使得每0.5秒获取一次数据。
3. 原数据流输出数组仅有数据本身，在数组第一列增加时间，便于数据统计。
4. 脚本运行后，按下空格键启动，按下回车键停止。
#### run_generate.py
1. **修改文件保存地址**，获取 output 文件夹中最后一个文件的文件中的数据，即该文件中的最新数据，并自行选择需要绘制的图像。
2. 根据generate.py选择需要的绘制图像函数的数字并输入。
#### run_save.py
1.  **修改文件保存地址**，输入output文件夹下子文件夹的目录，如TEST  
``` 
    path = input("请输入文件夹路径：")
    # 修改文件夹目录
    mydirectory = r"(your directory)\ft300-sensor\output"
```
2.  获取子文件夹所有数据文件的所有数据，生成所有图像，可在此处更改为需要的图像函数名
```
gn.plot_all(data, showcfg)
```
3. 在子文件夹下新建文件夹fig，将所有图像保存在fig。
