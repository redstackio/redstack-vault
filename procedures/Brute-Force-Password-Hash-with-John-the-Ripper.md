---
type: procedure
verified: true
submitted: true
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - '[[tags/Cryptography]]'
  - password-cracking
  - offline-attack
commands:
  - '[[commands/john-brute-force-hash-with-wordlist]]'
  - '[[commands/john-show-cracked-passwords]]'
platforms:
  - Linux
  - Unix
tools:
  - '[[tools/john-the-ripper]]'
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
---

# Brute-Force-Password-Hash-with-John-the-Ripper

## Summary

This procedure uses John the Ripper, a popular password cracking tool, to perform a dictionary-based brute force attack on a password hash file. It is particularly useful for offline cracking of hashes obtained from compromised systems, such as those extracted from /etc/shadow, SAM files, or network captures. John automatically detects the hash type if not specified, making it versatile for various formats like MD5, SHA-512, or DES.

## Description

In offensive security operations, brute forcing password hashes is a key technique in the credential access phase, allowing attackers to recover plaintext passwords from stolen hashes. This procedure focuses on dictionary attacks using a wordlist, which is efficient for common or weak passwords. It assumes the attacker has already obtained a hash file through prior discovery or exfiltration. The process involves loading the hash, running the crack with a wordlist, and then displaying results. This is typically performed on a Kali Linux or similar environment with sufficient computational resources for faster cracking. Success depends on the hash strength and wordlist quality; for stronger hashes, GPU acceleration or rules-based mutations can be added in advanced variations.

## Requirements

1. John the Ripper installed on a Linux system (see [[tools/john-the-ripper]] for installation).
2. A password hash file in a supported format (e.g., extracted from /etc/shadow or a .potfile).
3. A wordlist file containing potential passwords (e.g., rockyou.txt).
4. Sufficient CPU/GPU resources; for large wordlists, at least 4GB RAM recommended.
5. Basic command-line knowledge; no network access required as this is offline.

## Defense

Defensive measures include enforcing strong password policies (e.g., minimum length 12, complexity requirements), using salted hashes with high iteration counts (e.g., bcrypt, Argon2), and implementing account lockouts for online attempts. For offline attacks, monitor for unauthorized access to credential stores and use full-disk encryption. Detection can involve logging hash extraction attempts and endpoint detection rules for tools like John the Ripper in memory or process lists.

## Objectives

1. Load and identify the type of password hash from the input file.
2. Perform a dictionary-based brute force attack to crack the hash using a wordlist.
3. Retrieve and verify the plaintext password if successfully cracked.
4. Provide indicators of success or failure for further analysis.

## Instructions

### Step 1: Prepare the Hash File

**Context**: Ensure the hash file is in the correct format and accessible. If the hash is from a system file like /etc/shadow, extract it first using tools like unshadow. This step verifies the file integrity and places it in the working directory.

Copy or create the hash file:

```bash
cp /path/to/extracted/hash.txt .
```

> Check the file contents to confirm it contains valid hashes (e.g., $6$ for SHA-512crypt).

### Step 2: Run the Brute Force Attack

**Context**: Initiate the cracking process with John the Ripper using a wordlist. John will auto-detect the hash type and begin testing passwords from the list. This step may take time depending on the wordlist size and hardware; monitor progress with status keys.

**Command** ([[commands/john-brute-force-hash-with-wordlist]]):

```bash
john --wordlist=$_WORDLIST $_HASH_FILE
```

> This command loads the hash, guesses the type if unspecified, and runs the attack. Press any key (except 'q' or Ctrl-C) for status updates. If a password is found, it will be displayed; otherwise, it exhausts the wordlist.

### Step 3: Display Cracked Passwords

**Context**: After the attack completes, use the --show option to reliably display all cracked passwords. This verifies success and outputs the plaintext for use in further attacks, such as lateral movement.

**Command** ([[commands/john-show-cracked-passwords]]):

```bash
john $_HASH_FILE --show
```

> This retrieves results from John's session file (.pot). If cracked, it shows username:password; if not, indicates no cracks.
