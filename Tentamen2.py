# Author: Femke Spaans
# Date: 24/01/2020
# Name: Tentamen blok 2
# Version: 1

import re


def main():
    name_file = "TAIR10_pep_20101214.fa"
    headers, seqs = read_file(name_file)
    consensus(headers, seqs)


def read_file(name_file):
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
    :return:
    """
    pattern = re.search([])


main()
