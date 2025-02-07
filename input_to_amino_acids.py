"""

File: input_to_amino_acids.py
Author: Stefanie Moreno

Problem: Ask for gene name & bases; confirm inputs. Calculate & print total aa & MW in kDa. Alert if not multiple of 3.
"""


from sys import exit as sys_exit, stderr


def input_to_amino_acids():
    """
    Asks for gene name and sequence length, confirms inputs, calculates and prints total
    amino acids and molecular weight in kDa. Alerts if sequence length is not a multiple of 3.
    """
    gene_name = input("Please enter a name for the DNA sequence: ")
    print(f"Your sequence name is: {gene_name} ")

    sequence_length = int(input("Please enter the length of the sequence: "))
    print(f"The length of the DNA sequence is: {sequence_length} ")

    if sequence_length % 3 != 0:
        print("\n\nError: The DNA sequence length is not a multiple of 3.", file=stderr)  # print to STDERR
        sys_exit(1)  # exit the program with a non-zero value since zero means "successful termination"

    else:
        num_amino_acids = sequence_length // 3
        print(f"The length of the decoded protein is: {num_amino_acids} ")


        mw_in_kilodaltons = round((num_amino_acids * 110) / 1000, 2)
        print(f"The average weight of the protein sequence is: {mw_in_kilodaltons} ")

if __name__ == "__main__":
    input_to_amino_acids()
