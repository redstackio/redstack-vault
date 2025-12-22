---
id: 19e10971-3635-49e6-9489-ab65339983cc
name: Brute-Force-Password-Protected-XLSX-File
type: procedure
verified: true
submitted: true
created_at: '2020-06-25T21:07:47.268848+00:00'
updated_at: '2023-05-25T19:47:25.482851+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - brute-force
commands:
  - '[[commands/office2john-extract-hash-from-xlsx]]'
  - '[[commands/john-brute-force-hash-file]]'
platforms:
  - Linux
tools:
  - '[[tools/john-the-ripper]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Brute-Force-Password-Protected-XLSX-File

## Summary

This procedure extracts the password hash from a password-protected XLSX file using the office2john.py script from John the Ripper and then performs a brute-force attack on the hash using a wordlist to recover the plaintext password. It is useful in red team engagements or forensic analysis where access to protected Office documents is needed without the original credentials.

## Description

Password-protected XLSX files use encryption to secure their contents, typically with a hash derived from the password. This procedure leverages John the Ripper's specialized scripts to first convert the XLSX file into a crackable hash format compatible with common hashing algorithms like those used in Office 2013 and later. Once the hash is extracted, John the Ripper applies dictionary-based brute forcing with a wordlist to attempt password recovery. This technique is effective against weak passwords and is commonly used in scenarios involving data exfiltration or privilege escalation where protected files contain sensitive information such as credentials or intellectual property. The process assumes the attacker has obtained the XLSX file through prior access, such as phishing or network shares.

## Requirements

1. Linux environment (e.g., Kali Linux) with John the Ripper installed.
2. Access to the target password-protected XLSX file.
3. A wordlist file containing potential passwords (e.g., rockyou.txt).
4. Sufficient computational resources for cracking, as complex hashes may take time.

## Defense

Defensive measures and detection strategies:

- Use strong, complex passwords for Office documents to resist brute-force attacks.
- Enable full-disk encryption and access controls to prevent unauthorized file acquisition.
- Monitor for anomalous file access or extraction tools via endpoint detection and response (EDR) systems.
- Implement file integrity monitoring to detect tampering with protected documents.

## Objectives

1. Extract the password hash from the XLSX file in a format suitable for cracking.
2. Perform dictionary-based brute forcing to recover the plaintext password.
3. Verify the cracked password by opening the XLSX file.

## Instructions

### Step 1: Extract Hash from XLSX File

**Context**: Use the office2john.py script to analyze the XLSX file and output its password hash in John the Ripper's proprietary format. This step decrypts the file's metadata without needing the password, allowing subsequent cracking.

**Command** ([[commands/office2john-extract-hash-from-xlsx]]):
```bash
office2john.py $_TARGET_FILE.xlsx
```

> This command processes the XLSX file and prints the hash to stdout, which should be redirected to a file for the next step. The script handles Office 2013+ formats with AES-256 encryption. Expected output is a single line starting with the filename followed by the hash in $office$* format.

### Step 2: Brute Force the Extracted Hash

**Context**: Load the extracted hash into John the Ripper and run a wordlist-based attack to guess the password. This step iterates through the wordlist, testing each entry against the hash until a match is found or exhausted.

**Command** ([[commands/john-brute-force-hash-file]]):
```bash
john --wordlist=$_WORDLIST $_HASH_FILE
```

> After running the cracking session, use `john $_HASH_FILE --show` to display the cracked password. The tool will report progress and stop upon finding a match. If successful, the password will be displayed; otherwise, it may indicate no match in the wordlist.
