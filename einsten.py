#rafael castillo
#cs50 python
#programs set 0 problem #4



# Constants
speed_of_light = 3e8  # Speed of light in meters per second

# Function to calculate energy from mass
def calculate_energy(mass_kg):
    energy_joules = mass_kg * speed_of_light**2
    return int(energy_joules)

# Function to get user input and calculate energy
def main():
    # Prompt the user for mass in kilograms
    mass_kg = int(input("Enter mass in kilograms: "))

    # Calculate energy using E=mc^2
    energy_joules = calculate_energy(mass_kg)

    # Print the result
    print(f"The equivalent energy is {energy_joules} Joules.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
