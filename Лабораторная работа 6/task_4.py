import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", newline="\n") -> list[dict]:
    list_of_json = []
    headers_hint = {}
    lines = (line.rstrip(newline) for line in open(filename))

    headers = next(lines).split(sep=delimiter)

    for header_index in range(len(headers)):
        headers_hint[header_index] = headers[header_index]
    for row in lines:
        json_struct = {}
        columns_in_list = row.split(sep=delimiter)

        for index in range(len(columns_in_list)):
            json_struct[headers_hint[index]] = columns_in_list[index]
        list_of_json.append(json_struct)

    return list_of_json







print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))