# Dict of AA with D forms for lowercase
# Source for M.W.: www.sigmaaldrich.com
aa_dict = {'G': ['Gly', 'Glycine', 'nonpolar', 75.07],
           'A': ['Ala', 'Alanine', 'nonpolar', 89.10],
           'V': ['Val', 'Valine', 'nonpolar', 117.15],
           'L': ['Leu', 'Leucine', 'nonpolar', 131.18],
           'I': ['Ile', 'Isoleucine', 'nonpolar', 131.18],
           'M': ['Met', 'Methionine', 'nonpolar', 149.21],
           'F': ['Phe', 'Phenylalanine', 'nonpolar', 165.19],
           'W': ['Trp', 'Tryptophan', 'nonpolar', 204.23],
           'P': ['Pro', 'Proline', 'nonpolar', 115.13],
           'S': ['Ser', 'Serine', 'polar', 105.09],
           'T': ['Thr', 'Threonine', 'polar', 119.12],
           'C': ['Cys', 'Cysteine', 'polar', 121.16],
           'Y': ['Tyr', 'Tyrosine', 'polar', 181.19],
           'N': ['Asn', 'Asparagine', 'polar', 132.12],
           'Q': ['Gln', 'Glutamine', 'polar', 146.15],
           'D': ['Asp', 'Aspartic acid', 'negative', 133.11],
           'E': ['Glu', 'Glutamic acid', 'negative', 147.13],
           'K': ['Lys', 'Lysine', 'positive', 146.19],
           'R': ['Arg', 'Arginine', 'positive', 174.20],
           'H': ['His', 'Histidine', 'positive', 155.16],
           'g': ['DGly', 'D-Glycine', 'nonpolar', 75.07],
           'a': ['DAla', 'D-Alanine', 'nonpolar', 89.10],
           'v': ['DVal', 'D-Valine', 'nonpolar', 117.15],
           'l': ['DLeu', 'D-Leucine', 'nonpolar', 131.18],
           'i': ['DIle', 'D-Isoleucine', 'nonpolar', 131.18],
           'm': ['DMet', 'D-Methionine', 'nonpolar', 149.21],
           'f': ['DPhe', 'D-Phenylalanine', 'nonpolar', 165.19],
           'w': ['DTrp', 'D-Tryptophan', 'nonpolar', 204.23],
           'p': ['DPro', 'D-Proline', 'nonpolar', 115.13],
           's': ['DSer', 'D-Serine', 'polar', 105.09],
           't': ['DThr', 'D-Threonine', 'polar', 119.12],
           'c': ['DCys', 'D-Cysteine', 'polar', 121.16],
           'y': ['DTyr', 'D-Tyrosine', 'polar', 181.19],
           'n': ['DAsn', 'D-Asparagine', 'polar', 132.12],
           'q': ['DGln', 'D-Glutamine', 'polar', 146.15],
           'd': ['DAsp', 'D-Aspartic acid', 'negative', 133.11],
           'e': ['DGlu', 'D-Glutamic acid', 'negative', 147.13],
           'k': ['DLys', 'D-Lysine', 'positive', 146.19],
           'r': ['DArg', 'D-Arginine', 'positive', 174.20],
           'h': ['DHis', 'D-Histidine', 'positive', 155.16]}

def convert_1_to_3(aa_chain, d_forms):
    '''
    This function takes an aa_chain in a 1-letter representation and
    converts it to a 3-letter AA representation. The format for the 3-letter
    AA representation will be the 3-letter AA name with hyphens in between
    without any spaces.
    '''

    # Removes all whitespaces from aa_chain
    aa_chain = str(aa_chain)
    aa_chain = aa_chain.replace(' ', '')

    aa_length = len(aa_chain)

    # If D forms of AA are not needed, converts any lowercase to uppercase
    if not d_forms:
        aa_chain = aa_chain.upper()

    aa_chain3 = ''  # Converted aa_chain to 3-letter representation
    aa_stats = {}  # Dict of AA used and how many of each in aa_chain

    for aa in aa_chain:
        # searches AA in aa_dict and appends to aa_chain3 if it exists
        # if not found, process stops and an error is returned
        if aa in aa_dict:
            aa_chain3 += aa_dict[aa][0] + '-'

            # adds AA to aa_stats and calculates the total number of times
            # each AA is used
            if aa_dict[aa][1] not in aa_stats:
                aa_stats[aa_dict[aa][1]] = 1
            else:
                aa_stats[aa_dict[aa][1]] += 1
        else:
            aa_chain3 = "Error! \'" + aa + "\' does not exist. \
                            Please check your entry."
            break

    # Removes hyphen after last AA
    aa_chain3 = aa_chain3[:-1]

    result = {'chain': aa_chain,  # original AA chain being converted
              'length': aa_length,  # length of AA chain
              'conversion': aa_chain3,  # AA chain in 3-letter representation
              'aa_stats': aa_stats  # Stats of AA chain
              }

    return result
