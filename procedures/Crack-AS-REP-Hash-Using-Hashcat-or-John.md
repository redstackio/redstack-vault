---
id: 36b81492-9cb7-4f3a-8ba3-30640f70706a
name: Crack-AS-REP-Hash-Using-Hashcat-or-John
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T00:17:16.545805+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Password Spraying]]'
sub_techniques: []
tags:
  - asrep
  - hashcat
  - john
  - password-cracking
commands:
  - '[[commands/hashcat-crack-asrep-hash]]'
  - '[[commands/john-crack-asrep-hash]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Hashcat]]'
  - '[[tools/John-the-Ripper]]'
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
---

# Crack-AS-REP-Hash-Using-Hashcat-or-John

## Summary

This procedure cracks AS-REP hashes obtained from Kerberos roasting attacks using offline tools like Hashcat or John the Ripper. It uses dictionary attacks or rules to recover plaintext passwords from the encrypted tickets, providing valid credentials for domain access.

## Description

AS-REP hashes are RC4-encrypted Kerberos tickets that can be cracked offline since the encryption key is derived from the user's NTLM hash (password). Hashcat mode 18200 or John's krb5asrep format handles these. Success depends on password complexity and wordlist quality; it's a key step in credential access after roasting.

## Requirements

1. AS-REP hash file from roasting tool
2. Strong wordlist (e.g., rockyou.txt) or ruleset
3. GPU for Hashcat (optional but recommended) or CPU for John
4. Hashcat or John installed

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies (length, complexity, no dictionary words)
- Monitor for offline cracking attempts (though hard to detect directly)
- Use LAPS for local admin passwords; rotate service accounts
- Enable auditing of Kerberos failures to prevent initial hash acquisition

## Objectives

1. Recover plaintext password from AS-REP hash
2. Validate credentials for use in authentication
3. Enable further domain compromise

## Instructions

### Step 1: Prepare Hash and Wordlist Files

**Context**: Ensure the hash file contains valid AS-REP format and wordlist is ready.

Example hash file (hashes.txt): `$krb5asrep$23$username@DOMAIN:encrypted_hash`.

### Step 2: Crack with Hashcat

**Context**: Use Hashcat for faster GPU-based cracking with dictionary attack.

**Command** ([[commands/hashcat-crack-asrep-hash]]):

```bash
hashcat -m 18200 -a 0 $_HASH_FILE.txt $_WORDLIST.txt --force
```

> Outputs progress and cracked hashes. Use `hashcat --show $_HASH_FILE.txt` to view results, e.g., `username:password123`.

### Step 3: Alternative Crack with John (If Hashcat Unavailable)

**Context**: Fall back to John for CPU-based cracking if needed.

**Command** ([[commands/john-crack-asrep-hash]]):

```bash
john --wordlist=$_WORDLIST.txt --format=krb5asrep $_HASH_FILE.txt
```

> Run `john --show --format=krb5asrep $_HASH_FILE.txt` to display cracked passwords.

### Step 4: Verify Cracked Credentials

**Context**: Test the password against the domain to confirm.

Use `kinit username@DOMAIN` or similar to authenticate.
