---
id: a2766e48-3477-4a2a-9807-a89e3ccc67c1
name: Brute-Force-Users-without-Kerberos-Preauth
type: procedure
verified: true
submitted: false
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
  - as-rep-roasting
commands:
  - '[[commands/getnpusers-brute-force-as-rep-users]]'
platforms:
  - Linux
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Brute-Force-Users-without-Kerberos-Preauth

## Summary

Brute force a list of usernames against the domain to identify those with 'Do not require Kerberos preauthentication' (UF_DONT_REQUIRE_PREAUTH) set, requesting AS-REP TGTs for offline cracking.

## Description

Users with this flag allow AS-REP roasting: the KDC responds with an encrytable TGT without password validation if the username is valid. This procedure uses Impacket to request and collect these hashes for cracking, common in AD pentests.

## Requirements

- Domain name and DC IP
- Username wordlist (e.g., from LinkedIn or prior enum)
- Impacket installed
- No password needed

## Defense

- Audit and disable UF_DONT_REQUIRE_PREAUTH on user accounts
- Monitor Kerberos AS-REQ/AS-REP events (Event ID 4768/4769)
- Implement account lockout on failed AS-REQs

## Objectives

1. Identify valid users vulnerable to roasting
2. Collect AS-REP hashes
3. Prepare for offline cracking

## Instructions

### Step 1: Prepare Username List

**Context**: Create or obtain a targeted wordlist of potential usernames.

Use tools like theHarvester or from LDAP enum to build users.txt.

### Step 2: Request AS-REP Tickets

**Context**: Brute force usernames to solicit TGT responses from KDC.

**Command** ([[commands/getnpusers-brute-force-as-rep-users]]):
```bash
GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS.txt -dc-ip $_TARGET_IP -request -format hashcat
```

> This requests TGTs for each username; valid ones return encrytable AS-REP blobs. Output to file for Hashcat. If no hits, refine wordlist.

**Expected Output**: Sample: username$krb5asrep$23$username@DOMAIN:challenge...

### Step 3: Verify Hits

**Context**: Check for successful roasts (non-empty hash file).

Count lines in output; each is a crackable hash.
