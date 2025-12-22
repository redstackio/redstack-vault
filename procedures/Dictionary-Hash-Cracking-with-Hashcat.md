---
type: procedure
description: >-
  Recover passwords from hashed values using a dictionary attack with Hashcat,
  applying rules to generate variations from a wordlist.
verified: true
submitted: false
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - '[[tags/Dictionary]]'
  - '[[tags/Hashcat]]'
  - '[[tags/Hash Cracking]]'
commands:
  - '[[commands/hashcat-dictionary-attack-with-rules]]'
platforms:
  - Linux
tools:
  - '[[tools/Hashcat]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
---

# Dictionary-Hash-Cracking-with-Hashcat

## Summary

This procedure uses Hashcat to perform a dictionary-based attack on password hashes, leveraging a wordlist of common passwords and optional rules to generate variations. It is effective for cracking weak or commonly used passwords obtained during credential dumping or post-exploitation, targeting various hash formats like NTLM, MD5, or SHA-1.

## Description

Dictionary cracking involves hashing each entry in a wordlist and comparing it against the target hash until a match is found. Hashcat accelerates this process using GPU or CPU parallelization and supports rule-based mutations (e.g., appending numbers or changing case) to expand the dictionary without exhaustive brute-forcing. This technique is commonly used in red team engagements after extracting hashes via tools like Mimikatz or from files like SAM dumps. It assumes the attacker has offline access to the hashes and a suitable wordlist (e.g., rockyou.txt). Success depends on password strength; it fails against complex, unique passwords. The procedure maps to MITRE ATT&CK T1110 (Brute Force) under Credential Access.

## Requirements

1. Offline access to a file containing the target hashes (e.g., from credential dumping).
2. A pre-built wordlist file (e.g., rockyou.txt) with potential password candidates.
3. Hashcat installed on a system with GPU support for optimal performance (CPU fallback available).
4. Optional: A rules file (e.g., built-in Hashcat rules like best64.rule) for wordlist mutations.
5. Knowledge of the hash type (e.g., MD5 is type 0, NTLM is type 1000).

## Defense

- Enforce strong password policies requiring length >12, complexity, and no dictionary words.
- Use salted hashes (e.g., bcrypt, Argon2) to prevent precomputed attacks.
- Implement account lockouts and monitor for unusual offline hash access attempts.
- Regularly rotate credentials and use password managers to avoid reuse.

## Objectives

1. Recover plaintext passwords from captured hashes to enable lateral movement or privilege escalation.
2. Assess the effectiveness of organizational password policies by identifying crackable credentials.
3. Gain initial access to accounts using recovered passwords in authenticated environments.
4. Validate the security of hashed credentials during penetration testing.

## Instructions

### Step 1: Identify Hash Type

**Context**: Determine the hash format to select the correct mode in Hashcat, as incorrect identification leads to failed cracking attempts. Use Hashcat's example hashes or manual inspection (e.g., length and characters).

**Command** ([[commands/hashcat-show-hash-info]]):

Consult Hashcat documentation or run a test, but no specific command here—manually verify against known formats.

> Expected: Confirm type (e.g., MD5: 32 hex chars; NTLM: 32 hex chars). If unknown, use `hashcat --example-hashes` to compare.

### Step 2: Prepare Input Files

**Context**: Ensure hashes are in a clean file (one hash per line or in Hash:Plain format) and wordlist is ready. Rules file enhances coverage by applying transformations like leet speak or appending years.

No command execution here—create files manually:
- Save hashes to `hashes.txt`.
- Download wordlist to `wordlist.txt` (e.g., via wget).
- Copy rules to `rules.rule` (e.g., from Hashcat's rules directory).

> Expected: Files ready in working directory. Verify with `wc -l hashes.txt` showing hash count.

### Step 3: Execute Dictionary Attack

**Context**: Run Hashcat in dictionary mode (attack-mode 0) with rules to crack the hashes. This step performs the core cracking, outputting recovered passwords to a potfile or specified file.

**Command** ([[commands/hashcat-dictionary-attack-with-rules]]):
```bash
hashcat -m $_HASH_TYPE -a 0 $_HASHES_FILE $_WORDLIST_FILE -r $_RULES_FILE -o cracked.txt
```

> This command loads the hash type (-m), uses dictionary attack (-a 0), applies rules (-r), and outputs cracked passwords to cracked.txt. Monitor progress with session stats. Expected: Cracking session starts, showing speed (e.g., 100k H/s) and status. Upon completion or match, check `cracked.txt` for plaintext: e.g., `hash:password`.
