import re
import csv
import numpy as np


def main():
    input_file = "/Users/yuki/Desktop/output_01.txt"
    with open(input_file, "r") as file:
        read_file = file.read()
    file.close()

    contents = (read_file.replace('\r', '')).replace('\n', '')
    print(contents)
    new_list = re.split('(......)', contents)[1::2]
    print(np.array(new_list))

    with open('./dict.csv', mode='r', encoding="utf-8-sig") as inp:
        reader = csv.reader(inp)
        dict_from_csv = {rows[0]: rows[1] for rows in reader}

    print(dict_from_csv)

    dict_from_csv_swapped = {v: k for k, v in dict_from_csv.items()}
    print(dict_from_csv_swapped)


    output_file_path = './output_base64.txt'
    output_file = open(output_file_path, 'wt')

    for ch in new_list:
        if ch != '\n':
            try:
                val = dict_from_csv_swapped[ch]
                print(f'{ch}: {val}')
                output_file.write(val)
            except KeyError:
                print(f'{ch}: Key error')

    if len(new_list) % 4 == 1:
        output_file.write('=')
        output_file.write('=')
        output_file.write('=')
    elif len(new_list) % 4 == 2:
        output_file.write('=')
        output_file.write('=')
    elif len(new_list) % 4 == 3:
        output_file.write('=')
    elif len(new_list) % 4 == 3:
        print(f'len is {len(new_list)}, mod 4 is {len(new_list)%4}')

    output_file.close()

if __name__ == '__main__':
    main()
