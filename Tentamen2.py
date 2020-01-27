# Author: Femke Spaans
# Date: 24/01/2020
# Name: Tentamen blok 2
# Version: 1

import re


def main():
    name_file = "TAIR10_pep_20101214.fa"
    name_file_gff3 = "TAIR10_GFF3_genes.gff"
    headers, seqs = read_file_fasta(name_file)
    pattern = consensus(headers, seqs)
    open_file(name_file_gff3)


def read_file_fasta(name_file):
    """
    Open file,
    iterate over every line,
    append seqs and headers.
    :param: name_file
    :return:headers
    :return: seqs
    """
    headers = []
    seqs = []
    seq = ""
    file = open(name_file, 'r')
    for line in file:
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
        seqs.append(seq)
    file.close()
    return headers, seqs


def consensus(headers, seqs):
    """
    [LIVMFYC]-x-[HY]-x-D-[LIVMFY]-K-x(2)-N-[LIVMFYCT](3)
    :param: headers
    :param: seqs
    :return: pattern
    """
    match = []
    for seq in seqs:
        pattern = re.search(r"[LIVMFYC].[HY].D[LIVMFY]K..N[LIVMFYCT]{3}", seq)
        if str(pattern) in seq:
            match.append(headers)
    print(match)


def open_file(name_file_gff3):
    """
    :return:
    """
    file = open(name_file_gff3, 'r')
    print(file[1])


main()
