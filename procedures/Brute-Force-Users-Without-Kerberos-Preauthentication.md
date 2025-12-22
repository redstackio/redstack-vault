---
id: a2766e48-3477-4a2a-9807-a89e3ccc67c1
name: Brute-Force-Users-Without-Kerberos-Preauthentication
type: procedure
verified: true
submitted: false
created_at: '2020-03-17T21:43:18.756014+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques: []
tags:
  - active-directory
  - enumeration
  - kerberos
commands:
  - '[[commands/getnpusers-brute-force-users-without-preauth]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Brute-Force-Users-Without-Kerberos-Preauthentication

## Summary

This procedure identifies valid Active Directory users who have the 'Do not require Kerberos preauthentication' flag enabled by brute forcing a list of usernames. It requests AS-REP tickets without providing a password, allowing retrieval of TGTs and hashes for users where the username is correct, enabling further cracking or use in attacks.

## Description

In Kerberos authentication, users with the preauthentication flag disabled respond to AS-REQ requests with an AS-REP containing an encrypted TGT, even without a valid password. This procedure uses a username wordlist to probe for such users, confirming validity through successful responses. It's useful in initial access or reconnaissance phases when usernames are known but passwords are not, targeting misconfigured accounts in Active Directory environments.

## Requirements

1. Network access to the domain controller (UDP/TCP port 88)
2. Wordlist of potential usernames (e.g., from LDAP enumeration, OSINT, or common names)
3. Impacket suite installed (GetNPUsers.py)
4. Target domain name and DC IP address

## Defense

Defensive measures and detection strategies:

- Enable Kerberos preauthentication for all user accounts via Group Policy
- Monitor Kerberos AS-REQ/AS-REP traffic for unusual volume from single sources (Event ID 4768/4769 in Windows logs)
- Use account lockout policies on failed authentications
- Implement network segmentation to limit DC access

## Objectives

1. Enumerate and validate usernames with disabled preauth
2. Retrieve AS-REP hashes for offline cracking
3. Obtain initial credentials for domain access

## Instructions

### Step 1: Prepare Username Wordlist

**Context**: Create or obtain a list of potential usernames to brute force. This could be from prior enumeration like LDAP queries or social engineering.

Save usernames to a file, one per line (e.g., users.txt with entries like 'administrator', 'user1', etc.). No command needed here.

### Step 2: Brute Force and Request AS-REP Tickets

**Context**: Use GetNPUsers.py to send AS-REQ requests without passwords, targeting users without preauth. The tool will output hashes only for valid, flagged users.

**Command** ([[commands/getnpusers-brute-force-users-without-preauth]]):

```bash
GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS.txt -dc-ip $_TARGET_IP -format hashcat
```

> This command iterates through the username file, requests tickets, and outputs crackable hashes for successful hits. Expected output includes lines like `$krb5asrep$23$username@DOMAIN:encrypted_hash` for valid users.

### Step 3: Verify and Filter Results

**Context**: Review the output to identify valid users and save hashes for cracking. Invalid usernames will generate errors or no response.

Use grep or manual inspection to filter successful hashes: `grep 'krb5asrep' output.txt > valid_hashes.txt`.

> Success is indicated by the presence of AS-REP hashes without authentication failures.
