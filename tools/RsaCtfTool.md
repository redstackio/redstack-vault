---
type: tool
verified: true
commands:
  - '[[commands/rsa-ctf-tool-dump-parameters-from-public-key]]'
tags:
  - brute-force
  - cryptography
  - known-vulnerability
platforms:
  - Linux
  - Windows
  - macOS
url: 'https://github.com/RsaCtfTool/RsaCtfTool'
validated: true
---

# RsaCtfTool

**Status**: ✓ Verified

## Overview

RsaCtfTool is a Python-based toolkit designed for attacking weak RSA keys, particularly in capture-the-flag (CTF) challenges and cryptography assessments. It deciphers ciphertext encrypted with vulnerable public keys and recovers private keys by exploiting various flaws in key generation and implementation.

## Description

RsaCtfTool supports a wide range of RSA cryptanalysis techniques, making it invaluable for offensive security operations involving cryptographic weaknesses. It is typically used in scenarios where attackers identify poorly generated RSA keys on target systems, such as in web applications, SSH keys, or encrypted communications. The tool automates complex mathematical attacks that would otherwise require manual implementation.

## Features

- Prime N detection: Identifies if the modulus N is a known prime.
- Weak public key factorization: Factors keys with weak primes.
- Wiener's attack: Exploits small private exponents using continued fractions.
- Hastad's attack: Broadcast attack for small public exponents across multiple ciphertexts.
- Small q detection: Targets when one prime factor q is very small (< 100,000).
- Common factor between ciphertext and modulus attack: Finds shared factors.
- Fermat's factorization: For primes p and q that are close.
- Gimmicky Primes method: Detects artificially generated weak primes.
- Past CTF Primes method: Specialized for historical CTF weak primes.
- Self-Initializing Quadratic Sieve (SIQS) using Yafu: Advanced factorization.
- Common factor attacks across multiple keys: Batch factorization.
- Small fractions method: When p/q is close to a small rational fraction.
- Boneh Durfee Method: For small private exponents (d < n^0.292).
- Elliptic Curve Method (ECM): Probabilistic factorization.
- Pollard's p-1: For smooth prime factors.
- Mersenne primes factorization: Specialized for Mersenne-form primes.
- Londahl's factorization: For close p and q with optimized sieving.
- Qi Cheng's unsafe primes factorization: Targets unsafe prime generation.

## Installation

### Requirements

- Python 3.6+
- pip
- Optional: Yafu for SIQS (advanced factorization)

### Install Commands

On Debian/Ubuntu/Kali:

```bash
sudo apt update
sudo apt install python3 python3-pip git
pip3 install rsa-ctf-tool
```

Alternatively, install from source:

```bash
git clone https://github.com/RsaCtfTool/RsaCtfTool.git
cd RsaCtfTool
sudo python3 setup.py install
```

On Windows/macOS: Use pip as above, or install via Git Bash/Anaconda.

## Basic Usage

```bash
RsaCtfTool.py --help
```

This displays all available options, attacks, and usage syntax.

### Common Options

| Option | Description |
|--------|-------------|
| `--publickey` | Path to the public key file (PEM format) |
| `--private` | Path to private key for decryption testing |
| `--uncipher` | Ciphertext file to decrypt |
| `--attack` | Specify attack type (e.g., wiener, fermat) |
| `--dumpkey` | Dump key parameters (n, e, etc.) |
| `-h, --help` | Show help message |
| `-v` | Verbose output |

## Examples

### Example 1: Basic Usage - Dump Key Parameters

Use the related command [[commands/rsa-ctf-tool-dump-parameters-from-public-key]] to extract modulus (n) and public exponent (e) from a public key.

### Example 2: Advanced Usage - Wiener Attack

```bash
RsaCtfTool.py --publickey id_rsa.pub --attack wiener --privatekey output.pem
```

This attempts Wiener's attack on the public key and outputs the recovered private key if successful.

### Example 3: Decrypt Ciphertext

```bash
RsaCtfTool.py --publickey pubkey.pem --uncipher ciphertext.txt --attack factordb
```

Attempts to decrypt the ciphertext using online factorization databases.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials in Files]] Password Policy Discovery (for credential recovery via crypto breaks)
- [[Brute Force]] Brute Force (for key cracking attacks)

### Tactics

- [[Persistence]] Persistence (via recovered keys for access)
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes named `RsaCtfTool.py` or `rsa_ctf_tool`.
- Network connections to factorization services (e.g., factordb.com).
- File access to .pem or .pub keys with unusual read patterns.
- High CPU usage from mathematical computations (e.g., factorization).

## Related Procedures

No related procedures currently linked.

## Related Tools

- [[commands/factor]] (built-in factorization utilities)
- [[tools/Yafu]] (for advanced SIQS)

## References

- Official GitHub: https://github.com/RsaCtfTool/RsaCtfTool
- RSA Cryptanalysis resources: https://www.cryptologie.net/
