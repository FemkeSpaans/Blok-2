# Author: Femke Spaans
# Date: 24/01/2020
# Name: Tentamen blok 2
# Version: 1

import re
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *


def main():
    MyGUI()
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
    try:
        file = open(name_file, 'r')
        headers = []
        seqs = []
        seq = ""
        for line in file:
            line = line.strip()
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
    except FileNotFoundError:
        print("This file is not in this directory")
    except NameError:
        print("There is an identifier which is not found")
    except IOError:
        print("File %s is not legible" % name_file)
    except KeyboardInterrupt:
        print("Ctrl c has been pressed, this ends the program")


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
    try:
        matches = []
        for header, seq in zip(headers, seqs):
            if re.search(r"[LIVMFYC].[HY].D[LIVMFY]K..N[LIVMFYCT]{3}", seq):
                matches.append(header[1:12])
        print("Consensus ready")
        return matches
    except NameError:
        print("There is an identifier which is not found")
    except ImportError:
        print("There is something wrong with the import")
    except KeyboardInterrupt:
        print("Ctrl c has been pressed, this ends the program")

# Powerpoint van informatica lessen gebruikt.


def open_file(name_file_gff3, matches):
    """
    open file gff3 and put into a list
    :param: name_file_gff3
    :return: protein
    """
    try:
        file = open(name_file_gff3, 'r')
        protein = []
        entry_match = []
        for line in file:
            protein.append(line)
        for item in matches:
            for entry in protein:
                if item in entry:
                    if re.search(r"ID=", entry):
                        if re.search(r"protein", entry):
                            entry_match.append(entry)
        print("Gff3 ready")
        file.close()
        return entry_match
    except FileNotFoundError:
        print("This file is not in this directory")
    except NameError:
        print("There is an identifier which is not found")
    except IOError:
        print("File %s is not legible" % name_file_gff3)
    except ImportError:
        print("There is something wrong with the import")
    except KeyboardInterrupt:
        print("Ctrl c has been pressed, this ends the program")


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
    try:
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
                c += 1
            elif re.search(r"ChrM", line):
                m += 1
        print("Data graph ready")
        return one, two, three, four, five
    except NameError:
        print("There is an identifier which is not found")
    except ImportError:
        print("There is something wrong with the import")
    except KeyboardInterrupt:
        print("Ctrl c has been pressed, this ends the program")


def matplotlib_graph(one, two, three, four, five):
    """
    create a graph
    :param one:
    :param two:
    :param three:
    :param four:
    :param five:
    """
    try:
        names = [one, two, three, four, five]
        n = 5
        ind = np.arange(n)
        plt.figure(figsize=(7.65, 5))
        plt.title(
            "Genes with Serine/Threonine kinase active site per chromosome.")
        plt.ylabel("Amount of genes with Serine/Threonine kinase active site")
        plt.xlabel("Chromosome number")
        plt.xticks(ind, ("Chr1", "Chr2", "Chr3", "Chr4", "Chr5"))
        plt.bar(range(len(names)), names)
        plt.show()
    except ImportError:
        print("There is something wrong with the import")
    except NameError:
        print("There is an identifier which is not found")
    except KeyboardInterrupt:
        print("Ctrl c has been pressed, this ends the program")


def find_length_gene(entry_match):
    """
    :param entry_match:
    :return: length
    """
    try:
        start = int(entry_match[3])
        end = int(entry_match[4])
        length = end - start
        return str(length)
    except NameError:
        print("There is an identifier which is not found")
    except KeyboardInterrupt:
        print("Ctrl c has been pressed, this ends the program")


def count_amount_exons(name_file_gff3, match):
    """
    :param name_file_gff3:
    :param match:
    :return: exon
    """
    try:
        file = open(name_file_gff3, 'r')
        exon = 0
        protein = []
        for line in file:
            protein.append(line.strip().split("\t"))
        for entry in protein:
            if match in entry[8]:
                if entry[2] == "exon":
                    exon += 1
        file.close()
        return exon
    except NameError:
        print("There is an identifier which is not found")
    except KeyboardInterrupt:
        print("Ctrl c has been pressed, this ends the program")


class MyGUI:
    """
    """

    def __init__(self):
        self.data = Data()

        root = Tk()
        root.title("huppeldepup")

        mainframe = Frame(root, borderwidth=20)
        mainframe.grid(row=0, column=0)

        # label with accession numbers
        label_dropdown = Label(mainframe, text="Accession numbers")
        label_dropdown.grid(row=0, column=0, sticky="nw")

        # dropdown menu
        option_list = self.data.matches
        variable = StringVar(root)
        variable.set(option_list[0])
        drop_down = OptionMenu(mainframe, variable, *option_list,
                               command=self.data_display)
        drop_down.grid(row=1, column=0, sticky="nw")

        # label with extra information
        label_info = Label(mainframe, text="Information")
        label_info.grid(row=0, column=1, sticky="w", padx=(20, 0))

        # text with information
        self.text_chromo = Text(mainframe, width=50, height=5,
                                state="disabled")
        self.text_chromo.grid(row=1, column=1, sticky="w", padx=(20, 0))

        # label visualisation
        label_vis = Label(mainframe, text="Visualisation")
        label_vis.grid(row=2, column=0, sticky="nw", pady=(10, 0))

        # canvas for visualisation
        picture_chromo = Text(mainframe, width=68, height=3)
        picture_chromo.grid(row=3, column=0, columnspan=2, sticky="nw")

        # chromosome_number = (entry_match[0])

        root.mainloop()

    def data_display(self, state):
        # chromosome number finder
        accession_number = self.data.matches.index(state)
        data_entry = self.data.entry_match[accession_number] \
            .strip().split("\t")
        chromosome_number = data_entry[0][3]
        text = "Chromosome number: " + chromosome_number
        # length of the gene
        length = find_length_gene(data_entry)
        text_length = "Length of the gene: " + length
        # count amount of exons
        amount = count_amount_exons(self.data.name_file_gff3, state)
        text_exons = "Amount of exons on this gene: " + str(amount)

        # reset state so it can be adjusted,
        # wipe text field clean,
        # set state to disabled so it cannot be changed.
        self.text_chromo.config(state="normal")
        self.text_chromo.delete("1.0", "end")
        self.text_chromo.insert("end", text + "\n" + text_length
                                + "\n" + text_exons)
        self.text_chromo.config(state="disabled")


class Data:
    def __init__(self):
        self.name_file = "TAIR10_pep_20101214.fa"
        self.name_file_gff3 = "TAIR10_GFF3_genes.gff"

        self.headers, self.seqs = read_file_fasta(self.name_file)
        self.matches = consensus(self.headers, self.seqs)
        self.entry_match = open_file(self.name_file_gff3, self.matches)


main()
