from Bio import SeqIO

# 1. 定义你的FASTA文件路径
fasta_file = "your_sequence.fasta" # 替换成你的实际文件路径

# 2. 使用SeqIO.parse()迭代读取文件
# 'fasta'是格式类型
for record in SeqIO.parse(fasta_file, "fasta"):
    # 3. 打印或处理每个序列的ID, 描述, 序列内容和长度
    print(f"ID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Sequence: {record.seq}") # record.seq 是一个Seq对象
    print(f"Length: {len(record.seq)}") # 或者直接 len(record)
    print("-" * 20)

# 如果文件很大，可以分块读取
# for record in SeqIO.parse("large_file.fasta", "fasta"):
#     # 处理...
