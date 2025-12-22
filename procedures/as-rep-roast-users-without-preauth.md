---
id: a2766e48-3477-4a2a-9807-a89e3ccc67c1
name: as-rep-roast-users-without-preauth
type: procedure
verified: true
submitted: true
created_at: '2020-03-17T21:43:18.756014+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[rubeus-asrep-roast-user]]'
sub_techniques: []
tags:
  - active-directory
  - kerberos
  - enumeration
commands:
  - '[[commands/getnpusers-as-rep-roast]]'
tools:
  - '[[tools/impacket-getnpusers]]'
platforms:
  - Linux
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
---

# as-rep-roast-users-without-preauth

## Summary

Exploit users with the UF_DONT_REQUIRE_PREAUTH flag by requesting AS-REP TGTs without authentication, capturing crackable hashes for offline password recovery.

## Description

Kerberos AS-REP roasting targets accounts where pre-authentication is disabled, allowing attackers to obtain encrypted TGT portions using valid usernames, which can be cracked offline. This is effective against enumerated users from RPC.

## Requirements

- Username list (users.txt)
- Domain name and DC IP
- Impacket installed ([[tools/impacket-getnpusers]])

## Defense

- Enable preauth on all accounts (remove UF_DONT_REQUIRE_PREAUTH)
- Monitor Kerberos Event ID 4768 for RC4 requests
- Limit username enumeration

## Objectives

1. Identify valid users via AS-REP responses
2. Capture TGT hashes
3. Prepare for cracking

## Instructions

### Step 1: Prepare Username List

**Context**: Use enumerated users; ensure list is clean.

No command; create or use existing users.txt.

> If no preauth users, all requests fail; success on valid weak accounts.

### Step 2: Request AS-REP Hashes

**Context**: Run GetNPUsers to roast all users in list.

**Command** ([[commands/getnpusers-as-rep-roast]]):
```bash
GetNPUsers.py $_DOMAIN/ -usersfile users.txt -format hashcat -outputfile asrep_hashes.txt -dc-ip $_DC_IP
```

> Outputs hashes only for vulnerable users.

### Step 3: Verify Hashes

**Context**: Check file for captured hashes.

No command; `cat asrep_hashes.txt` to confirm format.

> Expected: $krb5asrep$ hashes.

## Expected Output

Hash file with entries like $krb5asrep$23$username@domain:hashvalue.
