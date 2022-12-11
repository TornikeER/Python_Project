from Data.db_query import transcription_query, translation_query


def convert_dna_to_rna(dna_sequence) -> str:
    m_rna = []
    for nucleotide in dna_sequence:
        m_rna.append(transcription_query(nucleotide))
    return ''.join(m_rna)


def convert_rna_to_protein(m_rna) -> str:
    protein = []
    index = 0
    current_triplet = []
    sequence = 3

    for index in range(0, len(m_rna)):
        current_triplet.append(m_rna[index])
        if (index + 1) % sequence:
            index += 1
            continue
        str_triplet = ''.join(current_triplet)
        protein.append(translation_query(str_triplet))
        current_triplet.clear()
        index += 1

    return ''.join(protein)

