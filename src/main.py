import subprocess
import colorama

colorama.init()

PHOTOSHOP_PATH = r"C:\Program Files\Adobe\Adobe Photoshop 2024\Photoshop.exe"
PREMIERE_PATH = r"C:\Program Files\Adobe\Adobe Premiere Pro 2024\Adobe Premiere Pro.exe"
ENCODER_PATH = (
    r"C:\Program Files\Adobe\Adobe Media Encoder 2024\Adobe Media Encoder.exe"
)
AUDITION_PATH = r"C:\Program Files\Adobe\Adobe Audition 2024\Adobe Audition.exe"


def add_inbound(path, program):
    add_inbound_rule = f'netsh advfirewall firewall add rule name="Block Inbound {program}" dir=in action=block program="{path}" enable=yes'
    try:
        subprocess.run(add_inbound_rule, shell=True, check=True)
        print("Firewall rules added correctly.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error adding firewall rules: {e}")
        return False


def add_outbound(path, program):
    add_outbound_rule = f'netsh advfirewall firewall add rule name="Block Outbound {program}" dir=out action=block program="{path}" enable=yes'
    try:
        subprocess.run(add_outbound_rule, shell=True, check=True)
        print("Firewall rules added correctly.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error adding firewall rules: {e}")
        return False


def block_program(path, program):
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
    option = str(input("Your option: "))
    success = False

    if option == "1":
        success = block_program(PHOTOSHOP_PATH, "Photoshop")
    elif option == "2":
        success = block_program(PREMIERE_PATH, "Adobe Premiere Pro")
    elif option == "3":
        success = block_program(ENCODER_PATH, "Adobe Media Encoder")
    elif option == "4":
        success = block_program(AUDITION_PATH, "Adobe Audition")
    elif option == "5":
        success = all(
            [
                block_program(PHOTOSHOP_PATH, "Photoshop"),
                block_program(PREMIERE_PATH, "Adobe Premiere Pro"),
                block_program(ENCODER_PATH, "Adobe Media Encoder"),
                block_program(AUDITION_PATH, "Adobe Audition"),
            ]
        )
    else:
        print("Enter one of the options from above please!")
        continue

    if success:
        print(colorama.Fore.GREEN + "Successfully Blocked!")
    break
