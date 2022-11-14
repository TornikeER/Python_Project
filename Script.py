import Data


def convert_dna_to_rna(dna_sequence) -> str:
    rna_sequence = dna_sequence.replace('T', 'U')
    return rna_sequence


def convert_rna_to_protein(rna_sequence) -> str:
    protein = ""

    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i + 3]
        if len(codon) == 3:
            protein += Data.table[codon]

    return protein
