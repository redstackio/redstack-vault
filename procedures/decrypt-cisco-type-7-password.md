---
id: b3ab27e6-8a3a-49ee-88c1-5e59a58a5945
name: decrypt-cisco-type-7-password
type: procedure
verified: true
submitted: false
created_at: '2019-12-18T20:24:02.242469+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - cryptography
  - credential-access
commands:
  - '[[commands/python-ciscot7-decrypt-cisco-type-7-password]]'
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# decrypt-cisco-type-7-password

## Summary

This procedure decrypts Cisco IOS Type 7 passwords, which use a weak, publicly known algorithm. These may appear in memory dumps or configs from Windows systems integrated with Cisco devices, providing cleartext credentials for further use.

## Description

Type 7 encryption is a reversible obfuscation in Cisco configs, using a fixed key. It's trivial to decrypt offline, making it valuable if found in cross-platform environments like AD with Cisco VPNs. This step follows memory extraction where such strings are harvested.

## Requirements

1. Encrypted Type 7 string (e.g., from strings output)
2. Python and ciscot7.py script downloaded from GitHub
3. No target access needed; offline operation

## Defense

- Avoid storing Type 7 passwords; use Type 5 (MD5) or stronger
- Monitor for script execution like ciscot7.py in logs
- Encrypt configs with stronger methods in integrated systems

## Objectives

1. Recover plaintext from Type 7 string
2. Validate credential for SMB/WinRM reuse
3. Identify if it grants elevated access

## Instructions

### Step 1: Prepare the Script

**Context**: Download and set up the decryption tool to process the encrypted password.

No command; clone repo: git clone https://github.com/theevilbit/ciscot7.

> Ensure Python 3 is available; test with sample.

### Step 2: Decrypt the Password

**Context**: Feed the Type 7 hash (after '7 ') to the script for reversal.

**Command** ([[commands/python-ciscot7-decrypt-cisco-type-7-password]]):
```bash
python ciscot7.py -d -p $_ENCRYPTED_PASSWORD
```

> For example, input 02375012182C1A1D751618034F36415408 yields the plaintext. If invalid, check format (hex string post '7 ').

### Step 3: Verify and Use

**Context**: Test the decrypted password against target services.

Use in SMB brute-force if applicable.

> Success if login succeeds; else, discard.
