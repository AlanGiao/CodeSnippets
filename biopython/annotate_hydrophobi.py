from Bio.PDB import PDBParser
from Bio.SeqUtils import seq1 # 获得三字母缩写

# 1. 定义 Kyte-Doolittle 评分
kyte_doolittle_scores = {
    'ALA': 1.8, 'ARG': -4.5, 'ASN': -3.5, 'ASP': -3.5, 'CYS': 2.5,
    'GLN': -3.5, 'GLU': -3.5, 'GLY': -0.4, 'HIS': -3.2, 'ILE': 4.5,
    'LEU': 3.8, 'LYS': -3.9, 'MET': 1.9, 'PHE': 2.8, 'PRO': -1.6,
    'SER': -0.8, 'THR': -0.7, 'TRP': -0.9, 'TYR': -1.3, 'VAL': 4.2
}

# 2. 解析 PDB (假设有 pdb.ent 文件)
parser = PDBParser()
structure = parser.get_structure("protein_id", "path/to/your/protein.pdb")

# 3. 遍历残基并标注
for model in structure:
    for chain in model:
        for residue in chain:
            res_name = seq1(residue.get_resname()) # 获取三字母缩写
            if res_name in kyte_doolittle_scores:
                score = kyte_doolittle_scores[res_name]
                # 这里可以进一步结合 DSSP 计算 SASA
                # residue.sasa = calculate_sasa(residue)
                print(f"Residue {residue.get_id
