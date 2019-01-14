import random


def _generate_secret(start, end, size):
    range_list = list(range(start, end))
    num_list = random.sample(range_list, size)

    return num_list


def get():
    start = random.randint(1, 100)
    end = 0
    while end <= start:
        end = random.randint(1, 100)

    size = 100
    while size > (end - start):
        size = random.randint(1, 100)

    return _generate_secret(start, end, size)
