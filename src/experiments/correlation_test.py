from PIL import Image

from src.analysis.correlation import (
    calculate_correlations
)


original = Image.open(
    "images/test.png"
).convert("L")

encrypted = Image.open(
    "results/phase5_encrypted.png"
).convert("L")


original_results = calculate_correlations(
    original
)

encrypted_results = calculate_correlations(
    encrypted
)


print("ORIGINAL IMAGE")
print("----------------")

for direction, value in (
    original_results.items()
):

    print(
        f"{direction:10}: "
        f"{value:.6f}"
    )


print("\nENCRYPTED IMAGE")
print("----------------")

for direction, value in (
    encrypted_results.items()
):

    print(
        f"{direction:10}: "
        f"{value:.6f}"
    )