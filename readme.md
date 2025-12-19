# Assignment 1: Python Variables and Data

## Description

As the first evaluation in Bioinf6200 for writing scripts and executable programs in Python, emphasis is on adherence to style guidelines as delineated by pep8, with particular focus on appropriate use of whitespace, indentation, and documentation. The programs are written within Pycharm using Python 3.11 and Pylint 2.17.7. 

In the first module, **protein_to_daltons.py**, the *R. norvegicus* analog of protein PKC beta-1 is hardcoded (as instructed) into the program. The sequence was extracted from NCBI and stripped of newline characters. This program calculates the estimated molecular weight of PKC beta-1 in kilodaltons, given 1 amino acid is an average of 110 daltons. The result of this calculation is then written to the screen.  

The second module, **input_to_amino_acids.py**, is an interactive program that asks the user for the name of a gene and the number of nucleotides in that gene. Upon each input, a confirmation statement on the screen stating the name of the gene and the number of nucleotides. The number of nucleotides input by the user is applied to calculate the number of amino acids that are in the translated protein sequence of that gene, as well as the molecular weight of the protein in kilodaltons, given 1 amino acid == 3 nucleotides, and 1 amino acid == approximately 110 daltons. If the user inputs a gene that has a nucleotide length not divisible by three, the program does not return a molecular weight, but rather, returns an error message stating "The sequence is not divisible by three!". Otherwise, the number of amino acids and molecular weight should be printed to the screen as statements below those of the gene name and number of nucleotides in the DNA sequence.

The third module, **input_to_protocol.py**, is a rewrite of the provided script converting it into an interactive program that supplies the user with instructions for making a solution of sodium chloride (NaCl) and magnesium chloride (MgCl2) of desired final volume and concentrations. The program first asks the user to input the number of mililiters wanted for the final solution, as well as the stock and final concentrations of both chemicals to be added- NaCl and MgCl2. The program then uses those input values to calculate the volume of each chemical that is required to produce a solution with the given input parameters based on the dilution theorem, C1V1 == C2V2, where C1 is the stock concentration, C2 is the final concentration, V2 is the final solution volume in milliliters, and the program solves for the input volume for each of the chemicals. The final solution volume, stock and final concentrations of each chemical, and the calculated volume of each chemical required to yield a solution based on the input parameters are then displayed on the screen for the user to reference to make their solution.  

## Getting Started

### Dependencies

* Python 3.11


* The only imported module is for the second program, **input_to_amino_acids.py**, and is 'from sys import exit as sys_exit, stderr', which is used to exit the program in the event the user inputs a nucleotide count that is not divisible by three, meaning the amino acid count would not turn out to be a whole number. The program exits without calculating the number of amino acids and molecular weight of the translated protein in that case.


* The protein sequence for PKC beta-1 was extracted from NCBI at:     for the program **protein_to_daltons.py**


* The protocol script which was converted to an interactive program in **input_to_protocol.py** was supplied by the instructor for the assignment, and I have included the original protocol script in the auxillary file **protocol_AUXILLARY_FILE.txt** for reference.


* The programs are designed to be run from the terminal of the user's operating system (OS).
* While written on macOS, the programs are basic enough to easily run on Windows or Linux as well.


* Scripts were written on PyCharm IDE version 2024.3.1.1

### Installing

1. Download the project files


2. Extract the zip file:
   * On Windows: Right-click the zip file **Assignment_1.zip** and select "Extract All..."
   * On macOS: Double-click the zip file **Assignment_1.zip** to extract it.
   * On Linux: Use the command 'unzip **Assignment_1.zip**' in the terminal.


3. Ensure that the all 3 programs (**protein_to_daltons.py**, **input_to_amino_acids.py**,
   **input_to_protocol.py**) are present in the extracted project directory.


### Executing the programs

How to run the programs:

From the terminal of your operating system, navigate to the project folder, **'Assignment_1'** and:

1. For the program **protein_to_daltons.py**, input the following:
```
python3 protein_to_daltons.py
```
the program will load and the following statements will be printed to the screen:
```
The length of "Protein Kinase C beta type is: 671
The average weight of this protein sequence in kilodaltons is: 73.81
```
2. For the program **input_to_amino_acids.py**, input:
```
python3 input_to_amino_acids.py
```
you will see on the screen:
```
Please enter a name for the DNA sequence:
```
After the colon, enter the name of a gene and hit enter. Next you will see:
```
Your sequence name is: (input)
Please enter the length of the sequence:
```
After the colon, enter the number of nucleotides in the DNA sequence for the gene you entered in question 1. Note that if you enter a number that is not divisible by 3, you will receive an error message and the program will halt. However, if you enter a number that is divisible by 3, you will see the following:
``` 
The length of the decoded protein is: (input/3)
The average weight of the protein sequence is: (input converted to kilodaltons) 
```

3. For the program **input_to_protocol.py**, please enter in your terminal the following:
``` 
python3 input_to_protocol.py
```
You will then see the following prompt:
``` 
Please enter the final volume of the solution (mM):
```
After inputting your desired final solution volume and hitting enter/return, you will see the following:
``` 
Please enter the NaCl stock (mM):
```
Here, you enter the starting concentration in mM of sodium chloride and hit enter/return. You will then see the following:
``` 
Please enter the NaCl final (mM):
```
Here, you enter the desired final concentration of sodium chloride and hit enter/return. You will then see:
``` 
Please enter the MgCl2 stock (mM):
```
Here, you enter the starting concentration of magnesium chloride in mM and hit enter/return. You will then see:
``` 
Please enter the MgCl2 final (mM):
```
Here, you enter your desired final concentration of magnesium chloride in mM for your solution and hit enter/return. You will then see:
``` 
Add (calculated) mL NaCl
Add (calculated) mL MgCl2
Add H2O to achieve a final solution volume of 1025.0 mL and mix
```


## Authors

Stefanie Moreno

moreno.st@northeastern.edu

[https://github.com/biotechiestefnie]


## Version History

* 0.1
    * Initial Release

## Acknowledgments

Instructions provided by Dr. Chelsey Leslin for Bioinformatics 6200 at Northeastern University, Spring Semester 2025.
