---
id: 0a10cdd1-1117-4bec-ab86-a3ed64cd7ec6
name: ASREPRoast-Users-Without-Preauthentication-Using-Username
type: procedure
verified: true
submitted: false
created_at: '2023-01-11T20:48:08.611174+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[rubeus-asrep-roast-user]]'
sub_techniques: []
tags:
  - asrep-roasting
  - kerberos
commands:
  - '[[commands/rubeus-asreproast-hashcat-format]]'
platforms:
  - Windows
tools:
  - '[[tools/Rubeus]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
---

# ASREPRoast-Users-Without-Preauthentication-Using-Username

## Summary

This procedure performs AS-REP roasting on Active Directory users without Kerberos preauthentication enabled, using only a valid username to request crackable AS-REP hashes from the domain controller. It targets misconfigured accounts to obtain encrypted tickets for offline password cracking, requiring no initial domain credentials.

## Description

AS-REP roasting exploits the Kerberos protocol by sending an AS-REQ to the KDC for users with preauth disabled, receiving an AS-REP with an encrypted TGT using the user's password hash as the key. These hashes (RC4-HMAC) can be cracked offline. This is effective in reconnaissance or when usernames are known from prior enumeration, allowing credential acquisition without passwords.

## Requirements

1. Valid username of a target user with preauth disabled
2. Network access to domain controller (port 88)
3. Rubeus tool on a Windows machine
4. Domain name and DC IP

## Defense

Defensive measures and detection strategies:

- Enforce Kerberos preauthentication on all accounts
- Audit user account flags in AD (dsquery or PowerShell Get-ADUser)
- Monitor for anomalous AS-REQ volume (Windows Event ID 4768)
- Use Kerberos armoring (FAST) for enhanced protection

## Objectives

1. Request AS-REP ticket for targeted user
2. Extract crackable hash
3. Prepare for offline password recovery

## Instructions

### Step 1: Identify Target User

**Context**: Select a username from prior brute force or enumeration that likely has preauth disabled.

No command; confirm via AD tools if possible, but proceed assuming known.

### Step 2: Perform AS-REP Roasting with Rubeus

**Context**: Use Rubeus to send the AS-REQ and capture the AS-REP hash in hashcat-compatible format for cracking.

**Command** ([[commands/rubeus-asreproast-hashcat-format]]):

```bash
Rubeus.exe asreproast /user:$_USERNAME /domain:$_DOMAIN /dc:$_TARGET_IP /format:hashcat /outfile:asrep_hashes.txt
```

> This requests the ticket and outputs the hash directly. Expected output: `$krb5asrep$23$username@DOMAIN:encrypted_hash` saved to file.

### Step 3: Verify Hash Retrieval

**Context**: Check the output file for the hash; success means the user responded without preauth.

Inspect asrep_hashes.txt; if empty, the user requires preauth or is invalid.
