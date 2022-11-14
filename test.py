import Data
from Script import convert_dna_to_rna, convert_rna_to_protein


def test_function(function, input_seq, output_seq):
    result = function(input_seq)
    print(result)
    assert result == output_seq


test_function(convert_dna_to_rna, Data.input_dna, Data.correct_rna)
test_function(convert_rna_to_protein, Data.correct_rna, Data.correct_protein)
