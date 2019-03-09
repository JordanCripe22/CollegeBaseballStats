
class Utils:

    def __init__(self):
        pass

    @staticmethod
    def array_to_string(arr):
        str_ans = ""
        for word in arr:
            if word != "":
                str_ans = str_ans + word + " "
        return str_ans[:-1]

    @staticmethod
    def parse_name_from_str(name_str):
        name_array = []
        first_name = ""
        last_name = ""
        name_str = name_str.replace(".", "")
        split_name_str = name_str.split(" ")

        if len(split_name_str) == 1:
            split_comma = split_name_str[0].split(',')

            last_name = split_comma[0]

            if len(split_comma) == 2:
                first_name = split_comma[1]

            elif len(split_comma) == 1:
                pass
            else:
                raise ValueError('Unable to identify ' + name_str)

        elif len(split_name_str) == 2:
            if split_name_str[0][-1] == ",":
                last_name = split_name_str[0][:-1]
                first_name = split_name_str[1]
            else:
                first_name = split_name_str[0]
                last_name = split_name_str[1]
        elif len(split_name_str) == 3:

            if split_name_str[0][-1] == ",":
                last_name = split_name_str[0][:-1]
                if split_name_str[1] == "":
                    first_name = split_name_str[2]
                else:
                    # case of 2 first names
                    first_name = split_name_str[1] + " " + split_name_str[2]
            elif split_name_str[1][-1] == ",":
                last_name = split_name_str[0] + " " + split_name_str[1][:-1]
                first_name = split_name_str[2]
            else:
                raise ValueError('ERROR 2 parseNameArray' + str(split_name_str))
        else:
            raise ValueError('ERROR 3 parseNameArray', name_str)

        if "." in first_name:
            first_name = first_name.replace('.', '')

        name_array.append(first_name)
        name_array.append(last_name)

        return name_array
