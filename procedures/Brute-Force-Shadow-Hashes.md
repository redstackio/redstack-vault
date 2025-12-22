---
id: 49d3830a-114e-44cd-8ff0-38a1677a50c7
name: Brute-Force-Shadow-Hashes
type: procedure
verified: true
submitted: true
created_at: '2020-01-20T20:42:02.745293+00:00'
updated_at: '2023-05-26T00:41:03.700936+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
platforms:
  - Linux
tags:
  - '[[tags/Cryptography]]'
  - '[[tags/data exposure]]'
commands:
  - '[[commands/hashcat-find-hash-mode-from-example-hashes]]'
  - '[[commands/hashcat-brute-force-password-hashes]]'
tools: []
validated: true
---

# Brute-Force-Shadow-Hashes

## Summary

This procedure demonstrates how to brute force password hashes extracted from the Linux /etc/shadow file using Hashcat. It covers identifying the hash algorithm type from the shadow file format and then cracking the hashes offline with a wordlist, assuming the attacker has obtained read access to the shadow file.

## Description

On Linux systems, user passwords are stored in hashed form in the /etc/shadow file, which is readable only by root or users with specific permissions. Once an attacker gains access to this file (e.g., via privilege escalation or misconfiguration), they can extract the hashes and attempt to crack them using brute force or dictionary attacks. Hashcat is used here because it supports various hash types used in Unix-like systems and can leverage GPU acceleration for faster cracking. This technique is effective against weak passwords but less so against strong, salted hashes like SHA-512. The procedure assumes a controlled environment like a red team engagement or lab setup.

## Requirements

1. Read access to /etc/shadow (typically requires root privileges or sudo).
2. Hashcat installed on a system with GPU support for optimal performance (CPU fallback possible but slower).
3. A wordlist file for dictionary attacks (e.g., rockyou.txt).
4. Extracted hashes in a clean text file, one per line without usernames or salts if not needed.

## Defense

- Enforce strong password policies with length, complexity, and rotation requirements to resist brute force.
- Use account lockout mechanisms after failed login attempts to prevent online brute force (though this is offline cracking).
- Monitor for unauthorized access to /etc/shadow via file integrity monitoring tools like AIDE or auditd.
- Enable full disk encryption and restrict shadow file permissions strictly to root.
- Detect offline cracking attempts by monitoring for tools like Hashcat on endpoints via EDR solutions.

## Objectives

1. Identify the hashing algorithm used in the shadow file to select the correct Hashcat mode.
2. Prepare a clean file of target hashes for cracking.
3. Successfully crack one or more passwords using a wordlist.
4. Verify cracked passwords against the original hashes.

## Instructions

### Step 1: Extract and Identify Hash Types from /etc/Shadow

**Context**: Begin by accessing /etc/shadow and noting the hash format. Each hash starts with identifiers like $1$ for MD5 or $6$ for SHA-512, which determine the Hashcat mode. Use the reference list of common Linux hash types to understand the format.

Reference the common Linux shadow hash type identifiers using [[codes/linux-shadow-hash-type-identifiers]]:

For example, a typical SHA-512 hash from /etc/shadow might look like:

$6$ngUYdXkcMLK$AI23a7brd9zZOgf336W.9a7/M2QstTHC/9Es0t17P/sAkBgxxrPituenv35hG.z/J28T1vfEx2I8nR6ac44AX0

This indicates SHA-512 ($6$). To confirm the exact Hashcat mode, search Hashcat's built-in example hashes.

**Command** ([[commands/hashcat-find-hash-mode-from-example-hashes]]):
```bash
hashcat --example-hashes | grep -C 2 $_VALUE
```

> Replace $_VALUE with the hash identifier pattern, e.g., '\$6\$'. This command outputs the mode number (e.g., 1800 for SHA-512) and a sample hash for verification. If no match, consult Hashcat documentation.

### Step 2: Prepare the Hashes File

**Context**: Create a text file containing only the hashes to crack, stripping usernames and any extraneous data from /etc/shadow. This ensures Hashcat processes only the hash portions. For instance, from a line like 'user:$6$hash:salt:...' extract just '$6$hash$salt:...'. Save as hashes.txt.

Use a text editor or command like:
```bash
sudo grep '^[^:]*:[^:]*\$' /etc/shadow | cut -d: -f2 > hashes.txt
```

> This extracts the second field (hash) from non-empty password lines. Verify the file contains clean hashes, one per line.

### Step 3: Brute Force the Hashes with Hashcat

**Context**: Run Hashcat with the identified mode, input hashes file, and a wordlist. For best performance, use a machine with NVIDIA/AMD GPU; otherwise, add --force for VM CPU usage. Monitor progress with session resumption if needed.

**Command** ([[commands/hashcat-brute-force-password-hashes]]):
```bash
hashcat -m $_MODE $_HASHES_FILE $_WORDLIST
```

> Replace $_MODE with the mode from Step 1 (e.g., 1800), $_HASHES_FILE with 'hashes.txt', and $_WORDLIST with your dictionary (e.g., '/usr/share/wordlists/rockyou.txt'). Hashcat will attempt to crack and display recovered passwords. Use -a 0 for straight dictionary attack or -a 3 for brute force with mask.

If successful, Hashcat outputs cracked passwords; verify by re-hashing and comparing.
