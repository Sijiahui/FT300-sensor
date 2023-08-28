from ft300python import generate as gn
import os
import pandas as pd

def is_txt_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.txt'

if __name__ == '__main__':
    # 获取 output 文件夹中最后一个文件的文件名
    # 修改文件夹目录
    mydirectory = r"(your directory)\ft300-sensor\output"
    path = input("请输入文件夹： ")
    directory = os.path.join(mydirectory, path)
    txt_files = [file for file in os.listdir(directory) if is_txt_file(file)]

    if len(txt_files) > 0:
        last_file = sorted(txt_files)[-1]
    else:
        print("该文件夹下没有txt文件")
        exit()

    # 使用 Pandas 读取最后一个文件的数据
    filename = os.path.join(directory, last_file)
    df = pd.read_csv(filename, header=0, delimiter=" ")
    print(filename)
    # 取出所有数据，并转换为 NumPy 数组
    data = df.iloc[:, :7].values
    while True:

        choice = input(
            "请选择要运行的函数：\n1. plot_FandM\n2. plot_Fx\n3. plot_Fy\n4. plot_Fz\n5. plot_Fxyz\n6. plot_Mx\n7. plot_My\n8. plot_Mz\n9. plot_Mxyz\n10. plot_all\n11. 退出\n")
        if choice == "11":
            break
        gn.choice_plot(choice, data)



