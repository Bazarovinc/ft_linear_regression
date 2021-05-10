def error_function(x, y, estimated):
    return sum(pow(y - estimated, 2)) / (len(x))


def mean(array):
    return sum(array) / len(array)


def mse(x, y, estimated):
    return sum(pow(y - estimated, 2)) / (len(x))


def determination(x, y, estimated):
    return 1 - mse(x, y, estimated) / sum(pow(y - mean(y), 2))
