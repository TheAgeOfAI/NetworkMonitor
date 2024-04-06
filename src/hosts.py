class Hosts:
    def __init__(self):
        self.hosts = ['google', 'duckduckgo', 'example', 'brave']

    def add_host(self, host):
        try:
            if not isinstance(host, str):
                raise ValueError("Host must be a string.")

            if host not in self.hosts:
                self.hosts.append(host)
        except ValueError as ve:
            print("Error:", ve)

    def remove_host(self, host):
        try:
            if not isinstance(host, str):
                raise ValueError("Host must be a string.")
            self.hosts.remove(host)
            print("removed successfully!")
        except ValueError as ve:
            print("Error:", ve)
