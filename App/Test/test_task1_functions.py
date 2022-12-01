from Data import Tables
from Script_Task1 import convert_dna_to_rna, convert_rna_to_protein


def test_function(function, input_seq, output_seq):
    result = function(input_seq)
    print(result)
    assert result == output_seq


test_function(convert_dna_to_rna, Tables.input_dna, Tables.correct_rna)
test_function(convert_rna_to_protein, Tables.correct_rna, Tables.correct_protein)
