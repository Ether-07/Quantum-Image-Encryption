import subprocess
import sys


EXPERIMENTS = [
    "src.experiments.phase5_recovery_test",
    "src.experiments.phase5_wrong_key_test",
    "src.experiments.phase6_security_analysis",
    "src.experiments.phase7_performance_test",
    "src.experiments.quantum_performance_test",
    "src.experiments.noise_model_test",
    "src.experiments.quantum_noise_test",
    "src.experiments.noise_impact_test"
]


print("=" * 70)
print("QUANTUM IMAGE ENCRYPTION")
print("FINAL EXPERIMENT SUITE")
print("=" * 70)


for experiment in EXPERIMENTS:

    print("\n")
    print("=" * 70)

    print(
        f"Running: {experiment}"
    )

    print("=" * 70)


    result = subprocess.run(
        [
            sys.executable,
            "-m",
            experiment
        ]
    )


    if result.returncode != 0:

        print(
            f"\nFAILED: {experiment}"
        )

        sys.exit(
            result.returncode
        )


print("\n")
print("=" * 70)
print("ALL EXPERIMENTS COMPLETED")
print("=" * 70)