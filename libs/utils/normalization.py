def normalize_data(data):
    return (data - min(data)) / (max(data) - min(data))


def denormalize_coefficents(x, y, b0, b1):
    denorm_b1 = (max(y) - min(y)) * b1 / (max(x) - min(x))
    denorm_b0 = min(y) + ((max(y) - min(y)) * b0) + denorm_b1 * (1 - min(x))
    return denorm_b0, denorm_b1