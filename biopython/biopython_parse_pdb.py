from Bio.PDB import PDBParser
from Bio.SeqUtils import seq1

pdb_file = '4HHB.pdb'
chain_id = 'A'

# 从PDB文件中提取氨基酸序列。
parser = PDBParser(QUIET=True)
structure = parser.get_structure('structure', pdb_file)
for model in structure:
    for chain in model:
        if chain == chain_id
            for residue in chain:
                sequence += f"{seq1(residue.get_resname())}"
            break  # 找到目标链以后，不再继续迭代 model 中的 chain
    break  # 这样只会考虑 model 0


# 从 PDB 文件中获取 backbone atoms 的坐标。形成 [L, 4, 3] 向量。
pdb_parser = PDBParser(PERMISSIVE=1)
pdb_id = str(pdb_file).rstrip('.pdb')

# Biopython 将PDB建模为层级结构：structure-model-chains-residues-atoms.
structure = pdb_parser.get_structure(pdb_id, pdb_file)
model = structure[0]  # 在 NMI 结构中，一个结构可能有多个 model
chains = list(model.child_dict.keys())

chain_id = chains[0]
protein_backbone_coords = []
for residue in model[chain_id]:
    residue_backbone_coords = []
    for atom in residue:
        # 获取原子名字。
        if atom.get_name() in ['N', 'CA', 'C', 'O']:
            # 获取原子 3D 坐标。
            residue_backbone_coords.append(atom.get_coord())
    assert len(residue_backbone_coords) == 4
    protein_backbone_coords.append(residue_backbone_coords)
