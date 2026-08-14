import argparse
import os

from src.encryption.pipeline import (
    encrypt_file,
    decrypt_file
)


def encrypt_command(
    input_path,
    output_path,
    key
):
    print("Encrypting...")

    encrypt_file(
        input_path,
        output_path,
        key
    )

    print(
        f"Encrypted image saved to: "
        f"{output_path}"
    )


def decrypt_command(
    input_path,
    output_path,
    key
):
    print("Decrypting...")

    decrypt_file(
        input_path,
        output_path,
        key
    )

    print(
        f"Decrypted image saved to: "
        f"{output_path}"
    )


def main():

    parser = argparse.ArgumentParser(
        description=(
            "Quantum-Inspired Image "
            "Encryption Using Quantum Circuits"
        )
    )

    subparsers = (
        parser.add_subparsers(
            dest="command",
            required=True
        )
    )


    # ----------------------------------------
    # Encrypt
    # ----------------------------------------

    encrypt_parser = (
        subparsers.add_parser(
            "encrypt",
            help="Encrypt an image"
        )
    )

    encrypt_parser.add_argument(
        "input",
        help="Input image path"
    )

    encrypt_parser.add_argument(
        "output",
        help="Encrypted image path"
    )

    encrypt_parser.add_argument(
        "--key",
        required=True,
        help="Encryption key"
    )


    # ----------------------------------------
    # Decrypt
    # ----------------------------------------

    decrypt_parser = (
        subparsers.add_parser(
            "decrypt",
            help="Decrypt an image"
        )
    )

    decrypt_parser.add_argument(
        "input",
        help="Encrypted image path"
    )

    decrypt_parser.add_argument(
        "output",
        help="Decrypted image path"
    )

    decrypt_parser.add_argument(
        "--key",
        required=True,
        help="Decryption key"
    )


    args = parser.parse_args()


    if args.command == "encrypt":

        encrypt_command(
            args.input,
            args.output,
            args.key
        )


    elif args.command == "decrypt":

        decrypt_command(
            args.input,
            args.output,
            args.key
        )


if __name__ == "__main__":
    main()