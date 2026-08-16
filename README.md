# Quantum-Inspired Image Encryption Using Quantum Circuits

<p align="center">

**A research-oriented image encryption prototype combining classical permutation/diffusion with quantum-circuit-derived keystream generation.**

</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python" alt="Python">
<img src="https://img.shields.io/badge/Qiskit-Quantum%20Computing-6929C4?style=flat-square" alt="Qiskit">
<img src="https://img.shields.io/badge/Qiskit%20Aer-Simulation-6929C4?style=flat-square" alt="Qiskit Aer">
<img src="https://img.shields.io/badge/Status-Research%20Prototype-orange?style=flat-square" alt="Status">
<img src="https://img.shields.io/badge/License-Academic%20Project-lightgrey?style=flat-square" alt="License">

</p>

---

## Table of Contents

- [Overview](#overview)
- [Research Objective](#research-objective)
- [Important Security Disclaimer](#important-security-disclaimer)
- [Architecture](#architecture)
- [How the System Works](#how-the-system-works)
- [Technology Stack](#technology-stack)
- [Hardware Requirements](#hardware-requirements)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Verifying the Installation](#verifying-the-installation)
- [Preparing Test Images](#preparing-test-images)
- [Running the Project](#running-the-project)
- [Graphical User Interface](#graphical-user-interface)
- [GUI Screenshots](#gui-screenshots)
- [GUI Visual Theme](#gui-visual-theme)
- [Command-Line Interface](#command-line-interface)
- [Running the Experiments](#running-the-experiments)
- [Understanding the Results](#understanding-the-results)
- [Quantum Noise Experiments](#quantum-noise-experiments)
- [Results and Generated Files](#results-and-generated-files)
- [Final Handoff Checklist](#final-handoff-checklist)
- [Reproducibility](#reproducibility)
- [Troubleshooting](#troubleshooting)
- [Limitations](#limitations)
- [Future Work](#future-work)
- [Academic Use](#academic-use)
- [Author](#author)

---

# Overview

**Quantum-Inspired Image Encryption Using Quantum Circuits** is an academic research project that investigates the use of quantum circuits as part of an image-encryption architecture.

The system combines classical image-encryption techniques with a quantum-circuit-derived keystream:

```text
                         Input Image
                              |
                              v
                     Image Preprocessing
                              |
                              v
                      Block Permutation
                              |
                              v
                   Local Pixel Permutation
                              |
                              v
                   Quantum Circuit Layer
                              |
                              v
                Quantum-Derived Keystream
                              |
                              v
                    Forward Diffusion
                              |
                              v
                    Backward Diffusion
                              |
                              v
                       Cipher Image
```

Decryption reverses these operations to reconstruct the original image.

The project is designed primarily as a **research and educational prototype**. It demonstrates how quantum-computing concepts can be integrated into a classical image-encryption workflow and then evaluated experimentally.

---

# Research Objective

The central research question is:

> **Can a quantum-circuit-derived keystream be incorporated into a reversible image-encryption architecture together with classical permutation and diffusion techniques, and what security, performance, and noise characteristics does the resulting system demonstrate?**

The project investigates:

- quantum-circuit-based keystream generation,
- image permutation,
- diffusion,
- key sensitivity,
- statistical security properties,
- differential attack metrics,
- performance,
- scalability,
- simulated quantum noise.

---

# Important Security Disclaimer

**This project is a research prototype. It is NOT intended to replace established cryptographic algorithms such as AES-GCM or ChaCha20-Poly1305.**

The project does **not** claim:

- unconditional security,
- quantum-secure encryption,
- resistance against every cryptanalytic attack,
- production-grade key management,
- physical quantum randomness,
- or formal cryptographic security.

Metrics such as entropy, NPCR, UACI, and pixel correlation are useful experimental indicators, but **they do not constitute a cryptographic security proof**.

The current quantum component is primarily evaluated through simulation. Therefore, this project should be described as a **quantum-inspired / quantum-circuit-based experimental encryption system**, not as a production quantum cryptosystem.

---

# Architecture

## High-Level Architecture

```text
                         +----------------+
                         |    User Key    |
                         +-------+--------+
                                 |
                                 v
                         +---------------+
                         | Key Derivation|
                         +-------+-------+
                                 |
               +-----------------+-----------------+
               |                 |                 |
               v                 v                 v
        +-------------+   +-------------+   +-------------+
        | Block Key   |   | Pixel Key   |   | Quantum Key |
        +------+------+   +------+------+   +------+------+
               |                 |                 |
               v                 v                 v
        Block Permutation   Local Permutation   Quantum Circuit
                                                   |
                                                   v
                                            Keystream Bytes
                                                   |
                                                   v
                                          Forward Diffusion
                                                   |
                                                   v
                                          Backward Diffusion
                                                   |
                                                   v
                                            Cipher Image
```

---

# How the System Works

## 1. Image Preprocessing

The input image is loaded and converted into the representation expected by the encryption pipeline.

The current research implementation primarily works with grayscale images.

---

## 2. Block Permutation

The image is divided into fixed-size blocks.

The current architecture uses:

```text
8 × 8 pixel blocks
```

For a 128 × 128 image:

```text
128 / 8 = 16 blocks per dimension
16 × 16 = 256 total blocks
```

The blocks are then deterministically rearranged using key-derived information.

This disrupts large-scale spatial relationships.

---

## 3. Local Pixel Permutation

Each 8 × 8 block contains:

```text
8 × 8 = 64 pixels
```

The positions within each block are also permuted.

This provides another layer of spatial confusion.

---

## 4. Quantum-Circuit-Derived Keystream

The quantum component uses a circuit containing operations such as:

- Hadamard gates,
- controlled-X gates,
- parameterized rotations,
- measurement.

Conceptually:

```text
Key-derived parameters
          |
          v
   +-------------+
   | Quantum     |
   | Circuit     |
   |             |
   | H / CX / RY |
   | RZ / Measure|
   +------+------+
          |
          v
    Measurement Bits
          |
          v
      Byte Stream
          |
          v
   Encryption Keystream
```

The quantum simulator currently uses deterministic seeding where reproducibility is required.

Therefore, the generated sequence should not be described as true physical quantum randomness.

---

## 5. Forward Diffusion

The current implementation uses modular feedback.

Conceptually:

```text
Plaintext
    |
    +---- Quantum Keystream
    |
    v
Forward Feedback
    |
    v
Intermediate Data
```

The current forward relation is:

\[
C_0=(P_0+K_0)\bmod256
\]

and:

\[
C_i=(P_i+K_i+3C_{i-1})\bmod256
\]

---

## 6. Backward Diffusion

A second diffusion pass operates in the opposite direction.

This creates dependencies from both directions of the flattened image data.

---

# Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Quantum Framework | Qiskit |
| Quantum Simulator | Qiskit Aer |
| Numerical Processing | NumPy |
| Image Processing | Pillow |
| Visualization | Matplotlib |
| Environment | Python `venv` |
| Platform | Windows/Linux/macOS capable, primarily developed on Windows |

---

# Hardware Requirements

## Minimum Practical Hardware

The project does not require a physical quantum computer.

Recommended:

| Component | Recommendation |
|---|---|
| CPU | Modern multi-core processor |
| RAM | 8 GB minimum, 16 GB recommended |
| Storage | 2–5 GB free |
| GPU | Not required |
| Quantum Hardware | Not required |

A dedicated GPU is not necessary for the current Qiskit Aer-based experiments.

## Physical Quantum Hardware

A physical quantum computer is an optional future extension.

The current project can be completed entirely using simulation.

---

# Project Structure

The final repository is organized into these main components:

```text
QuantumImageEncryption/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── images/
│   ├── test.png
│   ├── test_256.png
│   └── test_512.png
│
├── results/
├── docs/
│   ├── screenshots/
│   │   ├── 01_encryption_demo.png
│   │   ├── 02_security_analysis.png
│   │   ├── 03_performance.png
│   │   ├── 04_quantum_noise.png
│   │   └── 05_architecture.png
│   └── report/
├── tests/
│
└── src/
    ├── __init__.py
    ├── security_analysis.py
    │
    ├── app/
    │   ├── __init__.py
    │   └── gui.py
    │
    ├── analysis/
    │   ├── histogram.py
    │   ├── entropy.py
    │   ├── correlation.py
    │   ├── differential.py
    │   ├── key_space.py
    │   ├── metrics.py
    │   ├── quantum_metrics.py
    │   └── visualization.py
    │
    ├── encryption/
    │   ├── key_generator.py
    │   ├── quantum_keystream.py
    │   ├── permutation.py
    │   ├── block_permutation.py
    │   ├── block_transform.py
    │   ├── diffusion.py
    │   ├── encrypt.py
    │   ├── decrypt.py
    │   └── pipeline.py
    │
    ├── experiments/
    │   ├── phase5_*.py
    │   ├── phase6_*.py
    │   ├── phase7_*.py
    │   ├── quantum_performance_test.py
    │   ├── noise_model_test.py
    │   ├── quantum_noise_test.py
    │   ├── noise_sweep_test.py
    │   ├── noise_impact_test.py
    │   └── run_all.py
    │
    ├── image/
    └── noise/
        ├── __init__.py
        └── noise_models.py
```

The repository excludes the local virtual environment and Python cache files through `.gitignore`.

---

# Prerequisites

Before installing the project, install:

1. Python
2. Git
3. A code editor/IDE

Recommended:

- Python 3.10+
- Git
- Visual Studio Code

---

# Installation

## Windows

The following instructions assume the project is located at:

```text
M:\QuantumImageEncryption
```

If your project is located somewhere else, replace that path accordingly.

---

## Step 1 — Install Python

Download Python from the official Python website:

https://www.python.org/downloads/

During installation, **make sure this option is enabled**:

```text
☑ Add Python to PATH
```

After installation, open PowerShell or Command Prompt and verify:

```powershell
python --version
```

Expected:

```text
Python 3.x.x
```

Also verify pip:

```powershell
python -m pip --version
```

---

# Step 2 — Install Git

Download Git from:

https://git-scm.com/downloads

Verify:

```powershell
git --version
```

Expected:

```text
git version ...
```

Git is not required to execute the encryption system, but it is strongly recommended for project version control.

---

# Step 3 — Open the Project Directory

Open PowerShell.

Navigate to the project:

```powershell
cd M:\QuantumImageEncryption
```

Verify:

```powershell
dir
```

You should see directories/files such as:

```text
src
images
results
docs
```

---

# Step 4 — Create a Python Virtual Environment

From the project root:

```powershell
python -m venv .venv
```

This creates:

```text
QuantumImageEncryption/
└── .venv/
```

The virtual environment keeps project dependencies isolated from the global Python installation.

---

# Step 5 — Activate the Virtual Environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If using Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

When activation succeeds, your terminal should show something similar to:

```text
(.venv) M:\QuantumImageEncryption>
```

---

## PowerShell Execution Policy Error

If PowerShell displays an error about script execution being disabled, you can allow locally created scripts for your user account:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Confirm if prompted.

Then activate again:

```powershell
.venv\Scripts\Activate.ps1
```

Do not disable PowerShell security globally just to activate the environment.

---

# Step 6 — Upgrade pip

With `.venv` active:

```powershell
python -m pip install --upgrade pip
```

Verify:

```powershell
python -m pip --version
```

---

# Step 7 — Install Dependencies

If the repository contains `requirements.txt`, install from it:

```powershell
python -m pip install -r requirements.txt
```

If `requirements.txt` has not yet been generated, install the primary dependencies:

```powershell
python -m pip install qiskit qiskit-aer numpy pillow matplotlib
```

Then generate the dependency snapshot:

```powershell
python -m pip freeze > requirements.txt
```

### Important

Do not repeatedly install random packages every time an experiment fails.

If a module is missing, identify the actual import causing the problem first.

---

# Step 8 — Verify Qiskit

Run:

```powershell
python -c "import qiskit; print(qiskit.__version__)"
```

Then:

```powershell
python -c "import qiskit_aer; print(qiskit_aer.__version__)"
```

If both commands print versions without errors, the quantum environment is installed.

---

# Step 9 — Verify NumPy and Pillow

Run:

```powershell
python -c "import numpy; print(numpy.__version__)"
```

and:

```powershell
python -c "from PIL import Image; print('Pillow OK')"
```

Finally:

```powershell
python -c "import matplotlib; print(matplotlib.__version__)"
```

---

# Verifying the Installation

A successful environment should satisfy:

```text
Python        → installed
Qiskit        → importable
Qiskit Aer    → importable
NumPy         → importable
Pillow        → importable
Matplotlib    → importable
PySide6       → importable
```

You can perform a quick combined test:

```powershell
python -c "import qiskit, qiskit_aer, numpy, PIL, matplotlib, PySide6; print('Environment OK')"
```

Expected:

```text
Environment OK
```

---

# Preparing Test Images

The recommended test set contains:

```text
images/
├── test.png
├── test_256.png
└── test_512.png
```

Recommended dimensions:

```text
test.png       → 128 × 128
test_256.png  → 256 × 256
test_512.png  → 512 × 512
```

The dimensions should be compatible with the current 8×8 block-processing architecture.

For reproducible experiments, keep the test images unchanged after collecting results.

---

# Running the Project

## GUI Screenshots

The following screenshots should be added manually after running the application.

> **Screenshot location:** `docs/screenshots/`

Create this directory:

```text
docs/
└── screenshots/
```

Then save the screenshots using these exact filenames.

## 1. Encryption & Decryption

**File:**

```text
docs/screenshots/01-encryption-decryption.png
```
<img width="1920" height="1080" alt="01_encryption_demo" src="https://github.com/user-attachments/assets/b02e81da-a395-4e15-9388-8e01d67b0700" />

---

## 2. Security Analysis

**File:**

```text
docs/screenshots/02-security-analysis.png
```
<img width="1920" height="1080" alt="02_security_analysis" src="https://github.com/user-attachments/assets/c122738c-af0a-49a3-b182-fe67ecbf8cf9" />

---

## 3. Performance Analysis

**File:**

```text
docs/screenshots/03-performance.png
```
<img width="1920" height="1080" alt="03_performance" src="https://github.com/user-attachments/assets/02523389-425f-47a7-b773-89425fd2537f" />

---

## 4. Quantum / Noise Analysis

**File:**

```text
docs/screenshots/04-quantum-noise-analysis.png
```
<img width="1920" height="1080" alt="04_quantum_noise" src="https://github.com/user-attachments/assets/0a3a226c-1447-48bb-812a-a5e24d38dc15" />

---

## 5. Project Architecture / About

**File:**

```text
docs/screenshots/05-project-overview.png
```
<img width="1920" height="1080" alt="05_architecture" src="https://github.com/user-attachments/assets/30af7d76-7bc6-4db7-8ed5-c1c5c272427c" />


---

## Screenshot Checklist

Before the final GitHub release, replace every screenshot placeholder above with the actual image.

```text
[ ] 01-encryption-decryption.png
[ ] 02-security-analysis.png
[ ] 03-performance.png
[ ] 04-quantum-noise-analysis.png
[ ] 05-project-overview.png
```

The screenshots should be taken directly from the running application. Do not manually edit numerical results or fabricate values for presentation purposes.

# Graphical User Interface

The project includes a PySide6-based graphical user interface for demonstrating the complete encryption system.

Launch it from the project root with:

```powershell
python -m src.app.gui
```

The GUI is organized into five main tabs:

1. **Encryption Demo** — image selection, key entry, encryption/decryption, previews, and exact-recovery verification.
2. **Security Analysis** — entropy, pixel correlation, NPCR, UACI, histogram uniformity, and key-analysis results.
3. **Performance** — full encryption/decryption timing and quantum-keystream throughput measurements.
4. **Quantum Noise** — simulated depolarizing-noise analysis, readout-noise analysis, and Total Variation Distance (TVD).
5. **Architecture** — project overview, encryption architecture, quantum circuit description, and research limitations.

The GUI is intended to make the experimental pipeline easier to demonstrate without replacing the underlying Python modules and experiment scripts.

---

# GUI Screenshots

Screenshots are intentionally kept outside the source code and should be added under:

```text
docs/
└── screenshots/
    ├── 01_encryption_demo.png
    ├── 02_security_analysis.png
    ├── 03_performance.png
    ├── 04_quantum_noise.png
    └── 05_architecture.png
```

> **Screenshot placeholder:** Replace each placeholder below with the corresponding image after taking the final screenshots from the GUI.

### 1. Encryption Demo

**What to capture:** The complete first tab showing image selection, encryption key field, action buttons, original/grayscale/encrypted/decrypted previews, and exact recovery verification.

![Encryption Demo](docs/screenshots/01_encryption_demo.png)

---

### 2. Security Analysis

**What to capture:** The Security Analysis tab after running the analysis, including entropy, horizontal/vertical/diagonal correlation, NPCR, UACI, histogram uniformity, key analysis, and the interpretation panel.

![Security Analysis](docs/screenshots/02_security_analysis.png)

---

### 3. Performance

**What to capture:** The Performance tab with full encryption/decryption timing and the quantum-keystream performance table populated.

![Performance](docs/screenshots/03_performance.png)

---

### 4. Quantum Noise

**What to capture:** The Quantum Noise tab after running the noise analysis, including the noise sweep table and interpretation/results section.

![Quantum Noise](docs/screenshots/04_quantum_noise.png)

---

### 5. Architecture

**What to capture:** The Architecture tab showing the project overview, encryption architecture, quantum circuit component, and research limitations.

![Architecture](docs/screenshots/05_architecture.png)

---

## GUI Visual Theme

The final GUI uses a deliberate dark technical palette rather than a plain black/gray interface.

| UI Role | Palette | Purpose |
|---|---|---|
| Main background | Deep navy | Reduces visual harshness and creates depth |
| Primary accent | Cyan | Used for active tabs, section emphasis, and primary interaction |
| Secondary accent | Violet | Used for quantum/key-analysis visual emphasis |
| Success | Green | Indicates completed operations and exact recovery |
| In progress | Amber | Indicates active encryption, analysis, or testing |
| Error | Red | Indicates failed operations or validation errors |
| Panels | Blue-gray | Separates cards and sections without excessive contrast |

The goal is not to color every component. The palette uses **semantic color** so that color communicates meaning:

```text
CYAN   → primary / active
VIOLET → quantum / analytical
GREEN  → success / verified
AMBER  → running / attention
RED    → error / failure
```

This keeps the interface visually distinctive while maintaining a professional research-tool appearance.

---

# Recommended Demonstration Flow

For a clean academic/project demonstration, use the GUI in this order:

```text
1. Launch GUI
      ↓
2. Select test.png
      ↓
3. Enter encryption key
      ↓
4. Encrypt image
      ↓
5. Decrypt image
      ↓
6. Verify exact recovery
      ↓
7. Run Security Analysis
      ↓
8. Run Performance tests
      ↓
9. Run Quantum Noise analysis
      ↓
10. Open Architecture tab
```

For the strongest demonstration, take the five GUI screenshots after the corresponding tab has been populated with real results.

Do not fabricate or manually edit metric values in screenshots. Screenshots should represent actual program output from the current repository.

---

# Command-Line Interface

The CLI is located at:

```text
src/app/main.py
```

It can be executed using:

```powershell
python -m src.app.main
```

---

## Encrypt an Image

Example:

```powershell
python -m src.app.main encrypt images/test.png results/final_encrypted.png --key QuantumImageKey123
```

Expected:

```text
Encrypting...
Encrypted image saved to: results/final_encrypted.png
```

---

## Decrypt an Image

```powershell
python -m src.app.main decrypt results/final_encrypted.png results/final_decrypted.png --key QuantumImageKey123
```

Expected:

```text
Decrypting...
Decrypted image saved to: results/final_decrypted.png
```

---

# Verify Exact Recovery

After decrypting, run:

```powershell
python -m src.experiments.final_cli_validation
```

Expected:

```text
Images identical: True
Maximum pixel difference: 0
Total absolute difference: 0
```

If this test fails, **do not treat the encryption pipeline as finished**.

---

# Running the Experiments

The project is divided into experimental phases.

---

# Phase 1 — Environment and Basic Validation

Phase 1 establishes:

- Python environment
- dependencies
- basic project structure
- image loading
- initial functionality tests

Run the relevant Phase 1 experiments if you need to reproduce the initial setup.

---

# Phase 2 — Core Components

Phase 2 validates the foundational components of the system.

This includes the image and key-processing infrastructure.

---

# Phase 3 — Image Processing

Phase 3 introduces image preprocessing and transformation.

The experiments verify that image data can be loaded, transformed, and restored correctly.

---

# Phase 4 — Quantum-Circuit Integration

Phase 4 integrates quantum-circuit processing into the encryption architecture.

The quantum circuit becomes part of the keystream-generation process.

---

# Phase 5 — Encryption and Recovery

The Phase 5 tests validate the complete encryption/decryption pipeline.

## Encryption test

```powershell
python -m src.experiments.phase5_encrypt_test
```

## Recovery test

```powershell
python -m src.experiments.phase5_recovery_test
```

The recovery test should ultimately produce:

```text
Images identical: True
Maximum pixel difference: 0
Total absolute difference: 0
```

---

# Phase 6 — Security Analysis

Phase 6 evaluates statistical and differential characteristics.

Typical tests include:

```powershell
python -m src.experiments.phase6_security_analysis
```

and:

```powershell
python -m src.experiments.one_pixel_change_test
```

Depending on the final project structure, individual metric experiments may also exist.

---

# Phase 7 — Performance and Quantum Noise

Phase 7 evaluates computational cost and quantum-noise behavior.

## Full encryption performance

```powershell
python -m src.experiments.phase7_performance_test
```

## Quantum keystream performance

```powershell
python -m src.experiments.quantum_performance_test
```

## Image scalability

```powershell
python -m src.experiments.image_scalability_test
```

## Noise model

```powershell
python -m src.experiments.noise_model_test
```

## Ideal vs noisy simulation

```powershell
python -m src.experiments.quantum_noise_test
```

## Noise sweep

```powershell
python -m src.experiments.noise_sweep_test
```

## Quantitative noise impact

```powershell
python -m src.experiments.noise_impact_test
```

---

# Phase 8 — Finalization and Release

Phase 8 prepares the completed project for handoff and publication.

Completed finalization work includes:

- repository cleanup,
- removal of obsolete Phase-1 development files,
- `.gitignore` verification,
- secret/security review,
- fresh virtual-environment installation testing,
- README verification,
- GUI visual-theme and presentation review,
- GUI screenshot documentation,
- final Git review,
- final commit,
- GitHub publication/release.

The main deliverable is the runnable source repository and GUI/experiment suite. A generated PDF report or presentation is not required for the project to operate.

Supporting documentation remains under:

```text
docs/
```

---

# Final Experiment Suite

If the project contains:

```text
src/experiments/run_all.py
```

you can run:

```powershell
python -m src.experiments.run_all
```

This executes the configured experiment suite sequentially.

If one experiment fails, investigate that failure rather than assuming later results are valid.

---

# Understanding the Results

## Histogram

The encrypted histogram should ideally show less obvious correspondence with the original image's intensity distribution.

However:

> A visually uniform histogram does not prove cryptographic security.

---

## Shannon Entropy

For 8-bit grayscale images:

\[
H_{max}=8
\]

Higher entropy indicates a distribution closer to uniformity, but entropy alone is insufficient to establish security.

---

## Pixel Correlation

Natural images generally contain strong adjacent-pixel correlation.

A successful encryption transformation should substantially reduce:

- horizontal correlation,
- vertical correlation,
- diagonal correlation.

Values closer to zero indicate weaker linear correlation.

---

## NPCR

NPCR measures how many ciphertext pixels change after a small plaintext modification.

Higher differential propagation generally indicates stronger avalanche behavior.

Do not treat a single NPCR value as a security proof.

---

## UACI

UACI measures the average intensity difference between two ciphertext images.

It should be interpreted together with NPCR.

---

## Key Sensitivity

A small key modification should produce a substantially different ciphertext.

For example:

```text
QuantumImageKey123
QuantumImageKey124
```

should not produce nearly identical ciphertexts.

---

# Quantum Noise Experiments

The project uses Qiskit Aer to simulate quantum noise.

The experimental architecture is:

```text
                Quantum Circuit
                       |
             +---------+---------+
             |                   |
             v                   v
       Ideal Simulator      Noisy Simulator
             |                   |
             v                   v
       Distribution A       Distribution B
             |                   |
             +---------+---------+
                       |
                       v
                Distribution
                  Comparison
```

Noise experiments currently study:

- depolarizing gate noise,
- readout noise,
- increasing error rates,
- total variation distance.

---

# Results and Generated Files

The `results/` directory stores generated outputs from experiments and the GUI. GUI screenshots intended for repository documentation belong under `docs/screenshots/`.

Typical GUI outputs include:

```text
results/
├── gui_grayscale_preview.png
├── gui_encrypted.png
└── gui_decrypted.png
```

Experiment outputs can include encrypted/decrypted images, figures, performance results, and noise-analysis artifacts.

Do not blindly commit large collections of generated files to Git. Keep important reproducible artifacts when they are useful for demonstrating or documenting the project, and treat temporary runtime output as generated data.

---

# Reproducibility

The project is designed to make experiments reproducible.

## Use a virtual environment

Always activate:

```powershell
.venv\Scripts\Activate.ps1
```

before running experiments.

## Keep dependencies fixed

After the environment is finalized:

```powershell
python -m pip freeze > requirements.txt
```

## Keep test images unchanged

Do not replace the input image after collecting final results.

## Record hardware

When reporting performance, record:

- CPU
- RAM
- operating system
- Python version
- Qiskit version
- Qiskit Aer version

## Record experiment parameters

Document:

- key used,
- image dimensions,
- block size,
- circuit parameters,
- simulator seed,
- shot count,
- noise levels.

---

# Final Handoff Checklist

Before demonstrating or publishing the project:

```text
[ ] Fresh virtual environment can be created
[ ] requirements.txt installs successfully
[ ] Core dependencies import successfully
[ ] phase5_recovery_test passes
[ ] Wrong-key recovery test behaves as expected
[ ] Security analysis executes
[ ] Quantum performance test executes
[ ] Quantum-noise tests execute
[ ] GUI launches with python -m src.app.gui
[ ] GUI encryption/decryption works
[ ] Exact recovery reports zero pixel difference
[ ] Final screenshots captured for all five GUI tabs
[ ] Screenshot paths in README match docs/screenshots/
[ ] .venv/ and __pycache__/ are ignored by Git
[ ] No real credentials or secrets are present
```

For a professor demonstration, the primary launch command is:

```powershell
python -m src.app.gui
```

---

# Troubleshooting

## `ModuleNotFoundError: No module named 'image'`

If running modules from the project root, use package-qualified imports such as:

```python
from src.image.preprocessing import ...
```

and execute experiments using:

```powershell
python -m src.experiments.preprocessing_test
```

rather than:

```powershell
python src/experiments/preprocessing_test.py
```

The latter changes how Python resolves package imports.

---

## `ImportError: cannot import name ...`

This generally means one of:

1. The function does not exist.
2. The function name differs.
3. The wrong module is being imported.
4. Python is loading an unexpected copy of the module.
5. A circular import exists.

Check the actual function definitions in the referenced module.

Do not randomly rename imports until the problem disappears.

---

## NumPy Overflow Warnings

If you see warnings similar to:

```text
RuntimeWarning: overflow encountered in scalar subtract
```

the code is probably performing arithmetic directly on unsigned NumPy scalar types.

Convert operands to Python integers before subtraction:

```python
int(data[i]) - int(keystream[i])
```

and apply the modulus afterward.

The current diffusion implementation uses this approach.

---

## Decryption Does Not Match the Original

Run:

```powershell
python -m src.experiments.phase5_recovery_test
```

Check:

```text
Images identical
Maximum pixel difference
Total absolute difference
```

If the maximum difference is non-zero, do not proceed to security analysis.

First establish exact recovery.

---

## Noise Experiments Fail

Noise experiments are intentionally separated from the normal encryption pipeline.

Do not automatically insert a noisy simulator into:

```text
src/encryption/pipeline.py
```

A noisy quantum execution can produce different measurement outcomes and therefore different keystream material.

Noise should first be studied as an independent experiment.

---

## PowerShell Cannot Activate `.venv`

Try:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then:

```powershell
.venv\Scripts\Activate.ps1
```

---

# Screenshot Documentation

Before publishing the repository, capture the GUI at a stable final state.

Recommended screenshot rules:

- Use the same application window size for all five screenshots.
- Use the same test image and encryption key when comparing tabs.
- Run the relevant analysis before capturing result-heavy tabs.
- Do not include personal files, usernames, passwords, API keys, or unrelated desktop content.
- Keep screenshots at a readable resolution.
- Use descriptive filenames matching the paths documented above.

If a screenshot is not yet available, leave the placeholder in this README rather than inserting a broken image link.

---

# Limitations

The current project has several limitations.

## Simulation Instead of Physical Quantum Hardware

The quantum circuit is primarily executed using simulation.

Therefore, the project does not claim experimental results from a physical quantum processor.

## Deterministic Simulation

Simulator seeds are used where reproducibility is required.

This is useful experimentally but is not equivalent to physical quantum randomness.

## Grayscale Focus

The current implementation primarily focuses on grayscale images.

RGB processing can be added as future work.

## Key Management

The current project focuses on the encryption architecture rather than production-grade password and key management.

## Statistical Metrics Are Not Proofs

Entropy, NPCR, UACI, correlation, and histograms are useful indicators but do not prove resistance against all cryptanalytic attacks.

## Performance

Quantum circuit simulation can become computationally expensive as circuit size, number of shots, or generated keystream size increases.

---

# Future Work

Potential extensions include:

- RGB-native image encryption
- modern password-based key derivation
- authenticated encryption/integrity protection
- improved quantum circuit architecture
- circuit-depth optimization
- parallel execution
- larger image datasets
- physical quantum-hardware experiments
- hardware-derived noise models
- comparison with AES and other established baselines
- formal cryptanalysis
- optimized large-image processing

---

# Academic Use

This project is intended for:

- academic demonstration,
- research experimentation,
- cybersecurity/quantum-computing coursework,
- project presentations,
- experimentation with image-encryption metrics.

It should not be used to protect sensitive real-world data.

For real-world confidentiality, use established, peer-reviewed cryptographic constructions and secure key management.

---

# Author

**Yogesh Agrawal**

B.Tech Computer Science and Engineering

Project:

**Quantum-Inspired Image Encryption Using Quantum Circuits**

---

# Suggested Citation

If this project is referenced academically, describe it as:

> Ether, Yogesh Agrawal. *Quantum-Inspired Image Encryption Using Quantum Circuits*. Academic Research Prototype, 2026.

---

# License

This project is currently intended as an academic/research project.

If the repository is published publicly, add an explicit open-source license such as MIT only after deciding the licensing terms.