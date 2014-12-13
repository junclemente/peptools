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

    conversion = ''

    for aa in aa_chain:
        if aa in aa_dict:
            conversion += aa_dict[aa][0] + '-'
        else:
            conversion = "Error! \'" + aa + "\' does not exist. Please check your entry."
            break

    conversion = conversion[:-1]

    result = {'chain': aa_chain, 'length': aa_length, 'conversion': conversion}

    return result
