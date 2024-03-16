import re
import os
import platform
import subprocess
import time


# This method will filter file and append the filtered data to another file and returns None.
def filterAndAppend() -> None:

    # This pattern search for a line that contain 64 bytes from IP with time in ms
    pattern = re.compile(r"(\d+)\s+bytes\s+from\s+.*\s+([(\d.)]+).*time=(\d+\.?\d*)\s+ms")
    # We are using try block to check if file are available or not.([(\d\.)]+)
    try:
        # Opening file to read data.
        with open('ping.txt') as file:
            # Opening file to write data.
            with open("result.txt", 'a') as opt:
                # data = file.readlines()
                # readlines() can also be used but time-consuming.
                for line in file:
                    # checking for pattern if available in the line.
                    result = pattern.search(line)
                    if result:
                        # Writing to file if pattern found in the line.
                        opt.write(f'{result.group(1)}, {result.group(2)[1:-1]}, {result.group(3)}\n')

    except Exception as e:
        print("This Exception -> ", e, " <- occurred.")


# This function will make ping calls and return append that output to another file
def pinger() -> None:

    hosts = ['google', 'duckduckgo', 'example', 'brave']
    param = '-c' if platform.system().lower() == 'linux' else '-n'
    sites = {}
    with open('result.txt', 'a') as fd:
        for host in hosts:
            command = ['ping', param, '5', f'{host}.com']
            sites[host] = subprocess.run(command,capture_output=True)
            fd.write('(\n{}\n{})\n'.format(time.strftime('%Y:%m:%d-%X-%w'), sites[host].stdout.decode('utf-8')))
