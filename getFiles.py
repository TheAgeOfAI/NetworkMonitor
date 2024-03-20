import csv
import platform
import re
import subprocess
import time


class Networking:

    def __init__(self):
        self.block_string = ''
        self.block_status = False
        self.depricated =  './data/depricated.csv'
        self.ping_file = './data/ping.txt'
        self.result_file = './data/result.csv'
        self.hosts = ['google', 'duckduckgo', 'example', 'brave']
        self.param = '-c' if platform.system().lower() == 'linux' else '-n'
        self.pattern = re.compile(r"(\d+)\s+bytes\s+from\s+.*\s+.*time=(\d+\.?\d*)\s+ms")
        self.pattern_depricated = re.compile(r"(\d+)\s+bytes\s+from\s+.*\s+([(\d.)]+).*time=(\d+\.?\d*)\s+ms")

    # This method will filter file and append the filtered data to another file and returns None.
    def read_filter_block(self) -> None:
        # We are using try block to check if file are available or not.
        try:
            # Opening file to read data.
            with open('ping.txt') as file:
                for line in file:
                    start = re.search(r"^\(", line)
                    if start:
                        self.block_status = True
                    end = re.search(r"^\)", line)
                    if end:
                        self.block_status = False
                        self.extract_ping(self.block_string)
                        self.block_string = ''
                    if self.block_status:
                        if not start:
                            self.block_string += line

        except Exception as e:
            print("This Exception -> ", e, " <- occurred.")

    def extract_ping(self, data) -> None:
        # This pattern search for a line that contain 64 bytes from IP with time in ms
        # pattern = re.compile(r"(\d+)\s+bytes\s+from\s+.*\s+([(\d.)]+).*time=(\d+\.?\d*)\s+ms")
        try:
            data = data.split('\n')
            time_data = self.date_time_split(data[0])

            site_data = data[1].split()[1].split('.')[0]
            ipaddress = data[1].split()[2][1:-1]

            try:
                with open(f'./data/{site_data}.csv', 'a') as fd:

                    for line in data[2:]:
                        ping = self.pattern.search(line)
                        if ping:
                            fd.write(f'{time_data}, {site_data}, {ipaddress}, \{ping.group(2)}\n')
            except Exception as e:
                print("Exception with file.", e)

        except Exception as e:
            print("Exception may be due to ping error in os level.", e)

    def extract_ping_depricated(self) -> None:
        try:
            with open(self.ping_file) as fd:
                with open(self.depricated,'a') as csvfile:
                    file = csv.writer(csvfile, delimiter=',')
                    for line in fd:
                        ping = self.pattern_depricated.search(line)
                        if ping:
                            file.writerow([ping.group(2)[1:-1], ping.group(3)])
                        
        except Exception as e:
            print("This Exception -> ", e, " <- occurred.")

    # This function will make ping calls and return append that output to another file
    def ping_to_file(self) -> None:

        sites = {}
        processes = {}
        try:
            # with open(self.ping_file, 'a') as fd:
            for host in self.hosts:
                with open(f'./data/{host}.txt', 'a') as fd:
                    command = ['ping', self.param, '5', f'{host}.com']
                    sites[host] = subprocess.run(command, capture_output=True)
                    fd.write('(\n{}\n{})\n'.format(time.strftime('%Y:%m:%d-%X-%w'),
                                                    sites[host].stdout.decode('utf-8')))
        except Exception as e:
            print("This Exception -> ", e, " <- occurred.")

    @staticmethod
    def date_time_split(data):
        temp = data.split('-')[0].split(':')
        year = temp[0]
        month = temp[1]
        date = temp[2]
        temp = data.split('-')[1].split(':')
        hours = temp[0]
        minutes = temp[1]
        seconds = temp[2]
        weekday = data.split('-')[2]
        weekend = 1 if weekday == 0 or weekday == 6 else 0

        return (f'{year}, {month}, {date}, '
                f'{hours}, {minutes}, {seconds}, '
                f'{weekday}, {weekend}')
