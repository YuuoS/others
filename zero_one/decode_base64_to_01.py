import csv

def main():
    base64_file_path = 'base64.txt'
    output_file_path = 'output_01.txt'
    output_file = open(output_file_path, 'wt')

    with open('dict.csv', mode='r', encoding ="utf-8-sig") as inp:
        reader = csv.reader(inp)
        dict_from_csv = {rows[0]:rows[1] for rows in reader}

    print(dict_from_csv)

    with open(base64_file_path, encoding='utf-8') as f:
        content = f.read()

    for ch in content:
        if ch != '\n' and ch != '=':
            try:
                val = dict_from_csv[ch]
                print(f'{ch}: {val}')
                output_file.write(val)
            except KeyError:
                print(f'{ch}: Key error')

    # output_file.close()

if __name__ == '__main__':
    main()
