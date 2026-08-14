from src.encryption.key_generator import (
    derive_all_subkeys
)


key = "QuantumImageKey123"

subkeys = derive_all_subkeys(
    key
)

for name, value in subkeys.items():

    print(
        f"{name:10} : {value.hex()}"
    )