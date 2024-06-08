import subprocess
import colorama
import searcher

colorama.init()  # Color!

# Main path
ADOBE_PATH = r"C:\Program Files\Adobe"
# Get the paths of adobe programs (given in alphabetical order)
program_paths = searcher.buscar_programas_adobe(ADOBE_PATH)


def add_inbound(path, program):
    """
    Function with a command to add to the firewall inbound rules the program
    """
    add_inbound_rule = f'netsh advfirewall firewall add rule name="Block Inbound {program}" dir=in action=block program="{path}" enable=yes'
    try:
        subprocess.run(add_inbound_rule, shell=True, check=True)
        print("Firewall rules added correctly.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error adding firewall rules: {e}")
        return False


def add_outbound(path, program):
    """
    Function with a command to add to the firewall outbound rules the program
    """
    add_outbound_rule = f'netsh advfirewall firewall add rule name="Block Outbound {program}" dir=out action=block program="{path}" enable=yes'
    try:
        subprocess.run(add_outbound_rule, shell=True, check=True)
        print("Firewall rules added correctly.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error adding firewall rules: {e}")
        return False


def block_program(path, program):
    """
    Function to execute both functions above and get a bool
    """
    inbound_success = add_inbound(path, program)
    outbound_success = add_outbound(path, program)
    return inbound_success and outbound_success


print(
    "Which programs do you want to add to the firewall?\n"
    "1 - Photoshop\n"
    "2 - Adobe Premiere Pro\n"
    "3 - Adobe Media Encoder\n"
    "4 - Adobe Audition\n"
    "5 - Everything"
)

while True:
    #  While loop for the options
    option = str(input("Your option: "))
    success = False

    if option == "1":
        success = block_program(program_paths[2], "Photoshop")
    elif option == "2":
        success = block_program(program_paths[3], "Adobe Premiere Pro")
    elif option == "3":
        success = block_program(program_paths[1], "Adobe Media Encoder")
    elif option == "4":
        success = block_program(program_paths[0], "Adobe Audition")
    elif option == "5":
        success = all(
            [
                block_program(program_paths[2], "Photoshop"),
                block_program(program_paths[3], "Adobe Premiere Pro"),
                block_program(program_paths[1], "Adobe Media Encoder"),
                block_program(program_paths[0], "Adobe Audition"),
            ]
        )
    else:
        print("Enter one of the options from above please!")
        continue

    if success:  # Here we use the succes with the bool return of block_program()
        print(colorama.Fore.GREEN + "Successfully Blocked!")
        input(colorama.Fore.WHITE + "Press any key to exit...")
    break
