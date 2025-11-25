import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("path", help="log directory")
parser.add_argument("-t", "--text", help="text for search")
args = parser.parse_args()
print(args.path, args.text)

for file_name in os.listdir(args.path):
    file_path = os.path.join(args.path, file_name)
    with open(file_path) as log_file:
        data = log_file.readlines()
        for line_number, line in enumerate(data, start=1):
            if args.text in line:
                line_list = line.split()
                text_index = line_list.index(args.text)
                # fmt: off
                needed_line = (
                    line_list[text_index - 5:text_index]
                    + line_list[text_index:text_index + 6]
                )
                needed_line = " ".join(needed_line)
                print(file_name, line_number, needed_line)
