import socket


class FT300_TCP:
    def __init__(self, host, port, zero_reset=True):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

        # # read one-time data to determine format
        # data = self.sock.recv(1024)

        self.zero_force_torque = [0, 0, 0, 0, 0, 0]
        if zero_reset:
            self.zero_force_torque = self.get_force_torque_raw()

    def get_force_torque_raw(self):
        """get raw force and torque value without zero reset"""
        coef_list = [100, 100, 100, 1000, 1000, 1000]
        data = self.sock.recv(1024)
        raw_bytes = bytearray(data)
        force_torque = [int.from_bytes(raw_bytes[i * 2: i * 2 + 2], byteorder='little', signed=True) / coef_list[i] for
                        i in range(0, 6)]
        return force_torque

    def reset_zero_force_torque(self):
        """reset zero force torque values with current force torque"""
        self.zero_force_torque = self.get_force_torque_raw()

    def get_force_torque(self):
        """get force and torque value based on zero reset ft"""
        return [ft - ft_zero for ft, ft_zero in zip(self.get_force_torque_raw(), self.zero_force_torque)]


ft = FT300_TCP('192.168.1.12', 63351)  # specify the IP address and port of FT300
while True:
    ft_values_with_t = ft.get_force_torque()
    # print(force_torque)
    print(
        f"[{ft_values_with_t[0]:.1f} "
        f"{ft_values_with_t[1]:.3f} "
        f"{ft_values_with_t[2]:.3f} "
        f"{ft_values_with_t[3]:.3f} "
        f"{ft_values_with_t[4]:.3f} "
        f"{ft_values_with_t[5]:.3f}]"
    )


