import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode='r') as f:
        data = json.load(f)
    if field not in data:
        return None
    return data[field]


def main():
#    pass
    file = 'sequential.json'
    field = "unordered_numbers"
    sequential_data = read_data(file, field)
    print(sequential_data)


if __name__ == '__main__':
    main()