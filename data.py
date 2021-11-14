import csv

class Data:
    def __init__(self):
        self.data = {}
        with open('./data.csv', encoding="utf8") as f:
            csv_reader = csv.reader(f)
            for line_no, line in enumerate(csv_reader, 1):
                if line_no > 1:
                    self.data[line[0]] = line[1]
    def get_item(self, key):
        return self.data.get(key)