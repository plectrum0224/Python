# encoding: utf-8

def get_valid_input(input_string, valid_option):
    input_string += " ({}) ".format(", ".join(valid_option))
    response = raw_input(input_string)
    while response.lower() not in valid_option:
        response = raw_input(input_string)
    return response