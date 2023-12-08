'''
    CS50p Week 0, problem set 0: Einstein
    The Set up: Even if you haven/'t studied physics (recently or ever!), you might have heard that
    E = mc^2, wherein
        E represents energy (measured in Joules),
        m represents mass (measured in kilograms), and
        c represents the speed of light (measured approximately as 300000000 meters per second),
    per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

    The Goal: In a file called einstein.py, implement a program in Python that prompts the user
    for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.
    Assume that the user will input an integer.
'''

def mass_to_energy(m):
    '''
    input = integer representing mass in kg
    function: convert mass to energy equivalent using E=mc^2
    return: integer value of the approximate energy in Joules
    '''
    c = 300000000
    e = m * c**2
    return round(e)


def main():
    '''
        prompts user for a mass in Kilograms
        uses mass_to_energy to return the integer energy value that is
        approximately equivalent to the user supplied mass value
        prints the value of energy in Joules
    '''

    # prompt user for mass and convert string to integer
    mass = int(input("Enter a mass in Kilograms, and I'll return the approximate energy in Joules: "))

    energy = mass_to_energy(mass)

    print(f"Energy: {energy}J")

main()