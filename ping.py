import platform
import subprocess
from multiprocessing import Process
import time
from hosts import Hosts


class Ping(Hosts):
    def __init__(self):
        super(Ping, self).__init__()
        self.param = '-c' if platform.system().lower() == 'linux' else '-n'

    def ping_to_file(self):
        processes = []

        for host in self.hosts:
            process = Process(target=self.ping_host, args=(host,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

    # Helper Method
    def ping_host(self, host):
        # Execute the ping command for the specified host
        ping_process = subprocess.Popen(['ping', f'{self.param}', '50', f'{host}.com'], stdout=subprocess.PIPE)
        ping_output, _ = ping_process.communicate()

        # Write the ping output to a file
        with open(f'./data/txt/{host}.txt', 'a') as fd:
            fd.write('(\n{}\n{})\n'.format(time.strftime('%Y:%m:%d-%X-%w'),
                                           ping_output.decode('utf-8')))
