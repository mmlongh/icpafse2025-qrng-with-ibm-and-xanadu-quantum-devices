from code.read_write_bits import write_bits_to_binfile, read_bits_from_binfile
from code.von_neumann_postprocessing import von_neumann_postprocessing

if __name__ == "__main__":
    bits  = read_bits_from_binfile("data/ibm_sherbrooke_data.bin")

    unbiased_bits = von_neumann_postprocessing(bits)
    write_bits_to_binfile(unbiased_bits, "results/ibm_sherbrooke_unbiased_data.bin")
    print(f"Saved unbiased bits to results/ibm_sherbrooke_unbiased_data.bin")

    substring = unbiased_bits[:2_000_000]
    write_bits_to_binfile(substring, "results/ibm_sherbrooke_substring_unbiased_data.bin")
    print(f"Saved 2M substring of unbiased bits to results/ibm_sherbrooke_substring_unbiased_data.bin")