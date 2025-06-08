import numpy as np
from code.read_write_bits import write_bits_to_binfile, read_bits_from_binfile
from code.vn_pp_variants import vnpp_variant_2

if __name__ == "__main__":
    files = ['fig2', 'fig3a', 'fig3b', 'fig4', 'figS15']
    pp = np.array([], dtype=np.uint8)
    for file in files:
        data = np.load(f'data/xanadu_borealis_{file}.npy', mmap_mode='r')
        preprocess = np.empty_like(data, dtype=np.uint8)
        for i in range(data.shape[0]):
            preprocess[i] = (data[i] > 0).astype(np.uint8)
        current_pp = vnpp_variant_2(preprocess)
        pp = np.concatenate((pp, current_pp))
    
    write_bits_to_binfile(pp, "results/xanadu_borealis_unbiased_data_variant_2.bin")
    print(f"Saved unbiased bits (using variant 2) to results/xanadu_borealis_unbiased_data_variant_2.bin")

    substring = pp[:2_000_000]
    write_bits_to_binfile(substring, "results/xanadu_borealis_substring_unbiased_data_variant_2.bin")
    print(f"Saved 2M substring of unbiased bits (using variant 2) to results/xanadu_borealis_substring_unbiased_data_variant_2.bin")