# Author: Femke Spaans
# Date: 24/01/2020
# Name: Tentamen blok 2
# Version: 1

import re
import numpy as np
import matplotlib.pyplot as plt


def main():
    name_file = "TAIR10_pep_20101214.fa"
    name_file_gff3 = "TAIR10_GFF3_genes.gff"
    headers, seqs = read_file_fasta(name_file)
    matches = consensus(headers, seqs)
    entry_match = open_file(name_file_gff3, matches)
    one, two, three, four, five = matplotlib_data(entry_match)
    matplotlib_graph(one, two, three, four, five)


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
    print("Fasta ready")
    file.close()
    return headers, seqs


# code orgineel van Martijn of Teuntje


def consensus(headers, seqs):
    """
    consensus = [LIVMFYC]-x-[HY]-x-D-[LIVMFY]-K-x(2)-N-[LIVMFYCT](3)
    check if consensus is in seq,
    split headers,
    put headers of seqs with consensus in list.
    :param: headers
    :param: seqs
    :return: matches
    """
    matches = []
    for header, seq in zip(headers, seqs):
        if re.search(r"[LIVMFYC].[HY].D[LIVMFY]K..N[LIVMFYCT]{3}", seq):
            matches.append(header[1:12])
    print("Consensus ready")
    return matches


# Powerpoint van informatica lessen gebruikt.


def open_file(name_file_gff3, matches):
    """
    :param: name_file_gff3
    :param: matches
    :return: entry_match
    """
    protein = []
    entry_match = []
    with open(name_file_gff3, 'r') as f:
        for line in f:
            protein.append(line)
        for item in matches:
            for entry in protein:
                if item in entry:
                    entry_match.append(entry)
    t = len(entry_match)
    print(t)
    return entry_match


def matplotlib_data(entry_match):
    """
    Data for the bar graph
    :param: entry_match
    :return:one
    :return:two
    :return:three
    :return:four
    :return:five
    """
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    c = 0
    m = 0
    for line in entry_match:
        line.strip()
        if re.search(r"Chr1", line):
            one += 1
        elif re.search(r"Chr2", line):
            two += 1
        elif re.search(r"Chr3", line):
            three += 1
        elif re.search(r"Chr4", line):
            four += 1
        elif re.search(r"Chr5", line):
            five += 1
        elif re.search(r"ChrC", line):
            c +=1
        elif re.search(r"ChrM", line):
            m +=1
    return one, two, three, four, five


def matplotlib_graph(one, two, three, four, five):
    """
    create a graph
    :param one:
    :param two:
    :param three:
    :param four:
    :param five:
    :return:
    """
    names = [one, two, three, four, five]
    n = 5
    ind = np.arange(n)
    plt.figure(figsize=(7.65, 5))
    plt.title("Genes with Serine/Threonine kinase active site per chromosome.")
    plt.ylabel("Amount of genes with Serine/Threonine kinase active site")
    plt.xlabel("Chromosome number")
    plt.xticks(ind, ("Chr1", "Chr2", "Chr3", "Chr4", "Chr5"))
    plt.bar(range(len(names)), names)
    plt.show()


main()
