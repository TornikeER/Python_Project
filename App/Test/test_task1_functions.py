from Data import Constants
from Scripts.DnaToProteinFunctionScript import convert_dna_to_rna, convert_rna_to_protein


def test_function(function, input_seq, output_seq):
    result = function(input_seq)
    print(result)
    assert result == output_seq


test_function(convert_dna_to_rna, Constants.input_dna, Constants.correct_rna)
test_function(convert_rna_to_protein, Constants.correct_rna, Constants.correct_protein)
