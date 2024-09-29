from ft300python.ft300_stream import FT300Stream
import numpy as np
import time
import keyboard

def start_program():
    port = "COM4"
    ft_stream = FT300Stream(port, timeout=1, zero_reset=True)

    last_time = time.perf_counter()
    x = last_time
    t1 = t2 = 0
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    # 修改文件夹目录
    filename1 = r"(your directory)\ft300-sensor\output\TEST\ "
    filename = f"{filename1}{timestamp}.txt"

    with open(filename, "w") as file:
        is_save = False
        while True:
            last_time = time.perf_counter()
            elapsed_time = time.perf_counter() - last_time
            t = last_time - x
            t = round(t, 1)
            t2 = t - t1

            ft_values = ft_stream.get_force_torque()
            ft_values_with_t = np.insert(ft_values, 0, t)

            if t1 == t:
                is_save = False
            elif t1 != t:
                # if t2 > 0.4:
                    is_save = True
                    t1 = t

            if is_save:
                print(
                    f"[{ft_values_with_t[0]:.1f} "
                    f"{ft_values_with_t[1]:.3f} "
                    f"{ft_values_with_t[2]:.3f} "
                    f"{ft_values_with_t[3]:.3f} "
                    f"{ft_values_with_t[4]:.3f} "
                    f"{ft_values_with_t[5]:.3f} "
                    f"{ft_values_with_t[6]:.3f}]"
                )

                np.savetxt(file, [ft_values_with_t], fmt="%0.1f %0.3f %0.3f %0.3f %0.3f %0.3f %0.3f")

            # 检测按下特定键（例如回车键），如果按下了该键，则退出循环
            if keyboard.is_pressed('enter'):
                break

if __name__ == "__main__":
    # 监听按下特定键（例如空格键），当按下该键时执行 start_program() 函数
    print('按下空格键启动')
    keyboard.add_hotkey('space', start_program)
    keyboard.wait()

