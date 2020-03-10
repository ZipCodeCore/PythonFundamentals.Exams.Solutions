
def generate_list(start: int, stop: int, step: int = 1):
    """
    Generate a list of integers.

    :param start: Where to start the list (inclusive)
    :param stop: Where to stop the list (exclusive)
    :param step: How many digits apart each number is from the others around it.
    :return: A list of integers.
    """
    result = []
    for i in range(start, stop, step):
        result.append(i)
    return result
