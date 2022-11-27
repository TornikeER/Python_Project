from sqlalchemy.orm import sessionmaker

from Data.db_tables import Dna, Rna, RnaCodon, AminoAcid
from Data.db_create import ENGINE

SESSION = sessionmaker(ENGINE)


def transcription_query(dna_nuke: str) -> str:
    """Function receives codon and fetches the corresponding amino acid from Database"""
    with SESSION() as session:
        result = (
            session.query(Rna)
            .join(Dna)
            .filter(Dna.base_name == dna_nuke)
        )
        return result[0].base_name


def translation_query(triplet: str) -> str:
    """Function receives DNA and fetches the corresponding mRNA from Database"""
    with SESSION() as session:
        result = (
            session.query(AminoAcid)
            .join(RnaCodon)
            .filter(RnaCodon.codon_name == triplet)
        )
        return result[0].acid_name
