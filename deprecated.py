import csv
import re
from toCSV import ConvertCSV
from ping import Ping


class Deprecated(ConvertCSV, Ping):

    def __init__(self):
        super(Deprecated, self).__init__()
        super(Deprecated, self).__init__()
        self.deprecated = './data/deprecated.csv'
        self.ping_file = './data/ping.txt'
        self.result_file = './data/result.csv'
        self.pattern_deprecated = re.compile(r"(\d+)\s+bytes\s+from\s+.*\s+([(\d.)]+).*time=(\d+\.?\d*)\s+ms")

    def extract_ping_deprecated(self) -> None:
        try:
            with open(self.ping_file) as fd:
                with open(self.deprecated, 'a') as csvfile:
                    file = csv.writer(csvfile, delimiter=',')
                    for line in fd:
                        ping = self.pattern_deprecated.search(line)
                        if ping:
                            file.writerow([ping.group(2)[1:-1], ping.group(3)])
                        
        except Exception as e:
            print("This Exception -> ", e, " <- occurred.")
