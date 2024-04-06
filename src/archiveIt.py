import os


class Archive:
    def __init__(self):
        self.folder_path = './data'
        self.result_file = './data/result.csv'
        self.csv_files = './data/csv/'
        self.txt_files = './data/txt/'
        self.file_path = ''

    def archive_csv(self):
        with open(self.result_file, 'a') as output:
            for filename in os.listdir(self.csv_files):
                self.file_path = os.path.join(self.csv_files, filename)
                print(self.file_path)
                if os.path.isfile(self.file_path) and filename.endswith('.csv'):
                    with open(self.file_path, 'r') as file:
                        output.write(file.read())
        self.clear_csv()

    def clear_files(self, file_type, folder_location):
        for filename in os.listdir(self.txt_files):
            self.file_path = os.path.join(folder_location, filename)
            if os.path.isfile(self.file_path) and filename.endswith(file_type):
                file_path = os.path.join(folder_location, filename)
                with open(file_path, 'w') as file:
                    file.write('')

    def clear_txt(self):
        self.clear_files('txt', self.txt_files)

    def clear_csv(self):
        self.clear_files('csv', self.csv_files)

