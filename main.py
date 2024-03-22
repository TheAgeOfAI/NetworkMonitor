'''
Hello Worls!
This project is intended to monitor network traffic and display it in chart format.
'''
from deprecated import Deprecated
from archiveIt import Archive

class NetHandler(Deprecated):
    def __init__(self):
        super(Deprecated, self).__init__()
        self.arc = Archive()

    def make_data(self):
        print("Executing Your command ...")
        self.ping_to_file()
        print("Execution Done.")

    def format_data(self):
        print("Makings CSV files.")
        self.read_filter_block()
        print("CSV Processes completed")
        print("Removing txt files from storage.")
        self.arc.clear_txt()
        print("Text Files cleared.")

if __name__ == '__main__':
    net = NetHandler()
    print("Please choose wisely ")
    print("1. Make data using ping.")
    print("2. Convert to csv file.")
    print("3. Archive CSV data")
    print("Any other to quit the program.")
    while True:
        try:
            n = int(input("Enter Your Choice: "))
            if n == 1:
                net.make_data()
            elif n == 2:
                net.format_data()
            elif n == 3:
                net.arc.archive_csv()
            else:
                exit(0)
        except ValueError as ve:
            print(f"{ve} --> occurred.")
