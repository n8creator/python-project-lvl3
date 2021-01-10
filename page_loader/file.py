"""Module saving some variable data into file."""


def save_file(data, local_path):
    """Save string data into file with specified path.

    Args:
        data ([str]): some data
        local_path ([str]): local path
    """
    try:
        with open(local_path, 'w') as file:
            file.write(data)
    except Exception as err:
        print('An error occurred while saving the file:' + str(err))


def read_file(local_path):
    """Read file data and store into variable.

    Args:
        local_path ([str]): local path to file
    """
    try:
        with open(local_path, 'r') as file:
            data = file.read()
        return data
    except Exception as err:
        print('An error occurred while reading the file:' + str(err))