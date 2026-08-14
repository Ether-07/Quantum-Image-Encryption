# Quantum-Inspired Image Encryption Using Quantum Circuits

## Final Academic Project Report

**Student:** Yogesh Agrawal  
**Degree:** B.Tech Computer Science and Engineering  
**Project:** Quantum-Inspired Image Encryption Using Quantum Circuits  
**Date:** August 2026

---

## Abstract

This project presents a quantum-inspired image-encryption prototype that combines classical image permutation and diffusion techniques with a quantum-circuit-derived keystream. The system is implemented in Python using Qiskit, Qiskit Aer, NumPy, Pillow, and Matplotlib.

The encryption pipeline performs image preprocessing, block permutation, local pixel permutation, quantum-circuit-based keystream generation, and modular diffusion. The system was evaluated through exact-recovery testing, wrong-key testing, histogram and entropy analysis, adjacent-pixel correlation, NPCR, UACI, key sensitivity, theoretical key-space analysis, performance measurements, image-size scalability, and simulated quantum-noise experiments.

The final experiments achieved exact recovery with the correct key, while an incorrect key failed to recover the original image. The encrypted image achieved an entropy of 7.988329 bits, with encrypted horizontal, vertical, and diagonal correlations of 0.000958, 0.007067, and -0.000085 respectively. A one-pixel plaintext modification produced an NPCR of 99.707031% and UACI of 33.590519%. Key sensitivity testing produced an NPCR of 99.566650% and UACI of 33.672258%.

The results demonstrate favorable statistical and differential characteristics for the evaluated test image. However, the implementation has significant computational overhead, especially for larger images, and should be regarded as an academic research prototype rather than a production cryptographic system.

---

# 1. Introduction

## 1.1 Background

Digital images contain substantial spatial structure. Neighboring pixels in natural images are usually highly correlated, and image histograms are often non-uniform. If encryption does not adequately disrupt these properties, statistical information about the plaintext may remain visible.

Image-encryption research therefore commonly combines confusion and diffusion mechanisms.

**Confusion** changes the relationship between plaintext positions and ciphertext positions, while **diffusion** spreads a small plaintext change across a larger portion of the ciphertext.

Quantum computing introduces a different computational model based on quantum states and quantum operations. This project investigates whether quantum circuits can be incorporated into an image-encryption architecture as a source of circuit-derived keystream material.

## 1.2 Problem Statement

The project investigates:

> Can a quantum-circuit-derived keystream be incorporated into a reversible image-encryption architecture together with classical permutation and diffusion techniques, and what statistical, differential, performance, scalability, and noise characteristics does the resulting system demonstrate?

## 1.3 Objectives

1. Develop a reversible image-encryption pipeline.
2. Integrate a quantum circuit into keystream generation.
3. Combine the quantum-derived keystream with classical permutation and diffusion.
4. Verify exact recovery using the correct key.
5. Verify failure of recovery using an incorrect key.
6. Measure ciphertext entropy and histogram characteristics.
7. Measure adjacent-pixel correlation.
8. Measure NPCR and UACI.
9. Evaluate key sensitivity.
10. Evaluate theoretical key space.
11. Measure encryption and decryption performance.
12. Evaluate image-size scalability.
13. Study the effect of simulated quantum noise.
14. Produce reproducible documentation and experimental results.

## 1.4 Scope

The implementation is an academic research prototype. It primarily evaluates grayscale images using an 8×8 block architecture. Quantum computation is primarily performed using Qiskit Aer simulation.

The project does not claim unconditional security, quantum-secure encryption, resistance to every cryptanalytic attack, or production-grade cryptographic key management.

---

# 2. Background

## 2.1 Classical Image Encryption

The project uses:

- block permutation,
- local pixel permutation,
- quantum-circuit-derived keystream generation,
- forward diffusion,
- backward diffusion.

These stages are designed to reduce spatial structure and propagate changes through the ciphertext.

## 2.2 Qubits

A qubit can be represented as:

\[
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle
\]

where:

\[
|\alpha|^2+|\beta|^2=1
\]

The project does not directly encode complete image data into a large quantum state. Instead, quantum circuits are used as a component of keystream generation.

## 2.3 Quantum Gates

The experimental circuit uses operations including:

- Hadamard gates for superposition,
- CX/CNOT gates for qubit interactions,
- parameterized rotations,
- measurement.

## 2.4 Important Terminology

The system should be described as **quantum-inspired** or **quantum-circuit-based**.

It should not be described as:

- unbreakable,
- quantum-secure,
- physically random,
- or formally proven secure.

The simulator uses deterministic seeding where reproducibility is required.

---

# 3. Proposed Architecture

```text
                         USER KEY
                            |
                            v
                      KEY DERIVATION
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
        Block Key       Pixel Key      Quantum Key
             |              |              |
             v              v              v
      Block Permutation  Local Pixel   Quantum Circuit
                        Permutation         |
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
                                      Encrypted Image
```

Decryption performs the inverse operations in reverse order.

## 3.1 Block Permutation

The image is divided into 8×8 blocks.

For a 128×128 image:

\[
(128/8)^2=256
\]

blocks are produced.

The blocks are deterministically permuted using key-derived information.

## 3.2 Local Pixel Permutation

Each 8×8 block contains 64 pixel positions. A deterministic key-derived permutation rearranges these positions.

## 3.3 Quantum-Circuit-Derived Keystream

The quantum circuit performs superposition, qubit interaction, parameterized rotations, mixing, and measurement. The resulting measurement bits are converted into bytes and used as keystream material.

## 3.4 Diffusion

The current forward diffusion uses modular feedback:

\[
C_0=(P_0+K_0)\bmod256
\]

\[
C_i=(P_i+K_i+3C_{i-1})\bmod256
\]

A reverse operation is used during decryption, followed by the corresponding inverse processing for the backward diffusion stage.

---

# 4. Implementation

## 4.1 Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| Quantum framework | Qiskit |
| Quantum simulator | Qiskit Aer |
| Numerical processing | NumPy |
| Image processing | Pillow |
| Visualization | Matplotlib |
| Environment | Python virtual environment |

## 4.2 Hardware

The complete prototype can run on a conventional computer.

Recommended:

- modern multi-core CPU,
- 8 GB RAM minimum,
- 16 GB RAM recommended for larger simulations,
- sufficient storage.

A dedicated GPU is not required.

A physical quantum computer is not required for the current project.

## 4.3 Project Structure

```text
QuantumImageEncryption/
├── README.md
├── requirements.txt
├── .gitignore
├── images/
├── results/
├── docs/
│   ├── figures/
│   └── report/
├── tests/
└── src/
    ├── analysis/
    ├── app/
    ├── encryption/
    ├── experiments/
    ├── image/
    └── noise/
```

---

# 5. Experimental Methodology

## 5.1 Functional Validation

The first requirement is exact recovery:

\[
I_{decrypted}=I_{original}
\]

The final recovery test produced:

```text
Images identical: True
Maximum pixel difference: 0
Total absolute difference: 0
```

The wrong-key test produced:

```text
Wrong key recovered original: False
Total absolute difference: 1045214
```

This establishes that the implemented pipeline is reversible with the correct key and does not trivially recover the plaintext with the tested incorrect key.

## 5.2 Security Evaluation

The following metrics were evaluated:

- Shannon entropy,
- pixel correlation,
- NPCR,
- UACI,
- key sensitivity,
- theoretical key space.

## 5.3 Performance Evaluation

The following were measured:

- complete encryption time,
- complete decryption time,
- quantum keystream generation time,
- quantum keystream throughput,
- image-size scalability.

## 5.4 Quantum Noise Evaluation

The quantum circuit was evaluated under simulated noise using several noise levels. Total variation distance was used to quantify the difference between ideal and noisy measurement distributions.

---

# 6. Security Analysis

## 6.1 Entropy

Shannon entropy is:

\[
H(X)=-\sum_i p_i\log_2(p_i)
\]

For an 8-bit grayscale image, the theoretical maximum is 8 bits.

| Image | Entropy |
|---|---:|
| Original | 6.908056 |
| Encrypted | **7.988329** |

The encrypted entropy is very close to the theoretical maximum. This indicates that the encrypted image has a substantially more uniform intensity distribution than the original test image.

However, entropy alone does not establish cryptographic security.

## 6.2 Pixel Correlation

| Direction | Original | Encrypted |
|---|---:|---:|
| Horizontal | 0.970758 | **0.000958** |
| Vertical | 0.951356 | **0.007067** |
| Diagonal | 0.934675 | **-0.000085** |

The original image shows strong spatial correlation. After encryption, all three measured correlations are close to zero.

This indicates that the encryption pipeline substantially disrupts linear relationships between neighboring pixels.

## 6.3 NPCR

The Number of Pixels Change Rate is:

\[
NPCR=
\frac{\sum D(i,j)}{W\times H}\times100
\]

where \(D(i,j)\) is 1 when two corresponding ciphertext pixels differ and 0 otherwise.

The one-pixel-change experiment produced:

\[
\boxed{NPCR=99.707031\%}
\]

This indicates that a one-intensity change in one plaintext pixel caused changes in almost all ciphertext pixels for the tested image.

## 6.4 UACI

The Unified Average Changing Intensity is:

\[
UACI=
\frac{1}{W\times H}
\sum
\frac{|C_1(i,j)-C_2(i,j)|}{255}
\times100
\]

The experiment produced:

\[
\boxed{UACI=33.590519\%}
\]

NPCR and UACI should be interpreted together rather than as independent proofs of security.

## 6.5 Key Sensitivity

Two nearly identical keys were tested.

The key-sensitivity experiment produced:

| Metric | Result |
|---|---:|
| NPCR | **99.566650%** |
| UACI | **33.672258%** |

The large ciphertext difference indicates strong sensitivity to the tested key modification.

## 6.6 Key-Space Analysis

The experiment produced:

| Key length | Key space | Theoretical entropy |
|---:|---:|---:|
| 8 | 6095689385410816 | 52.44 bits |
| 12 | 475920314814253376475136 | 78.66 bits |
| 16 | 37157429083410091685945089785856 | 104.87 bits |
| 20 | 2901062411314618233730627546741369470976 | 131.09 bits |
| 32 | 1380674536088650126365233338290905239051505147118049339937652736 | 209.75 bits |

For a character set of size \(N\) and key length \(L\):

\[
K=N^L
\]

and:

\[
B=L\log_2(N)
\]

These are theoretical combinatorial values. They should not be interpreted as the effective entropy of a human-selected password.

Hashing a weak password does not magically increase its original entropy. A production implementation should use a dedicated password-based key derivation function and a clearly defined key-generation policy.

---

# 7. Performance Analysis

## 7.1 Complete Encryption/Decryption

| Measurement | Time |
|---|---:|
| Encryption | **27.882508 s** |
| Decryption | **38.769167 s** |
| Total | **66.651674 s** |

The current implementation has substantial computational overhead. This is an important limitation rather than a performance advantage.

## 7.2 Quantum Keystream Performance

Final measured results:

| Bits requested | Time | Throughput |
|---:|---:|---:|
| 128 | 0.020762 s | 6165.08 bits/s |
| 512 | 0.045600 s | 11228.17 bits/s |
| 1024 | 0.084818 s | 12072.85 bits/s |
| 4096 | 0.361393 s | 11333.92 bits/s |
| 8192 | 0.726578 s | 11274.77 bits/s |

For larger requests, throughput stabilizes around 11,000–12,000 bits/s under the recorded test environment. The lower throughput for the 128-bit request is consistent with fixed circuit/simulator overhead becoming a larger proportion of a short run.

## 7.3 Image Scalability

The scalability experiment recorded total execution time:

| Image size | Total time |
|---|---:|
| 128×128 | 50.790058 s |
| 256×256 | 217.319936 s |
| 512×512 | 1914.999096 s |

The scalability experiment did not separately record encryption and decryption times, so those values are not fabricated.

The 512×512 experiment required approximately 31.9 minutes, demonstrating substantial computational overhead as image dimensions increase.

This is a major area for future optimization, including circuit optimization, caching, batching, parallel execution, and more efficient image processing.

---

# 8. Quantum Noise Analysis

## 8.1 Purpose

Quantum systems are affected by noise. Simulation makes it possible to investigate the sensitivity of the quantum-circuit output without requiring physical quantum hardware.

## 8.2 Noise Levels

The experiment evaluated:

```text
0.1%
0.5%
1%
2%
5%
```

## 8.3 Total Variation Distance

The total variation distance between two probability distributions is:

\[
TVD(P,Q)=
\frac{1}{2}\sum_x|P(x)-Q(x)|
\]

A value of zero indicates identical distributions.

The measured results were:

| Noise level | TVD |
|---:|---:|
| 0.1% | 0.003000 |
| 0.5% | 0.008000 |
| 1% | 0.023000 |
| 2% | 0.039000 |
| 5% | 0.117000 |

The results show an increasing difference between the ideal and noisy distributions as the modeled error rate increases.

This experiment demonstrates sensitivity of the circuit output to simulated noise. It should **not** be interpreted as evidence that quantum noise improves encryption security.

---

# 9. Results Summary

| Category | Metric | Final result |
|---|---|---:|
| Recovery | Exact recovery | **True** |
| Recovery | Maximum pixel difference | **0** |
| Wrong key | Original recovered | **False** |
| Security | Original entropy | **6.908056** |
| Security | Encrypted entropy | **7.988329** |
| Security | Encrypted horizontal correlation | **0.000958** |
| Security | Encrypted vertical correlation | **0.007067** |
| Security | Encrypted diagonal correlation | **-0.000085** |
| Security | NPCR | **99.707031%** |
| Security | UACI | **33.590519%** |
| Key sensitivity | NPCR | **99.566650%** |
| Key sensitivity | UACI | **33.672258%** |
| Performance | Encryption | **27.882508 s** |
| Performance | Decryption | **38.769167 s** |
| Performance | Total | **66.651674 s** |
| Noise | TVD at 0.1% | **0.003000** |
| Noise | TVD at 5% | **0.117000** |

---

# 10. Discussion

The final experiments demonstrate three important characteristics.

First, the implementation is functionally reversible. The correct-key decryption produced an exact pixel-level match with the original image, while the tested wrong key did not recover the plaintext.

Second, the encrypted image demonstrated strong statistical disruption for the evaluated test image. Entropy increased from 6.908056 to 7.988329 bits, and all measured adjacent-pixel correlations decreased to values very close to zero. The NPCR and UACI experiments also demonstrated strong differential propagation for the tested one-pixel modification.

Third, the performance measurements reveal a significant trade-off. Quantum-circuit simulation introduces substantial computational cost. The 512×512 scalability experiment required approximately 1915 seconds, showing that the current prototype is not optimized for large images.

Therefore, the project should be viewed as an investigation of a quantum-inspired architecture rather than as a claim that quantum-circuit-based image encryption is currently faster or more secure than mature classical cryptographic systems.

---

# 11. Limitations

## 11.1 Quantum Simulation

The quantum component is primarily evaluated using Qiskit Aer simulation rather than physical quantum hardware.

## 11.2 Deterministic Simulation

Simulator seeds are used for reproducibility. This should not be confused with true physical quantum randomness.

## 11.3 Grayscale Focus

The current pipeline primarily targets grayscale images. RGB processing would require additional design and validation.

## 11.4 Key Management

The current project focuses on the encryption architecture rather than production-grade password and key management.

## 11.5 Statistical Metrics Are Not Security Proofs

Entropy, correlation, NPCR, UACI, and histogram analysis provide useful evidence about statistical behavior but do not prove resistance against all cryptanalytic attacks.

## 11.6 Computational Cost

The scalability results demonstrate substantial computational overhead, particularly for larger images.

## 11.7 No Production-Cryptography Claim

The prototype should not be used to protect sensitive real-world information. Established cryptographic constructions should be preferred for practical security.

---

# 12. Future Work

Potential extensions include:

1. RGB-native image encryption.
2. Modern password-based key derivation.
3. Authentication and integrity protection.
4. More efficient quantum circuits.
5. Reduced circuit depth.
6. Parallel and batched execution.
7. Larger image datasets.
8. Evaluation on physical quantum hardware.
9. Hardware-derived noise models.
10. Comparison with established classical encryption baselines.
11. Formal cryptanalytic analysis.
12. Optimization for large images.
13. Automated experiment reporting.
14. Evaluation across multiple image classes and datasets.

---

# 13. Conclusion

This project developed and experimentally evaluated a quantum-inspired image-encryption prototype that combines classical permutation and diffusion with quantum-circuit-derived keystream generation.

The final implementation achieved exact recovery with the correct key and failed to recover the original image using the tested wrong key. Statistical experiments showed an encrypted-image entropy of 7.988329 bits and near-zero adjacent-pixel correlations. Differential analysis produced NPCR of 99.707031% and UACI of 33.590519%, while key-sensitivity testing produced NPCR of 99.566650% and UACI of 33.672258%.

Performance experiments demonstrated that the quantum simulation component introduces significant computational overhead, especially as image dimensions increase. Quantum-noise experiments also showed increasing measurement-distribution divergence as modeled noise increased.

Overall, the project demonstrates a reproducible experimental framework for investigating quantum-circuit-derived transformations in image encryption. The results are promising from a statistical experimentation perspective, but they do not constitute a formal proof of cryptographic security. Further work is required in key management, performance optimization, RGB support, physical quantum execution, and formal cryptanalysis.

---

# Appendix A — Main Commands

Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

Encrypt:

```powershell
python -m src.app.main encrypt images/test.png results/final_encrypted.png --key QuantumImageKey123
```

Decrypt:

```powershell
python -m src.app.main decrypt results/final_encrypted.png results/final_decrypted.png --key QuantumImageKey123
```

Validate recovery:

```powershell
python -m src.experiments.phase5_recovery_test
```

Wrong-key test:

```powershell
python -m src.experiments.phase5_wrong_key_test
```

Entropy:

```powershell
python -m src.experiments.entropy_test
```

Correlation:

```powershell
python -m src.experiments.correlation_test
```

NPCR/UACI:

```powershell
python -m src.experiments.one_pixel_change_test
```

Key sensitivity:

```powershell
python -m src.experiments.key_sensitivity_test
```

Key space:

```powershell
python -m src.experiments.key_space_test
```

Full performance:

```powershell
python -m src.experiments.phase7_performance_test
```

Quantum performance:

```powershell
python -m src.experiments.quantum_performance_test
```

Image scalability:

```powershell
python -m src.experiments.image_scalability_test
```

Quantum noise:

```powershell
python -m src.experiments.quantum_noise_test
```

Noise sweep:

```powershell
python -m src.experiments.noise_sweep_test
```

Noise impact:

```powershell
python -m src.experiments.noise_impact_test
```

---

# Appendix B — Reproducibility Checklist

- [x] Correct-key recovery tested.
- [x] Exact pixel recovery confirmed.
- [x] Wrong-key test completed.
- [x] Entropy measured.
- [x] Pixel correlation measured.
- [x] NPCR measured.
- [x] UACI measured.
- [x] Key sensitivity measured.
- [x] Key-space experiment completed.
- [x] Full performance measured.
- [x] Quantum performance measured.
- [x] Image scalability measured.
- [x] Quantum noise impact measured.
- [ ] Final report figures generated and inserted.
- [ ] Fresh-environment reproduction test completed.
- [ ] Git repository reviewed for secrets.
