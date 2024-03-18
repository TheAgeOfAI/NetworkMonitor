import re
import os
import platform
import subprocess
import time


# This method will filter file and append the filtered data to another file and returns None.
def filterAndAppend() -> None:

    # This pattern search for a line that contain 64 bytes from IP with time in ms
    # pattern = re.compile(r"(\d+)\s+bytes\s+from\s+.*\s+([(\d.)]+).*time=(\d+\.?\d*)\s+ms")
    # start = re.compile(r"^\(")
    # end = re.compile(r"^\)")
    block_string = ''
    block_status = False
    # We are using try block to check if file are available or not.([(\d\.)]+)
    try:
        # Opening file to read data.
        with open('ping.txt') as file:
            # Opening file to write data.
            # with open("result.txt", 'a') as opt:
                # data = file.readlines()
                # readlines() can also be used but time-consuming.
            for line in file:
                # checking for pattern if available in the line.
                # result = pattern.search(line)
                start = re.search(r"^\(", line)
                if start:
                    block_status = True
                end = re.search(r"^\)", line)
                if end:
                    block_status = False
                    site_ping_data(block_string)
                    block_string = ''
                if block_status:
                    if not start:
                        block_string += line
                # if result:
                #     # Writing to file if pattern found in the line.
                #     opt.write(f'{result.group(1)}, {result.group(2)[1:-1]}, {result.group(3)}\n')


    except Exception as e:
        print("This Exception -> ", e, " <- occurred.")


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

    return f'{year}, {month}, {date}, {hours}, {minutes}, {seconds}, {weekday}, {weekend}'


def site_ping_data(data):
    ping_filter = re.compile("time=(\d+\.*\d+)\s+\S+")
    data = data.split('\n')
    time_data = date_time_split(data[0])

    site_data = data[1].split()[1].split('.')[0]
    ipaddress = data[1].split()[2][1:-1]

    with open('results.txt', 'a') as fd:

        for line in data[2:]:
            ping = ping_filter.search(line)
            if ping:
                fd.write(f'{time_data}, {site_data}, {ipaddress}, {ping.group(1)}\n')


# This function will make ping calls and return append that output to another file
def ping_to_file() -> None:

    hosts = ['google', 'duckduckgo', 'example', 'brave']
    param = '-c' if platform.system().lower() == 'linux' else '-n'
    sites = {}
    try:
        with open('result.txt', 'a') as fd:
            for host in hosts:
                command = ['ping', param, '5', f'{host}.com']
                sites[host] = subprocess.run(command,capture_output=True)
                fd.write('(\n{}\n{})\n'.format(time.strftime('%Y:%m:%d-%X-%w'), sites[host].stdout.decode('utf-8')))
    except Exception as e:
        print("This Exception -> ", e, " <- occurred.")