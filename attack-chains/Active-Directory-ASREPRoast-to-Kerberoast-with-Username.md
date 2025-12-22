---
id: eb691bf4-46b3-4bf3-a22a-cb50e90a8be0
name: Active-Directory-ASREPRoast-to-Kerberoast-with-Username
type: attack_chain
description: >-
  Attack chain starting with brute forcing users without Kerberos
  preauthentication, performing AS-REP roasting to obtain crackable hashes,
  cracking the hashes for credentials, and then using those credentials to
  perform Kerberoasting for additional service account hashes.
verified: true
submitted: false
step_count: 4
created_at: '2023-01-11T20:54:04.613349+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
  - '[[procedures/Brute-Force-Users-Without-Kerberos-Preauthentication]]'
  - '[[procedures/ASREPRoast-Users-Without-Preauthentication-Using-Username]]'
  - '[[procedures/Crack-AS-REP-Hash-Using-Hashcat-or-John]]'
  - '[[procedures/Query-Domain-for-SPNS-and-Kerberoast-Authenticated]]'
commands:
  - '[[commands/getnpusers-brute-force-users-without-preauth]]'
  - '[[commands/rubeus-asreproast-hashcat-format]]'
  - '[[commands/hashcat-crack-asrep-hash]]'
  - '[[commands/john-crack-asrep-hash]]'
  - '[[commands/getuserspns-query-spns-and-request-tgs]]'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[rubeus-asrep-roast-user]]'
  - '[[cme-smb-enable-rdp]]'
  - '[[Password Spraying]]'
tags:
  - kerberos
  - asrep-roasting
  - kerberoasting
  - active-directory
  - credential-access
platforms:
  - Windows
  - Linux
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
---

# Active-Directory-ASREPRoast-to-Kerberoast-with-Username

Multi-stage attack chain demonstrating a complete workflow for credential access in Active Directory environments using AS-REP roasting and Kerberoasting, assuming the attacker has valid usernames but no initial credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~1-2 hours |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Brute Force Users] --> B[AS-REP Roasting]
    B --> C[Crack Hashes]
    C --> D[Kerberoasting]
    D --> E[Credential Access Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Impacket]]
- [[tools/Rubeus]]
- [[tools/Hashcat]]
- [[tools/John-the-Ripper]]

### Target Environment

- Active Directory domain controller accessible over the network
- Kerberos-enabled Windows environment
- Users with 'Do not require Kerberos preauthentication' flag set

### Initial Access Requirements

- List of potential usernames (e.g., from enumeration or OSINT)
- Network connectivity to domain controller (port 88 UDP/TCP for Kerberos)
- No initial domain credentials required, but valid usernames needed

## Detailed Attack Procedures

### Step 1: Brute Force Users Without Preauthentication
procedure: [[procedures/Brute-Force-Users-Without-Kerberos-Preauthentication]]

**Objective**: Identify valid usernames that have the 'Do not require Kerberos preauthentication' flag set, obtaining their TGTs for further use.

**Instructions**: Prepare a wordlist of usernames. Use the Impacket GetNPUsers tool to request AS-REP tickets for users without preauth, filtering for valid responses.

Execute [[commands/getnpusers-brute-force-users-without-preauth]]:

```bash
GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS.txt -dc-ip $_TARGET_IP -format hashcat
```

Save valid users and their hashes to a file for the next step.

**Expected Output**: List of valid users with AS-REP hashes in hashcat format, e.g., `$krb5asrep$23$username@DOMAIN:encrypted_hash`.

**Success Indicators**:
- Valid usernames identified with AS-REP responses
- No errors for invalid usernames; successful TGT retrieval for flagged users

### Step 2: ASREPRoast Users Without Preauthentication Using Username
procedure: [[procedures/ASREPRoast-Users-Without-Preauthentication-Using-Username]]

**Objective**: Request AS-REP tickets from the domain controller for targeted users without preauth to obtain crackable hashes.

**Instructions**: Target specific users identified in Step 1. Use Rubeus to perform AS-REP roasting and output hashes in a crackable format.

Execute [[commands/rubeus-asreproast-hashcat-format]] on a Windows machine with access to the DC:

```bash
Rubeus.exe asreproast /user:$_USERNAME /domain:$_DOMAIN /dc:$_TARGET_IP /format:hashcat
```

Collect the output hashes for cracking.

**Expected Output**: AS-REP hash in hashcat format, e.g., `$krb5asrep$23$username:encrypted_hash`.

**Success Indicators**:
- AS-REP ticket received without password prompt
- Hash exported successfully for offline cracking

### Step 3: Crack AS-REP Hash Using Hashcat or John
procedure: [[procedures/Crack-AS-REP-Hash-Using-Hashcat-or-John]]

**Objective**: Offline crack the obtained AS-REP hashes to recover plaintext passwords for valid credentials.

**Instructions**: Use a strong wordlist or ruleset. Prefer Hashcat for GPU acceleration if available.

For Hashcat, execute [[commands/hashcat-crack-asrep-hash]]:

```bash
hashcat -m 18200 -a 0 $_HASH_FILE.txt $_WORDLIST.txt
```

If using John, execute [[commands/john-crack-asrep-hash]]:

```bash
john --wordlist=$_WORDLIST.txt --format=krb5asrep $_HASH_FILE.txt
```

Verify cracked passwords with `hashcat --show` or `john --show`.

**Expected Output**: Recovered plaintext password, e.g., `username:password123`.

**Success Indicators**:
- Hash cracked successfully
- Plaintext password retrieved and verified

### Step 4: Query Domain for SPNs and Kerberoast Authenticated
procedure: [[procedures/Query-Domain-for-SPNS-and-Kerberoast-Authenticated]]

**Objective**: Use the cracked credentials to authenticate and query for service principal names (SPNs), then request and extract TGS tickets for Kerberoasting.

**Instructions**: Authenticate with the cracked credentials. Use Impacket GetUserSPNs to enumerate SPNs and request tickets.

Execute [[commands/getuserspns-query-spns-and-request-tgs]]:

```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_TARGET_IP -request -outputfile $_TGS_HASHES.txt
```

The tool will output TGS hashes for cracking.

**Expected Output**: TGS-REP hashes in hashcat format, e.g., `$krb5tgs$23$*serviceaccount$DOMAIN$spn*$hash`.

**Success Indicators**:
- Successful authentication with cracked creds
- SPNs enumerated and TGS tickets requested
- Hashes saved for further cracking

## Attack Chain Summary

### Key Achievements

1. Identified valid users without preauth via brute force
2. Obtained and cracked AS-REP hashes for initial credentials
3. Used credentials to perform authenticated Kerberoasting for service account access
4. Achieved credential access for lateral movement or privilege escalation

---

*Last updated: 2023-05-29T16:48:53.162677+00:00*
