"""
Forage AIG Cybersecurity Program
Bruteforce script
"""
import sys
from zipfile import ZipFile


def main():
    found_pw = False
    print("[+] Beginning bruteforce ")

    with ZipFile("./enc.zip") as zf:
        with open("rockyou.txt", "rb") as f:
            # Write your logic here...
            # Iterate through password entries in rockyou.txt
            passwords = [line.decode("utf-8").strip() for line in f]

            # Attempt to extract the zip file using each password
            # Handle correct password extract versus incorrect password attempt
            for pw in passwords:
                try:
                    zf.extractall(pwd=bytes(pw, "utf-8"))

                    found_pw = True
                    print(f"****\nThe decryption key was: {pw}\n****\n")
                    sys.exit(0)
                except:
                    pass

    if found_pw == False:
        print("The decryption key is not in our records")


if __name__ == "__main__":
    main()
