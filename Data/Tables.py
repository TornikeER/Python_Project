input_dna = "ATTTGGCTACTAACAATCTA"

correct_rna = "AUUUGGCUACUAACAAUCUA"

correct_protein = "IWLLTI"


transcription_table = {
    'A': 'A',
    'T': 'U',
    'G': 'G',
    'C': 'C',
}

translation_table = {
    'F': {'full_name': 'Phenylalanine', 'codons': ['UUU', 'UUC'], },
    'L': {'full_name': 'Leucine',
          'codons': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], },
    'S': {'full_name': 'Serine',
          'codons': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], },
    'Y': {'full_name': 'Tyrosine', 'codons': ['UAU', 'UAC'], },
    '*': {'full_name': 'Stop codon', 'codons': ['UAA', 'UAG', 'UGA'], },
    'C': {'full_name': 'Cysteine', 'codons': ['UGU', 'UGC'], },
    'W': {'full_name': 'Tryptophan', 'codons': ['UGG'], },
    'P': {'full_name': 'Proline', 'codons': ['CCU', 'CCC', 'CCA', 'CCG'], },
    'H': {'full_name': 'Histidine', 'codons': ['CAU', 'CAC'], },
    'Q': {'full_name': 'Glutamine', 'codons': ['CAA', 'CAG'], },
    'R': {'full_name': 'Arginine',
          'codons': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], },
    'I': {'full_name': 'Isoleucine', 'codons': ['AUU', 'AUC', 'AUA'], },
    'M': {'full_name': 'Methionine', 'codons': ['AUG'], },
    'T': {'full_name': 'Threonine', 'codons': ['ACU', 'ACC', 'ACA', 'ACG'], },
    'N': {'full_name': 'Asparagine', 'codons': ['AAU', 'AAC'], },
    'K': {'full_name': 'Lysine', 'codons': ['AAA', 'AAG'], },
    'V': {'full_name': 'Valine', 'codons': ['GUU', 'GUC', 'GUA', 'GUG'], },
    'A': {'full_name': 'Alanine', 'codons': ['GCU', 'GCC', 'GCA', 'GCG'], },
    'D': {'full_name': 'Aspartic acid', 'codons': ['GAU', 'GAC'], },
    'E': {'full_name': 'Glutamic acid', 'codons': ['GAA', 'GAG'], },
    'G': {'full_name': 'Glycine', 'codons': ['GGU', 'GGC', 'GGA', 'GGG'], },
}

Amino_Dict =  {
    # 'M' - START, '*' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "*", "UAG": "*", "UGA": "*"
}
