import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """

    pos = np.arange(seq_len)[:, np.newaxis]
    i = np.arange(d_model)[np.newaxis, :]

    # use base instead of fixed 10000
    angle_rates = 1 / np.power(base, (2 * (i // 2)) / d_model)

    angles = pos * angle_rates

    pe = np.zeros((seq_len, d_model))

    pe[:, 0::2] = np.sin(angles[:, 0::2])
    pe[:, 1::2] = np.cos(angles[:, 1::2])

    return pe.astype(float)


print(np.round(positional_encoding(3,4),4))