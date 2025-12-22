---
type: procedure
description: >-
  A step-by-step guide to cracking password hashes using John the Ripper,
  focusing on dictionary and rule-based attacks for credential recovery.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - '[[tags/Hash Cracking]]'
  - '[[tags/John]]'
  - '[[tags/John Usage]]'
commands:
  - '[[commands/john-crack-password-file]]'
  - '[[commands/john-crack-with-specific-wordlist]]'
  - '[[commands/john-crack-with-wordlist-and-rules]]'
  - '[[commands/john-show-cracked-passwords]]'
  - '[[commands/john-restore-interrupted-session]]'
platforms:
  - Linux
tools:
  - '[[tools/John-the-Ripper]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Crack-Password-Hashes-with-John-the-Ripper

## Summary

This procedure outlines how to use John the Ripper to crack password hashes extracted from systems or files, employing dictionary attacks, brute force, and rule modifications to recover plaintext passwords. It is typically used in red team engagements to demonstrate weak password policies or in defensive assessments to identify vulnerable credentials.

## Description

John the Ripper is a fast password cracker that supports numerous hash formats, including those from Unix/Linux (/etc/shadow), Windows (NTLM), and databases. In an attack scenario, hashes are obtained via techniques like dumping SAM files or querying LDAP, then cracked offline to obtain credentials for lateral movement or privilege escalation. This procedure assumes hashes are already in a compatible format (e.g., in a file like 'passwd' or 'hashes.txt'). It covers basic cracking, wordlist usage, rule application for mutations, viewing results, and session restoration. Success depends on hash strength, wordlist quality, and computational resources; GPU acceleration can significantly speed up the process. Target environments include Linux systems where John is commonly run from Kali or similar distributions.

## Requirements

1. John the Ripper installed on a Linux machine with sufficient CPU/GPU resources.
2. A file containing password hashes in a supported format (e.g., Unix crypt, NTLM).
3. Optional: Custom wordlists (e.g., rockyou.txt) and rule sets (e.g., Jumbo ruleset).
4. Access to the tool's configuration files for format-specific tweaks if needed.

## Defense

- Enforce strong password policies with complexity requirements and regular rotations.
- Use salted hashes and algorithms resistant to brute force (e.g., bcrypt, Argon2).
- Implement account lockouts after failed login attempts and monitor for offline hash cracking attempts via endpoint detection.
- Limit hash exposure by securing credential stores and using just-in-time access.

## Objectives

1. Recover plaintext passwords from captured hashes to enable further access.
2. Assess password strength in a target environment to recommend improvements.
3. Demonstrate the feasibility of credential attacks in a controlled red team exercise.

## Instructions

### Step 1: Prepare the Hash File

**Context**: Ensure the input file contains valid hashes in a format John recognizes, such as /etc/passwd or /etc/shadow style. This step verifies compatibility and avoids errors during cracking.

Extract or format hashes into a file named 'hashes.txt'. Use tools like unshadow if combining passwd and shadow files.

> No specific command here; manually prepare the file.

**Expected Output**: A text file with lines like 'username:$6$rounds=5000$salt$hash' for SHA-512 crypt.

### Step 2: Perform Basic Cracking on the Hash File

**Context**: Start with John's default incremental or single mode to attempt cracking without external wordlists, useful for simple or default passwords.

**Command** ([[commands/john-crack-password-file]]):
```bash
john hashes.txt
```

> This initiates cracking using built-in modes. Monitor progress via on-screen statistics. Interrupt with Ctrl+C to save the session.

**Expected Output**: Real-time stats like 'Loaded 1 password hash' and guesses per second; cracked passwords appear in the output.

### Step 3: Crack Using a Specific Wordlist

**Context**: If basic mode fails, use a dictionary attack with a targeted wordlist to test common passwords, improving efficiency over brute force.

**Command** ([[commands/john-crack-with-specific-wordlist]]):
```bash
john --wordlist=rockyou.txt hashes.txt
```

> Replace 'rockyou.txt' with your wordlist path. This mode tries each word directly against the hashes.

**Expected Output**: Progress showing wordlist position and any cracks, e.g., 'password123 (user1)'

### Step 4: Apply Rules to the Wordlist for Mutations

**Context**: Enhance the wordlist by applying transformation rules (e.g., appending numbers, changing case) to cover variations without exhaustive brute force.

**Command** ([[commands/john-crack-with-wordlist-and-rules]]):
```bash
john --wordlist=rockyou.txt --rules=Jumbo hashes.txt
```

> The Jumbo ruleset includes advanced mutations. If no rules specified, defaults to built-in.

**Expected Output**: Extended cracking session with mutated attempts; more cracks if passwords are leetspeak or patterned.

### Step 5: View Cracked Passwords

**Context**: After cracking (or interruption), retrieve recovered passwords without re-running the full session.

**Command** ([[commands/john-show-cracked-passwords]]):
```bash
john --show hashes.txt
```

> This displays only cracked entries; uncracked hashes show as '?'.

**Expected Output**: Lines like 'user1:password123 (hash1)' for each success.

### Step 6: Restore an Interrupted Session

**Context**: John saves sessions automatically; restore to continue long-running cracks without restarting from scratch.

**Command** ([[commands/john-restore-interrupted-session]]):
```bash
john --restore
```

> Use this if the session was paused or crashed. It loads the last checkpoint.

**Expected Output**: Resumes from last position, showing updated stats.
