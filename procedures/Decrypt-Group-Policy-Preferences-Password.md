---
id: b84cf1aa-9379-4fdf-8b0b-1da6ce4658ad
name: Decrypt-Group-Policy-Preferences-Password
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T18:34:03.961833+00:00'
updated_at: '2023-05-25T19:53:01.794693+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - cryptography
  - data-encryption
  - known-vulnerability
commands:
  - '[[commands/gpp-decrypt-extract-password-from-encrypted-string]]'
tools:
  - '[[tools/gpp-decrypt]]'
validated: true
---

# Decrypt-Group-Policy-Preferences-Password

## Summary

This procedure decrypts AES-encrypted passwords from Group Policy Preferences XML files using the publicly known Microsoft key.

## Description

GPP files in SYSVOL store admin settings with embedded credentials. Though encrypted, the AES-256 key was leaked by Microsoft (MS14-025), allowing trivial decryption. This yields domain admin or service account passwords.

## Requirements

- Downloaded GPP XML file (e.g., Groups.xml)
- Extracted cpassword attribute
- gpp-decrypt tool

## Defense

- Avoid storing passwords in GPP (use LAPS or secure alternatives)
- Patch MS14-025 and remove old GPP files
- Monitor SYSVOL access

## Objectives

1. Extract encrypted password from XML
2. Decrypt to plaintext
3. Use for further access

## Instructions

### Step 1: Extract Encrypted String

**Context**: Parse XML for cpassword in <Properties> tags.

Use grep or editor: grep -o 'cpassword=.*' Groups.xml.

> Obtain string like CiDUq6tbrBL1m/js9DmZNIydXpsE69WB9JrhwYRW9xywOz1/0W5VCUz8tBPXUkk9y80n4vw74KeUWc2+BeOVDQ.

### Step 2: Decrypt the Password

**Context**: Apply known key to reveal plaintext.

**Command** ([[commands/gpp-decrypt-extract-password-from-encrypted-string]]):
```bash
gpp-decrypt $_ENCRYPTED_STRING
```

> Outputs plaintext; ignore OpenSSL deprecation warning.
