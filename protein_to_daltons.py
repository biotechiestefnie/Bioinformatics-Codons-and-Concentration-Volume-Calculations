"""

File: protein_to_daltons.py
Author: Stefanie Moreno

# Problem: Calculate PKCβ-1 MW in kDa (671 aa, 110 Da/aa), and hardcode its DNA sequence.
"""

# Input: hardcoded sequence for protein PKCßβ-1 from species ''R. norvegicus''
# Output: length in aa and mw of protein PKCβß-1 in kDa printed to screen

def main():
    """
    Calculate and print the molecular weight of PKCβ-1 in kDa.
    """

    # Hardcode the sequence for PKCβß-1 by assigning the sequence to a variable within the module
    protein_sequence = (
        "MADPAAGPPPSEGEESTVRFARKGALRQKNVHEVKNHKFTARFFKQPTFCSHCTDFIWGFGKQGFQCQV"
        "CCFVVHKRCHEFVTFSCPGADKGPASDDPRSKHKFKIHTYSSPTFCDHCGSLLYGLIHQGMKCDTCMMN"
        "VHKRCVMNVPSLCGTDHTERRGRIYIQAHIDREVLIVVVRDAKNLVPMDPNGLSDPYVKLKLIPDPKS"
        "ESKQKTKTIKCSLNPEWNETFRFQLKESDKDRRLSVEIWDWDLTSRNDFMGSLSFGISELQKAGVDGW"
        "FKLLSQEEGEYFNVPVPPEGSEGNEELRQKFERAKIGQGTKAPEEKTANTISKFDNNGNRDRMKLTDF"
        "NFLMVLGKGSFGKVMLSERKGTDELYAVKILKKDVVIQDDDVECTMVEKRVLALPGKPPFLTQLHSCF"
        "QTMDRLYFVMEYVNGGDLMYHIQQVGRFKEPHAVFYAAEIAIGLFFLQSKGIIYRDLKLDNVMLDSEG"
        "HIKIADFGMCKENIWDGVTTKTFCGTPDYIAPEIIAYQPYGKSVDWWAFGVLLYEMLAGQAPFEGEDE"
        "DELFQSIMEHNVAYPKSMSKEAVAICKGLMTKHPGKRLGCGPEGERDIKEHAFFRYIDWEKLERKEIQ"
        "PPYKPKARDKRDTSNFDKEFTRQPVELTPTDKLFIMNLDQNEFAGFSYTNPEFVINV"
    )

    # Calculate the number of amino acids in the protein
    num_of_amino_acids = len(protein_sequence)

    # Assign 110 daltons per amino acid to a variable
    daltons_per_amino_acid = 110

    # Calculate estimated molecular weight rounded to the hundredth decimal in kDa by converting aa to Da and Da to kDa
    molecular_weight_kilodaltons = round((daltons_per_amino_acid * num_of_amino_acids) / 1000, 2)

    # Print the results to the screen
    print(f'The length of "Protein Kinase C beta type" is: {num_of_amino_acids}')
    print(
        f'The average weight of this protein sequence in kilodaltons is: {molecular_weight_kilodaltons}')

# Call main to run protein_to_daltons starting from here when the program is executed directly
if __name__ == "__main__":
    main()
