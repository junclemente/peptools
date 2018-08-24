import re

# Source for M.W.: American Peptide Company
# Dict of AA with D forms for lowercase
aa_dict = {'G': ['Gly', 'Glycine', 'nonpolar', 75.07],
           'A': ['Ala', 'Alanine', 'nonpolar', 89.09],
           'V': ['Val', 'Valine', 'nonpolar', 117.15],
           'L': ['Leu', 'Leucine', 'nonpolar', 131.17],
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
           'Q': ['Gln', 'Glutamine', 'polar', 146.14],
           'D': ['Asp', 'Aspartic acid', 'negative', 133.1],
           'E': ['Glu', 'Glutamic acid', 'negative', 147.14],
           'K': ['Lys', 'Lysine', 'positive', 146.19],
           'R': ['Arg', 'Arginine', 'positive', 174.20],
           'H': ['His', 'Histidine', 'positive', 155.15],
           # 'g': ['DGly', 'D-Glycine', 'nonpolar', 75.07],  # Does not exist
           'a': ['DAla', 'D-Alanine', 'nonpolar', 89.09],
           'v': ['DVal', 'D-Valine', 'nonpolar', 117.15],
           'l': ['DLeu', 'D-Leucine', 'nonpolar', 131.17],
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
           'q': ['DGln', 'D-Glutamine', 'polar', 146.14],
           'd': ['DAsp', 'D-Aspartic acid', 'negative', 133.1],
           'e': ['DGlu', 'D-Glutamic acid', 'negative', 147.14],
           'k': ['DLys', 'D-Lysine', 'positive', 146.19],
           'r': ['DArg', 'D-Arginine', 'positive', 174.20],
           'h': ['DHis', 'D-Histidine', 'positive', 155.15]}


class PeptideChain:

    def __init__(self, aa_chain, d_forms = False, convert3 = False):

        # removes all spaces from AA chain
        aa_chain = str(aa_chain)
        aa_chain = aa_chain.replace(' ', '')

        if d_forms:
          self.peptide = aa_chain  # peptide chain entered without spaces
        else:
          self.peptide = aa_chain.upper()
        self.d_forms = d_forms
        self.convert3 = convert3

    def make_peptide_chain(self):

        peptide1 = ''
        # Creates peptide 1 letter representation.
        if not self.convert3:
            if not self.d_forms:
                peptide1 = self.peptide.upper()

        print peptide1

        # Convert3 is true, therefore creates peptide 1 letter representation from
        # 3 letter representation
        if self.convert3:
            peptide_list = re.findall('([A-Z][a-z][a-z])', self.peptide)

            for aa in peptide_list:
                for key, value in aa_dict.items():
                    if aa == value[0]:
                        peptide1 += key

        return peptide1

    def peptide_chain(self):

        if not self.convert3:
            # Convert to all uppercase unless D-forms of AA needed
            if not self.d_forms:
                self.peptide = self.peptide.upper()

            return self.peptide
        else:
            peptide3_list = ''
            peptide3_list = re.findall('([A-Z][a-z][a-z])', self.peptide)
            print self.peptide
            print peptide3_list
            return peptide3_list


    def convert1_to_3(self):

        # Converts 1-letter representation to 3-letter representation AA
        peptide3 = ''

        try:
            for aa in self.peptide:
                peptide3 += aa_dict[aa][0] + '-'

            peptide3 = peptide3[:-1]

        # If aa does not exist in aa_dict, KeyError is returned
        except KeyError:
            peptide3 = "Error! \'" + aa + "\' does not exist.\
                                 Please check your peptide. "

        return peptide3

    def peptide_length(self):
        return len(self.peptide)

    def peptide_stats(self):
        peptide_stats = {}

        try:
            for aa in self.peptide:
                if aa_dict[aa][1] not in peptide_stats:
                    peptide_stats[aa_dict[aa][1]] = 1
                else:
                    peptide_stats[aa_dict[aa][1]] += 1

        except KeyError:
            peptide_stats = {}

        return peptide_stats

    def mo_weight(self):
        mw = 0
        mw_water = 18.01528

        try:
            for aa in self.peptide:
                mw += aa_dict[aa][3]

            mw = mw - ((len(self.peptide)-1) * mw_water)

        except KeyError:
            mw = 0

        return mw
