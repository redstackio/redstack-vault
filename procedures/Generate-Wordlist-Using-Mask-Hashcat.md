---
id: 79525632-d61c-4cf0-9d37-dfc430f8101f
name: Generate-Wordlist-Using-Mask-Hashcat
type: procedure
verified: true
submitted: false
created_at: '2019-10-18T01:13:23.076721+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - '[[tags/Cryptography]]'
  - '[[tags/password cracking]]'
commands:
  - '[[commands/hashcat-generate-wordlist-mask]]'
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# Generate-Wordlist-Using-Mask-Hashcat

## Summary

This procedure uses Hashcat's mask attack mode to generate a custom wordlist for brute-force operations when dictionary attacks are insufficient. By defining a mask pattern that specifies character sets for each position in the password, Hashcat can systematically produce all possible combinations, outputting them to a file for use in subsequent cracking attempts.

## Description

Mask-based wordlist generation is essential for targeted brute-force attacks on passwords with known patterns, such as PINs, short codes, or structured credentials. Hashcat's --stdout option allows it to generate candidates without attempting to crack hashes, enabling the creation of large wordlists efficiently. This approach is particularly useful in credential access scenarios where partial information about password structure is available, such as length and character types. The procedure assumes Hashcat is installed and focuses on building a wordlist with a specific mask: first character digit (?d), second special character (?s), third any byte (?b), fourth alphanumeric/special (?a). The generated wordlist can then be piped into other tools like John the Ripper or used directly in Hashcat for cracking.

## Requirements

1. Hashcat installed on a Linux or Windows system with sufficient CPU/GPU resources for generation (GPU recommended for large keyspaces).
2. Knowledge of the target password structure to define an effective mask.
3. Write access to the output directory for saving the wordlist file.
4. Optional: A rules file or custom character sets if extending beyond built-in masks.

## Defense

Defensive measures and detection strategies:

- Monitor for high CPU/GPU usage on systems, as wordlist generation can be resource-intensive.
- Implement password policies enforcing complexity beyond simple masks (e.g., minimum length >8, mixed case, no predictable patterns).
- Use account lockout mechanisms after failed login attempts to thwart brute-force usage of generated wordlists.
- Log and alert on offline cracking tool executions in environments where such tools are not authorized.

## Objectives

1. Generate a complete wordlist covering a defined keyspace using Hashcat masks.
2. Ensure the wordlist is formatted for direct use in password cracking tools.
3. Verify the output covers all expected combinations without duplicates or errors.

## Instructions

### Step 1: Review Mask Character Definitions

**Context**: Before defining your mask, understand Hashcat's built-in character sets to ensure your pattern matches the target password structure. This step references a standard mask symbol table to select appropriate placeholders like ?d for digits or ?s for specials.

**Code** ([[codes/Hashcat-Mask-Character-Definitions]]):

Refer to the mask definitions for symbols such as ?l (lowercase), ?u (uppercase), ?d (digits), ?s (specials), ?a (alphanumeric + specials), and ?b (full byte range).

> This table provides the foundation for constructing masks. For example, ?d selects from 0-9, while ?b covers 0x00-0xff for any byte.

### Step 2: Define the Target Mask Pattern

**Context**: Based on reconnaissance or known patterns, construct your mask. For this example, use ?d?s?b?a to generate passwords starting with a digit, followed by a special character, any byte, and then any alphanumeric/special character. This targets short, mixed-character passwords common in some systems.

> Masks are built by prefixing each position with a ? followed by the character set (e.g., ?d for the first position). The total combinations for this mask: 10 (digits) * 32 (specials) * 256 (bytes) * 95 (alphanumeric/special) = approximately 7.7 million entries.

### Step 3: Execute Wordlist Generation

**Context**: Run Hashcat in brute-force mode (-a 3) with --stdout to generate and redirect output to a file. This step produces the actual wordlist without cracking any hashes.

**Command** ([[commands/hashcat-generate-wordlist-mask]]):

```bash
hashcat -a 3 --stdout $_MASK > $_OUTPUT_FILE
```

> Substitute $_MASK with your pattern (e.g., ?d?s?b?a) and $_OUTPUT_FILE with the desired filename (e.g., mask_wordlist.txt). Run this on a system with adequate resources, as large masks can generate gigabytes of data. Monitor progress with Hashcat's built-in counters.
