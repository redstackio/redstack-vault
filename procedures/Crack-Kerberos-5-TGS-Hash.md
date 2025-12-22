---
id: f72c836e-7e5e-4364-ac5d-f41d75e0995e
name: Crack-Kerberos-5-TGS-Hash
type: procedure
verified: true
submitted: false
created_at: '2023-01-11T21:03:47.343868+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[cme-smb-enable-rdp]]'
sub_techniques: []
tags:
  - hashcat
  - john
  - kerberos
  - password-cracking
commands:
  - '[[commands/hashcat-crack-krb5tgs]]'
  - '[[commands/john-crack-krb5tgs]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Hashcat]]'
  - '[[tools/John-the-Ripper]]'
validated: true
---

# Crack-Kerberos-5-TGS-Hash

## Summary

This procedure outlines how to crack Kerberos 5 Ticket Granting Service (TGS) hashes obtained from Kerberoasting attacks using tools like Impacket or Rubeus against a Domain Controller. It uses dictionary attacks with Hashcat or John the Ripper to recover plaintext passwords from the hashes, enabling further credential access for lateral movement or privilege escalation in Active Directory environments.

## Description

Kerberoasting involves requesting service tickets for accounts with Service Principal Names (SPNs) and extracting the encrypted TGS tickets, which can be cracked offline due to weaker encryption compared to AS-REP tickets. This procedure assumes you have already obtained the TGS hash in a compatible format (e.g., $krb5tgs$23$*user$realm$service*...). The cracking process uses a wordlist for brute-force or dictionary attacks. Success depends on password complexity and wordlist quality. This is typically performed in a post-exploitation phase after initial domain access.

## Requirements

1. A TGS hash file (e.g., hash.txt) extracted from tools like Impacket's GetUserSPNs.py or Rubeus.
2. A comprehensive password wordlist (e.g., rockyou.txt or custom domain-specific list).
3. Installed cracking tools: Hashcat or John the Ripper.
4. Sufficient computational resources (GPU recommended for Hashcat) for efficient cracking.
5. Domain knowledge of target service accounts to prioritize cracking.

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies for service accounts, including length >25 characters and avoidance of dictionary words.
- Monitor for anomalous Kerberos ticket requests (Event ID 4769) with high volume from single users.
- Use tools like Microsoft ATA or ETW logging to detect Kerberoasting attempts.
- Rotate service account passwords regularly and use managed service accounts (gMSAs).
- Offline cracking is hard to detect directly, but monitor for unusual outbound data exfiltration of hashes.

## Objectives

1. Load and process the TGS hash into a cracking tool.
2. Perform a dictionary attack to recover the plaintext password.
3. Verify the cracked credentials for use in further attacks.
4. Expected outcome: Obtain valid service account password for domain access.

## Instructions

### Step 1: Prepare the Hash and Wordlist

**Context**: Ensure the TGS hash is in the correct format and your wordlist is ready. The hash should be in Hashcat mode 13100 or John krb5tgs format, typically starting with $krb5tgs$.

Place the hash in a file named hash.txt and the wordlist as password-list.txt in the working directory.

### Step 2: Crack Using Hashcat

**Context**: Hashcat is GPU-accelerated and efficient for large wordlists. This step uses mode 13100 for Kerberos 5 TGS-REP etype 23 (RC4-HMAC).

**Command** ([[commands/hashcat-crack-krb5tgs]]):
```bash
hashcat -m 13100 -a 0 hash.txt password-list.txt
```

> This command loads the hash, attacks it with the wordlist in straight dictionary mode (-a 0). Monitor progress with the built-in status display. If cracked, Hashcat will show the password in the output.

### Step 3: Crack Using John the Ripper

**Context**: John is a CPU-based alternative, useful if no GPU is available. It supports the krb5tgs format natively.

**Command** ([[commands/john-crack-krb5tgs]]):
```bash
john hash.txt --format=krb5tgs --wordlist=password-list.txt
```

> This loads the hash in krb5tgs format and runs a wordlist attack. Use 'john --show hash.txt' afterward to view cracked passwords.

### Step 4: Verify Cracked Credentials

**Context**: Test the recovered password to ensure it works for the service account.

Use tools like Impacket's psexec.py or PowerView to authenticate with the cracked credentials against the domain.
