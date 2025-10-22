---
id: 5fd5077f-1b4f-4472-adda-e8f168e932a0
name: RsaCtfTool
type: tool
verified: true
created_at: '2020-02-27T05:15:52.476710+00:00'
updated_at: '2023-05-30T19:50:10.375302+00:00'
commands:
- '[[RsaCtfTool Dump parameters from a public key]]'
tags:
- '[[Brute Force]]'
- '[[Cryptography]]'
- '[[known vulnerability]]'
---

# RsaCtfTool

**Status**: ✓ Verified

## Overview

RsaCtfTool  is used to decipher ciphertext encrypted with weak public keys, and can recover private keys using a number of vulnerabilities in key generation. Attacks: Prime N detection Weak public key factorization Wiener's attack Hastad's attack (Small public exponent attack) Small q (q < 100,000)

## Description

# Description

RsaCtfTool  is used to decipher ciphertext encrypted with weak public keys, and can recover private keys using a number of vulnerabilities in key generation.

Attacks:

- Prime N detection

- Weak public key factorization

- Wiener's attack

- Hastad's attack (Small public exponent attack)

- Small q (q < 100,000)

- Common factor between ciphertext and modulus attack

- Fermat's factorisation for close p and q

- Gimmicky Primes method

- Past CTF Primes method

- Self-Initializing Quadratic Sieve (SIQS) using Yafu

- Common factor attacks across multiple keys

- Small fractions method when p/q is close to a small fraction

- Boneh Durfee Method when the private exponent d is too small compared to the modulus (i.e d < n^0.292)

- Elliptic Curve Method

- Pollards p-1 for relatively smooth numbers

- Mersenne primes factorization

- Londahl's factorisation for close p and q

- Qi Cheng's unsafe primes factorization

# Example

# Installation

## Install on Debian/Ubuntu

## Services

- ssh
- ssh

## Commands (1)

- [[RsaCtfTool Dump parameters from a public key]]

## Tags

- [[Brute Force]]
- [[Cryptography]]
- [[known vulnerability]]
