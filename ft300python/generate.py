import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 表区域上移动鼠标来显示折线图数据点信息时不能显示负数
# plt.rcParams['axes.unicode_minus'] = False

# # 获取 output 文件夹中最后一个文件的文件名
# directory = r"C:\Users\sjh\OneDrive\桌面\ur5\ft300python-main\ft300python-main\output"
# last_file = sorted(os.listdir(directory))[-1]
#
# # 使用 Pandas 读取最后一个文件的数据
# filename = os.path.join(directory, last_file)
# df = pd.read_csv(filename, header=0, delimiter=" ")
#
# # 取出所有数据，并转换为 NumPy 数组
# data = df.iloc[:, :7].values


showcfg = 1

# 设置中文字符的字体，否则不能显示中文
font_path = "C:/Windows/Fonts/simsun.ttc"  # 这里使用宋体字体
font_prop = fm.FontProperties(fname=font_path)


# 分别显示力和力矩
def plot_FandM(data, showcfg):
    # 将数组的第一列作为横坐标，将其余列作为纵坐标
    x = data[:, 0]
    y1 = data[:, 1:4]
    y2 = data[:, 4:7]

    # 创建 Figure 和 Axes 对象 设置横1列2 长15宽6
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    # 绘制三维力变化图
    axs[0].plot(x, y1)
    axs[0].set_xlabel("时间/s", fontproperties=font_prop)
    axs[0].set_ylabel("力/N", fontproperties=font_prop)
    axs[0].set_title("三维力变化图", fontproperties=font_prop)
    axs[0].legend(["Fx", "Fy", "Fz"], prop=font_prop)

    # 绘制三维力矩变化图
    axs[1].plot(x, y2)
    axs[1].set_xlabel("时间/s", fontproperties=font_prop)
    axs[1].set_ylabel("力矩/N·m", fontproperties=font_prop)
    axs[1].set_title("三维力矩变化图", fontproperties=font_prop)
    axs[1].legend(["Mx", "My", "Mz"], prop=font_prop)

    # 设置两图间距
    plt.subplots_adjust(hspace=0.5)

    if showcfg == 1:
        plt.show()

# 单独绘制Fx、Fy、Fz的图
def plot_Fxyz(data, showcfg):
    x = data[:, 0]
    yFx = data[:, 1:2]
    yFy = data[:, 2:3]
    yFz = data[:, 3:4]

    # 创建 Figure 和 Axes 对象 设置横1列3 长15宽6
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(20, 6))

    # 绘制三维力变化图
    axs[0].plot(x, yFx)
    axs[0].set_xlabel("时间/s", fontproperties=font_prop)
    axs[0].set_ylabel("力/N", fontproperties=font_prop)
    axs[0].set_title("Fx变化图", fontproperties=font_prop)
    axs[0].legend(["Fx"], prop=font_prop)

    axs[1].plot(x, yFy)
    axs[1].set_xlabel("时间/s", fontproperties=font_prop)
    axs[1].set_ylabel("力/N", fontproperties=font_prop)
    axs[1].set_title("Fy变化图", fontproperties=font_prop)
    axs[1].legend(["Fy"], prop=font_prop)

    axs[2].plot(x, yFz)
    axs[2].set_xlabel("时间/s", fontproperties=font_prop)
    axs[2].set_ylabel("力/N", fontproperties=font_prop)
    axs[2].set_title("Fz变化图", fontproperties=font_prop)
    axs[2].legend(["Fz"], prop=font_prop)

    # 设置两图间距
    plt.subplots_adjust(hspace=0.5)

    if showcfg == 1:
        plt.show()


# 单独绘制Mx、My、Mz的图
def plot_Mxyz(data, showcfg):
    x = data[:, 0]
    yMx = data[:, 4:5]
    yMy = data[:, 5:6]
    yMz = data[:, 6:7]

    # 创建 Figure 和 Axes 对象 设置横1列3 长15宽6
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(20, 6))

    # 绘制三维力矩变化图
    axs[0].plot(x, yMx)
    axs[0].set_xlabel("时间/s", fontproperties=font_prop)
    axs[0].set_ylabel("力矩/N·m", fontproperties=font_prop)
    axs[0].set_title("Mx变化图", fontproperties=font_prop)
    axs[0].legend(["Mx"], prop=font_prop)

    axs[1].plot(x, yMy)
    axs[1].set_xlabel("时间/s", fontproperties=font_prop)
    axs[1].set_ylabel("力矩/N·m", fontproperties=font_prop)
    axs[1].set_title("My变化图", fontproperties=font_prop)
    axs[1].legend(["My"], prop=font_prop)

    axs[2].plot(x, yMz)
    axs[2].set_xlabel("时间/s", fontproperties=font_prop)
    axs[2].set_ylabel("力矩/N·m", fontproperties=font_prop)
    axs[2].set_title("Mz变化图", fontproperties=font_prop)
    axs[2].legend(["Mz"], prop=font_prop)

    # 设置两图间距
    plt.subplots_adjust(hspace=0.5)

    if showcfg == 1:
        plt.show()

# 单独绘制Fx的折线图
def plot_Fx(data, showcfg):
    x = data[:, 0]
    yFx = data[:, 1:2]

    # 创建 Figure 和 Axes 对象 设置横1列1 长8宽6
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))

    # 绘制 Fx 变化图
    ax.plot(x, yFx)
    ax.set_xlabel("时间/s", fontproperties=font_prop)
    ax.set_ylabel("力/N", fontproperties=font_prop)
    ax.set_title("Fx变化图", fontproperties=font_prop)
    ax.legend(["Fx"], prop=font_prop)

    if showcfg == 1:
        plt.show()


# 单独绘制Fy的折线图
def plot_Fy(data, showcfg):
    x = data[:, 0]
    yFx = data[:, 2:3]

    # 创建 Figure 和 Axes 对象 设置横1列1 长8宽6
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))

    # 绘制 Fx 变化图
    ax.plot(x, yFx)
    ax.set_xlabel("时间/s", fontproperties=font_prop)
    ax.set_ylabel("力/N", fontproperties=font_prop)
    ax.set_title("Fy变化图", fontproperties=font_prop)
    ax.legend(["Fy"], prop=font_prop)

    if showcfg == 1:
        plt.show()

# 单独绘制Fz的折线图
def plot_Fz(data, showcfg):
    x = data[:, 0]
    yFz = data[:, 3:4]

    # 创建 Figure 和 Axes 对象 设置横1列1 长8宽6
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))

    # 绘制 Fx 变化图
    ax.plot(x, yFz)
    ax.set_xlabel("时间/s", fontproperties=font_prop)
    ax.set_ylabel("力/N", fontproperties=font_prop)
    ax.set_title("Fz变化图", fontproperties=font_prop)
    ax.legend(["Fz"], prop=font_prop)

    if showcfg == 1:
        plt.show()

# 单独绘制Mx的折线图
def plot_Mx(data, showcfg):
    x = data[:, 0]
    yMx = data[:, 4:5]

    # 创建 Figure 和 Axes 对象 设置横1列1 长8宽6
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))

    # 绘制 Fx 变化图
    ax.plot(x, yMx)
    ax.set_xlabel("时间/s", fontproperties=font_prop)
    ax.set_ylabel("力矩/N·m", fontproperties=font_prop)
    ax.set_title("Mx变化图", fontproperties=font_prop)
    ax.legend(["Mx"], prop=font_prop)

    if showcfg == 1:
        plt.show()

# 单独绘制My的折线图
def plot_My(data, showcfg):
    x = data[:, 0]
    yMy = data[:, 5:6]

    # 创建 Figure 和 Axes 对象 设置横1列1 长8宽6
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))

    # 绘制 Fx 变化图
    ax.plot(x, yMy)
    ax.set_xlabel("时间/s", fontproperties=font_prop)
    ax.set_ylabel("力矩/N·m", fontproperties=font_prop)
    ax.set_title("My变化图", fontproperties=font_prop)
    ax.legend(["My"], prop=font_prop)

    if showcfg == 1:
        plt.show()


# 单独绘制Mz的折线图
def plot_Mz(data, showcfg):
    x = data[:, 0]
    yMz = data[:, 4:5]

    # 创建 Figure 和 Axes 对象 设置横1列1 长8宽6
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))

    # 绘制 Fx 变化图
    ax.plot(x, yMz)
    ax.set_xlabel("时间/s", fontproperties=font_prop)
    ax.set_ylabel("力矩/N·m", fontproperties=font_prop)
    ax.set_title("Mz变化图", fontproperties=font_prop)
    ax.legend(["Mz"], prop=font_prop)
    if showcfg == 1:
        plt.show()

def plot_all(data, showcfg):
    x = data[:, 0]
    yFx = data[:, 1:2]
    yFy = data[:, 2:3]
    yFz = data[:, 3:4]
    yMx = data[:, 4:5]
    yMy = data[:, 5:6]
    yMz = data[:, 6:7]

    # 创建 Figure 和 Axes 对象 设置横2列3 长20宽12
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(20, 12))

    # 绘制三维力变化图
    axs[0, 0].plot(x, yFx)
    axs[0, 0].set_xlabel("时间/s", fontproperties=font_prop)
    axs[0, 0].set_ylabel("力/N", fontproperties=font_prop)
    axs[0, 0].set_title("Fx变化图", fontproperties=font_prop)
    axs[0, 0].legend(["Fx"], prop=font_prop)

    axs[0, 1].plot(x, yFy)
    axs[0, 1].set_xlabel("时间/s", fontproperties=font_prop)
    axs[0, 1].set_ylabel("力/N", fontproperties=font_prop)
    axs[0, 1].set_title("Fy变化图", fontproperties=font_prop)
    axs[0, 1].legend(["Fy"], prop=font_prop)

    axs[0, 2].plot(x, yFz)
    axs[0, 2].set_xlabel("时间/s", fontproperties=font_prop)
    axs[0, 2].set_ylabel("力/N", fontproperties=font_prop)
    axs[0, 2].set_title("Fz变化图", fontproperties=font_prop)
    axs[0, 2].legend(["Fz"], prop=font_prop)

    # 绘制三维力矩变化图
    axs[1, 0].plot(x, yMx)
    axs[1, 0].set_xlabel("时间/s", fontproperties=font_prop)
    axs[1, 0].set_ylabel("力矩/N·m", fontproperties=font_prop)
    axs[1, 0].set_title("Mx变化图", fontproperties=font_prop)
    axs[1, 0].legend(["Mx"], prop=font_prop)

    axs[1, 1].plot(x, yMy)
    axs[1, 1].set_xlabel("时间/s", fontproperties=font_prop)
    axs[1, 1].set_ylabel("力矩/N·m", fontproperties=font_prop)
    axs[1, 1].set_title("My变化图", fontproperties=font_prop)
    axs[1, 1].legend(["My"], prop=font_prop)

    axs[1, 2].plot(x, yMz)
    axs[1, 2].set_xlabel("时间/s", fontproperties=font_prop)
    axs[1, 2].set_ylabel("力矩/N·m", fontproperties=font_prop)
    axs[1, 2].set_title("Mz变化图", fontproperties=font_prop)
    axs[1, 2].legend(["Mz"], prop=font_prop)

    # 设置两图间距
    plt.subplots_adjust(hspace=0.5)
    if showcfg == 1:
        plt.show()



def choice_plot(choice,data):


    if choice == "1":
        plot_FandM(data, showcfg)
    elif choice == "2":
        plot_Fx(data, showcfg)
    elif choice == "3":
        plot_Fy(data, showcfg)
    elif choice == "4":
        plot_Fz(data, showcfg)
    elif choice == "5":
        plot_Fxyz(data, showcfg)
    elif choice == "6":
        plot_Mx(data, showcfg)
    elif choice == "7":
        plot_My(data, showcfg)
    elif choice == "8":
        plot_Mz(data, showcfg)
    elif choice == "9":
        plot_Mxyz(data, showcfg)
    elif choice == "10":
        plot_all(data, showcfg)
    else:
        print("无效的选择！")




# 调用函数绘制力和力矩折线图
# plot_FandM()
# plot_F()
# plot_M()
# plot_Fx()
# plot_Fy()
# plot_Fz()
# plot_Mx()
# plot_My()
# plot_Mz()
