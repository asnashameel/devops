import csv
import re
def process_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
process_csv(r'C:\Users\Administrator\Desktop\devops\007_python\day1\file.csv')