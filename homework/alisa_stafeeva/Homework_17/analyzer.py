import os
import argparse
from colorama import init, Fore, Style


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
                index_start = max(text_index - 5, 0)
                index_end = min(text_index + 6, len(line_list))
                needed_line = line_list[index_start:index_end]
                needed_line = " ".join(needed_line)
                old_list = line_list
                print(
                    f"{Fore.CYAN}{file_name}{Style.RESET_ALL}, "
                    f"строка {Fore.MAGENTA}{line_number}{Style.RESET_ALL}: {needed_line}"
                )
