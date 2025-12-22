---
id: 588255c0-9513-4cee-bdad-6eb2ed7c5da2
name: Query-Domain-for-SPNS-and-Kerberoast-Authenticated
type: procedure
verified: true
submitted: false
created_at: '2019-12-04T19:39:54.389336+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[cme-smb-enable-rdp]]'
sub_techniques: []
tags:
  - kerberoasting
  - spn
  - network
commands:
  - '[[commands/getuserspns-query-spns-and-request-tgs]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Query-Domain-for-SPNS-and-Kerberoast-Authenticated

## Summary

This procedure uses valid domain credentials to query Active Directory for service principal names (SPNs) associated with user accounts, then requests TGS tickets for those services to obtain crackable Kerberos ticket hashes. It's an authenticated Kerberoasting attack targeting service accounts for privilege escalation.

## Description

Kerberoasting involves requesting TGS tickets for SPN-registered services using legitimate credentials, receiving encrypted tickets (using the service account's password hash) that can be cracked offline. SPNs identify services like SQL or HTTP; high-privilege service accounts are prime targets. This requires initial creds but no service access.

## Requirements

1. Valid domain credentials (username/password)
2. Network access to DC (port 88)
3. Impacket GetUserSPNs.py tool
4. Domain details (name, DC IP)

## Defense

Defensive measures and detection strategies:

- Randomize and rotate service account passwords regularly
- Limit SPN registrations to necessary services
- Monitor TGS requests for unusual patterns (Event ID 4769)
- Use minimum necessary privileges for service accounts
- Enable Kerberos ticket encryption with AES

## Objectives

1. Enumerate SPNs in the domain
2. Request TGS tickets for identified services
3. Extract hashes for offline cracking

## Instructions

### Step 1: Authenticate and Query SPNs

**Context**: Use credentials to query AD for users with SPNs.

The command handles this; no separate step.

### Step 2: Request TGS Tickets and Dump Hashes

**Context**: Send TGS-REQ for each SPN to get encrypted tickets in crackable format.

**Command** ([[commands/getuserspns-query-spns-and-request-tgs]]):

```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_TARGET_IP -request -outputfile $_KERB_HASHES.txt
```

> Outputs SPN details and `$krb5tgs$` hashes to file. Expected: List of services with hashes like `$krb5tgs$23$*service$DOMAIN$SPN*$hash`.

### Step 3: Review and Prepare Hashes

**Context**: Inspect output for high-value targets (e.g., admin services).

Filter hashes: `grep 'krb5tgs' $_KERB_HASHES.txt > crackable.txt`. Proceed to cracking.
