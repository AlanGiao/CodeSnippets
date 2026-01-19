from Bio.PDB import PDBParser
from Bio.SeqUtils import seq1

pdb_file = '4HHB.pdb'
chain_id = 'A'

parser = PDBParser(QUIET=True)
structure = parser.get_structure('structure', pdb_file)
for model in structure:
    for chain in model:
        if chain == chain_id
            for residue in chain:
                sequence += f"{seq1(residue.get_resname())}"
            break  # 找到目标链以后，不再继续迭代 model 中的 chain
    break  # 这样只会考虑 model 0
