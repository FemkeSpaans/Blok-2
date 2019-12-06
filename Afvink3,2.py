# Author: Femke Spaans
# Date: 02/12/2019
# Name: Afvink 3
# Version: 2


def main():
    codon = lexicon()
    data(codon)


def lexicon():
    """dictionary,
    :return: codon
    """

    codon = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
             'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
             'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
             'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
             'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
             'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
             'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
             'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
             'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
             'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
             'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
             'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
             'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
             'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
             'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
             'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
             }
    return codon


def data(codon):
    """input file,
    open file,
    loop to iterate over file in steps of three,
    print letters of amino acids,
    :param codon:
    """
    var = ''
    file = input("What file would you like to open?")
    file1 = open(file, "r").readline()
    dna = False
    a = file1.count("A")
    t = file1.count("T")
    c = file1.count("C")
    g = file1.count("G")
    total = a + t + c + g
    if total == len(file1):
        dna = True
    if dna is True:
        for i in range(file1.find("ATG"), len(file1), 3):
            codons = file1[i:i + 3].lower()
            var += codon[codons]
    else:
        print("This sequence is not DNA")
    print(var)


main()
