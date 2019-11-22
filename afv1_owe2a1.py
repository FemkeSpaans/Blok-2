# Naam: Femke Spaans
# Datum: 12/11/2019
# Versie: 1

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.


def main():
    open_bestand()


def open_bestand():
    """bestand opgeven,
        lees_inhoud,
        if zoekwoord in headers,
        check_is_dna.
        """

    try:
        bestand_naam = "GCF_000164845.2_Vicugna_pacos-2.0.2_rna (1).fna"
        headers, seqs = lees_inhoud(bestand_naam)
        if 'fasta' in bestand_naam or 'fna' in bestand_naam or 'fa' in bestand_naam:
            zoekwoord = input("Geef een zoekwoord op: ")
            for i in range(len(headers)):
                if zoekwoord in headers[i]:
                    print("Header:", headers[i])
                    try:
                        check_is_dna = is_dna(seqs[i])
                        if check_is_dna:
                            print("Sequentie is DNA")
                            knipt(seqs[i])
                        else:
                            print("Sequentie is geen DNA. Er is iets fout gegaan.")
                    except TypeError:
                        main()
        else:
            print("Geen fasta bestand")
    except FileNotFoundError:
        print("Dit bestand bestaat niet in de map.")


def lees_inhoud(bestands_naam):
    """
    :param bestands_naam: openen van bestand,
    for loop line.strip,
    if statement to append seqs
    :return: headers, seqs
    """
    bestand = open(bestands_naam)
    headers = []
    seqs = []
    seq = ""
    for line in bestand:
        line = line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
    return headers, seqs


def is_dna(seq):
    """
    aantal letters tellen,
    aantal letter vergelijken met de lengte van de sequentie,
    :param seq:
    :return: dna
    """
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g
    if total == len(seq):
        dna = True
    return dna


def knipt(alpaca_seq):
    """bestand openen(enzymen.txt)
    :param alpaca_seq:
    """
    try:
        try:
            bestand = open("enzymen.txt")
            for line in bestand:
                naam, seq = line.split(" ")
                seq = seq.strip().replace("^", "")
                if seq in alpaca_seq:
                    print(naam, "knipt in sequentie")
        except ValueError:
            print("Er is iets mis met je enzymen bestand.")
    except FileNotFoundError:
        print("Dit bestand bestaat niet in deze map.")


main()
