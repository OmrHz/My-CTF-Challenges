from hashlib import sha256
from secret import FLAG

WELCOME_MSG = """
==============================================
  Welcome to the Super Secure Hashing Service.
==============================================
"""

def H(m):
    return [sha256(m[i:i+40]).digest().hex() for i in range(0, len(m), 40)]

def main():
    print(WELCOME_MSG)

    while True:
        print("Menu:")
        print("1 - Sign a message")
        print("2 - Verify a message")
        print("3 - Exit")

        try:
            choice = int(input("> "))
        except:
            print("Invalid input. Please enter a number.\n")
            continue

        if choice == 1:
            m = input("Enter your message: ").encode()
            combined = m + FLAG.encode()
            h = H(combined)
            print("Hash list:")
            print(h)
            print()
        elif choice == 2:
            m = input("Enter your message: ").encode()
            h_input = input("Enter your hash (comma-separated): ").split(",")
            h_input = [x.strip() for x in h_input]
            if H(m) == h_input:
                print("Signature Validated!\n")
            else:
                print("Invalid Signature!\n")
        elif choice == 3:
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
