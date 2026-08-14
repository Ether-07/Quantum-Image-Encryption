# Final Results Record

All values below are taken from the final experiment outputs supplied for the project.

## Functional validation

- Images identical: **True**
- Maximum pixel difference: **0**
- Total absolute difference: **0**
- Wrong key recovered original: **False**
- Wrong-key total absolute difference: **1,045,214**

## Phase 6

- Original entropy: **6.908056**
- Encrypted entropy: **7.988329**
- Original horizontal correlation: **0.970758**
- Original vertical correlation: **0.951356**
- Original diagonal correlation: **0.934675**
- Encrypted horizontal correlation: **0.000958**
- Encrypted vertical correlation: **0.007067**
- Encrypted diagonal correlation: **-0.000085**
- NPCR: **99.707031%**
- UACI: **33.590519%**
- Key sensitivity NPCR: **99.566650%**
- Key sensitivity UACI: **33.672258%**

## Key-space

| Length | Key space | Entropy |
|---:|---:|---:|
| 8 | 6095689385410816 | 52.44 bits |
| 12 | 475920314814253376475136 | 78.66 bits |
| 16 | 37157429083410091685945089785856 | 104.87 bits |
| 20 | 2901062411314618233730627546741369470976 | 131.09 bits |
| 32 | 1380674536088650126365233338290905239051505147118049339937652736 | 209.75 bits |

## Phase 7

- Encryption: **27.882508 s**
- Decryption: **38.769167 s**
- Total: **66.651674 s**

### Quantum performance

- 128 bits: **0.020762 s**, **6165.08 bits/s**
- 512 bits: **0.045600 s**, **11228.17 bits/s**
- 1024 bits: **0.084818 s**, **12072.85 bits/s**
- 4096 bits: **0.361393 s**, **11333.92 bits/s**
- 8192 bits: **0.726578 s**, **11274.77 bits/s**

### Scalability

- 128×128: **50.790058 s total**
- 256×256: **217.319936 s total**
- 512×512: **1914.999096 s total**

### Noise impact

- 0.1%: **0.003000 TVD**
- 0.5%: **0.008000 TVD**
- 1%: **0.023000 TVD**
- 2%: **0.039000 TVD**
- 5%: **0.117000 TVD**
