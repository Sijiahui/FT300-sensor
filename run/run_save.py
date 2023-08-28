import os
from ft300python import generate as gn
import pandas as pd
import matplotlib.pyplot as plt


def is_txt_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.txt'


if __name__ == '__main__':

    path = input("请输入文件夹路径：")
    # 修改文件夹目录
    mydirectory = r"(your directory)\ft300-sensor\output"
    # 获取目录下所有文件
    directory = os.path.join(mydirectory, path)
    all_files = os.listdir(directory)
    i = 0
    showcfg = 0
    save_dir = os.path.join(directory, "fig")
    os.makedirs(save_dir, exist_ok=True)
    # 遍历每个文件`

    for file in all_files:
        if is_txt_file(file):
            # 构建文件路径
            filename = os.path.join(directory, file)

            # 使用 Pandas 读取文件数据
            df = pd.read_csv(filename, header=0, delimiter=" ")

            # 取出所有数据，并转换为 NumPy 数组
            data = df.iloc[:, :7].values

            # 生成唯一的文件名
            save_filename = f'chart_{i + 1}.png'
            # 构建保存路径
            save_path = os.path.join(save_dir, save_filename)

            gn.plot_all(data, showcfg)
            plt.savefig(save_path)
            plt.clf()

            i += 1
