# Author: Femke Spaans
# Date: 15/11/2019
# Name: Tentamen blok 1, again
# Version: 1


def main():
    genen_per_chr()
    # alle_genen()


def genen_per_chr():
    """open the file,
    input chr,
    count the genes on this chromosome,
    count how many are on the p and the q arm,
    :return: p and q arm.
    """
    amount = 0
    amount_p = 0
    amount_q = 0
    File = open("gene_with_protein_product.txt", "r", encoding="utf8")
    chr = int(input("Which chromosome would you like to use?"))
    for line in File:
        position = line.split("\t")[7]
        if position[0:2] == chr:
            amount += 1
            if position[2] == "p":
                amount_p += 1
            if position[2] == "q":
                amount_q += 1
    print("p:", amount_p)
    print("q:", amount_q)
    print("amount:", amount)
    return amount_p, amount_p



# amount = 0 : a variable to count the genes on the given chromosome
# amount_p = 0 : a variable to count the number of p on the genes, in the given chromosome
# amount_q = 0 : a variable to count the number of q on the genes, in the given chromosome


def alle_genen():
    pass


main()
