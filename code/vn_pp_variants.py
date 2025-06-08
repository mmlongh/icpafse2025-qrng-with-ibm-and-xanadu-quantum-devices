from typing import Sequence
import numpy as np

def vnpp_variant_1(bits: Sequence[int]) -> np.ndarray:
    bits = np.array(bits)
    shots =  bits.shape[0]
    unbiased_bits = [] 
    for shot_idx in range(0, shots, 2):
        bit_1 = bits[shot_idx, 0, 0]
        bit_2 = bits[shot_idx + 1, 0, 0]
        if bit_1 != bit_2:
            unbiased_bits.append(bit_1)
    return np.array(unbiased_bits)

def vnpp_variant_2(bits: Sequence[int]) -> np.ndarray:
    bits = np.array(bits)
    shots =  bits.shape[0]
    unbiased_bits = [] 
    for shot_idx in range(0, shots, 2):
        shot_1 = bits[shot_idx, 0, :]
        shot_2 = bits[shot_idx + 1, 0, :]
        for bit_1, bit_2 in zip(shot_1, shot_2):
            if bit_1 != bit_2:
                unbiased_bits.append(bit_1)
                break
    return np.array(unbiased_bits)