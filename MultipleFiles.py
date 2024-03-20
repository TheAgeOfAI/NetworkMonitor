import multiprocessing
import re


class MultipleFiles:
    def __init__(self):
        self.hosts = ['google', 'duckduckgo', 'example', 'brave']
        self.block_string = ''
        self.block_status = False
        self.pattern = re.compile(r"(\d+)\s+bytes\s+from\s+.*\s+.*time=(\d+\.?\d*)\s+ms")

    def read_filter_block(self):
        processes = []

        for host in self.hosts:
            process = multiprocessing.Process(target=self.read_and_filter_file, args=(host,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

    def read_and_filter_file(self, host):
        try:
            with open(f'./data/txt/{host}.txt', 'r') as file:
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
            print(f"Exception occurred while processing {host}: {e}")

    def extract_ping(self, data):
        # Implement your logic to extract ping data here
        try:
            data = data.split('\n')
            time_data = self.date_time_split(data[0])

            site_data = data[1].split()[1].split('.')[0]
            ipaddress = data[1].split()[2][1:-1]

            try:
                with open(f'./data/csv/{site_data}.csv', 'a') as fd:

                    for line in data[2:]:
                        ping = self.pattern.search(line)
                        if ping:
                            fd.write(f'{time_data}, {site_data}, {ipaddress}, {ping.group(2)}\n')
            except Exception as e:
                print("Exception with file.", e)

        except Exception as e:
            print("Exception occured.", e)

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


if __name__ == '__main__':
    mf = MultipleFiles()
    mf.read_filter_block()
