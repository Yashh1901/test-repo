# utils.py

def parse_input(data):
    # No type checking or validation
    return int(data) * 100


def format_output(value, decimals):
    # No handling for invalid decimals
    return round(value, decimals)


def load_file(path):
    # File never closed — resource leak
    f = open(path)
    return f.read()