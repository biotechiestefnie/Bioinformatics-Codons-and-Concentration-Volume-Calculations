"""
File: input_to_amino_acids.py
Author: Stefanie Moreno

Problem: Instruct how to prepare NaCl & MgCl2 solution from user input, print to screen.
"""

def main():
    """
    Prompts user for final solution volume (mL), stock and final concentrations (mM) of NaCl and MgCl2.
    Calculates and prints the volumes of NaCl, MgCl2, and H2O needed for solution preparation.
    """
    final_vol = float(input("Please enter the final volume of the solution (mM): "))
    # use input for calculations

    # NaCl --> Use input concentrations for calculations
    nacl_stock = float(input("Please enter the NaCl stock (mM): "))
    nacl_final = float(input("Please enter the NaCl final (mM): "))

    # MgCl2 --> Use input concentrations for calculations
    mg_stock = float(input("Please enter the MgCl2 stock (mM): "))
    mg_final = float(input("Please enter the MgCl2 final (mM): "))

    # Calculations using the equation C1V1 = C2V2 to determine volume of NaCl and MgCl2 required
    step1 = f"Add {round(final_vol * (nacl_final / nacl_stock), 2)} mL NaCl"
    # Calculate mL NaCl using with stock and final NaCl concentrations, final solution volume

    step2 = f"Add {round(final_vol * (mg_final / mg_stock), 2)} mL MgCl2"
    # Calculate MgCl2 volume needed using stock and final MgCl2 concentrations, final solution volume

    step3 = f"Add H2O to achieve a final solution volume of {round(final_vol, 2)} mL and mix"

    # Print protocol to screen on separate lines by concatenating steps
    print(f"{step1}\n{step2}\n{step3}")

    # Call the main function to run the main function when the program is executed directly


if __name__ == "__main__":
    main()
