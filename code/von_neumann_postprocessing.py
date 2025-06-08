from typing import Sequence
import numpy as np

def von_neumann_postprocessing(bits: Sequence[int]) -> np.ndarray:
    unbiased_bits = []
    for bit_1, bit_2 in zip(bits[::2], bits[1::2]):
        if bit_1 != bit_2:
            unbiased_bits.append(bit_1)
    return np.array(unbiased_bits)