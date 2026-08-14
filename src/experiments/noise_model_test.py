from src.noise.noise_models import (
    create_depolarizing_noise_model,
    create_readout_noise_model
)


print("=" * 70)
print("PHASE 7 - NOISE MODEL TEST")
print("=" * 70)


print("\nCreating depolarizing model...")

depolarizing_model = (
    create_depolarizing_noise_model(
        single_qubit_error=0.001,
        two_qubit_error=0.01
    )
)


print(
    "Depolarizing model created successfully."
)

print(
    depolarizing_model
)


print("\nCreating readout model...")

readout_model = (
    create_readout_noise_model(
        probability_0_to_1=0.01,
        probability_1_to_0=0.01
    )
)


print(
    "Readout model created successfully."
)

print(
    readout_model
)


print("\nNoise model test complete.")