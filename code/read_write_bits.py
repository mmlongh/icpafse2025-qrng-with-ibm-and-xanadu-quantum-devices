import numpy as np

def write_bits_to_binfile(bits: np.ndarray, filename: str, big_endian: bool = False) -> None:
    """Write a 1D array of 0/1 bits to a binary file."""
    pad_len = (-len(bits)) % 8
    if pad_len:
        bits = np.concatenate([bits, np.zeros(pad_len, dtype=np.uint8)])

    bits = bits.reshape(-1, 8)
    if not big_endian:
        bits = bits[:, ::-1]

    bytes_out = np.packbits(bits, axis=1).flatten()
    with open(filename, 'wb') as f:
        f.write(bytes_out.tobytes())

def read_bits_from_binfile(filename: str, big_endian: bool = False) -> np.ndarray:
    """Read bits from a binary file and return them as a list of 0/1 ints."""
    bits = []
    with open(filename, 'rb') as f:
        while chunk := f.read(16384):
            for byte in chunk:
                for i in range(8):
                    if big_endian:
                        bit = (byte >> (7 - i)) & 1
                    else:
                        bit = (byte >> i) & 1
                    bits.append(bit)
    return np.array(bits)
