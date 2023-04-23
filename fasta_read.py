def fasta_read(database):
    import re
    ANNO = re.compile('>')
    CLEAR = re.compile('[^>\n]+')
    IDs = []
    anno_idx = []
    sequences = []

    with open(database) as f:
        lines = f.readlines()
# 주석 위치 찾기 (인덱스) 및 정제, 리스트 반환
    n=0    
    for line in lines:
        if ANNO.findall(line):
            anno_idx.append(n)
            clear = CLEAR.findall(line)
            IDs.append(clear[0].split('|'))
        n += 1

# 주석 사이의 (주석 인덱스 사이의) 시퀀스 정제 및 리스트 반환
    for i in range(len(anno_idx)):
        max_index = len(anno_idx) -1
        if i != max_index:
            seq_lines = lines[anno_idx[i]+1:anno_idx[i+1]]
            seq = ''
            for seq_line in seq_lines:
                seq_line = CLEAR.findall(seq_line)
                seq += seq_line[0]
            sequences.append(seq)
        else:
            seq_lines = lines[anno_idx[i]+1:]
            seq = ''
            for seq_line in seq_lines:
                seq_line = CLEAR.findall(seq_line)
                seq += seq_line[0]
            sequences.append(seq)

    import pandas as pd

    df = pd.DataFrame({'IDs':IDs, 'sequences':sequences})

    return df
