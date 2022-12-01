from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Dna(Base):
    __tablename__ = 'dna_nucleotides'

    nucleotide_id = Column(Integer, primary_key=True)
    base_name = Column(String(1))
    child_rna = relationship('Rna', back_populates='parent_dna')
    rna_id = Column(Integer, ForeignKey('rna_nucleotides.nucleotide_id'))

    def __str__(self):
        return f'{self.nucleotide_id}: {self.base_name} ---> {self.child_rna}'


class Rna(Base):
    __tablename__ = 'rna_nucleotides'

    nucleotide_id = Column(Integer, primary_key=True)
    base_name = Column(String(1))
    parent_dna = relationship('Dna', back_populates='child_rna')

    def __str__(self):
        return f'{self.nucleotide_id}: {self.base_name}'


class RnaCodon(Base):
    __tablename__ = 'rna_codons'

    codon_id = Column(Integer, primary_key=True)
    codon_name = Column(String(3))
    amino_acid = relationship('AminoAcid', back_populates='rna_codon')
    acid_id = Column(Integer, ForeignKey('amino_acids.acid_id'))

    def __str__(self):
        return f'{self.codon_id}: {self.codon_name} ---> {self.amino_acid}'


class AminoAcid(Base):
    __tablename__ = 'amino_acids'

    acid_id = Column(Integer, primary_key=True)
    acid_name = Column(String(1))
    acid_full_name = Column(String(30))
    rna_codon = relationship('RnaCodon', back_populates='amino_acid')

    def __str__(self):
        return f'{self.acid_id}: {self.acid_name}({self.acid_full_name})'
