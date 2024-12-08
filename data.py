import csv
import os

class Data:
    def __init__(self, filename):
        self.filename = filename
        self.fieldnames = ['name', 'level', 'checkpoint', 'health', 'points', 'enhances']
        if not os.path.isfile(self.filename):
            self.create_file()

    def create_file(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()

    def read_data(self):
        if not os.path.isfile(self.filename):
            self.create_file()
            return []

        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def write_data(self, data):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerows(data)

    def update_data(self, name, **kwargs):
        rows = self.read_data()
        for row in rows:
            if row['name'] == name:
                for key, value in kwargs.items():
                    if key in self.fieldnames:
                        row[key] = value

        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)
