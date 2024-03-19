'''
Hello Worls!
This project is intended to monitor network traffic and display it in chart format.
'''
from getFiles import Networking


if __name__ == '__main__':
    net = Networking()
    # print(os.getlogin())
    net.filter_block()
    # net.site_ping_data()