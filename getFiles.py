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

