from config import aa_dict


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
