import time

from src.encryption.quantum_keystream import (
    generate_quantum_bits
)


KEY = "QuantumImageKey123"


BIT_SIZES = [
    128,
    512,
    1024,
    4096,
    8192
]


print("=" * 70)
print("PHASE 7 - QUANTUM KEYSTREAM PERFORMANCE")
print("=" * 70)


for number_of_bits in BIT_SIZES:

    print("\n" + "-" * 70)

    print(
        f"Requested bits : {number_of_bits}"
    )

    start = time.perf_counter()

    bits = generate_quantum_bits(
        KEY,
        number_of_bits
    )

    elapsed = (
        time.perf_counter()
        - start
    )

    print(
        f"Generated bits : {len(bits)}"
    )

    print(
        f"Time           : "
        f"{elapsed:.6f} seconds"
    )

    if elapsed > 0:

        throughput = (
            number_of_bits
            / elapsed
        )

        print(
            f"Throughput     : "
            f"{throughput:.2f} bits/sec"
        )


print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)