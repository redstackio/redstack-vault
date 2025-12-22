---
id: proc-uuid-004
tags:
  - tld-verification
  - domain-registration
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-verify-fix]]'
verified: false
platforms:
  - DNS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:39.497Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-TLD-Registration-and-Fix

## Summary

This procedure verifies if a TLD from a CNAME is registered and available for takeover, then confirms DNS resolution after a fix by re-querying the record.

## Description

After identifying an unregistered TLD, check against official lists like IANA's. If available, register it to takeover the subdomain. Post-fix (e.g., by defender), re-query to ensure the CNAME is removed and replaced with a valid A record, preventing exploitation.

## Requirements

1. Access to IANA TLD list (http://data.iana.org/TLD/tlds-alpha-by-domain.txt)
2. Domain registrar account for purchase
3. DNS query tool for verification

## Defense

Defensive measures and detection strategies:

- Maintain an inventory of all DNS records and TLDs used
- Automate checks for unregistered TLDs in CNAMEs
- Respond to reports by null-routing or removing vulnerable records

## Objectives

1. Confirm TLD availability for registration
2. Execute takeover by purchasing and configuring the domain
3. Validate fix by checking for proper DNS resolution

## Instructions

### Step 1: Check TLD Status

**Context**: Verify if the TLD is registered using official sources.

Download and grep the IANA list:

```bash
grep ".tld" http://data.iana.org/TLD/tlds-alpha-by-domain.txt
```

> If absent, the TLD is available; proceed to register via a registrar.

### Step 2: Post-Fix Verification

**Context**: After remediation, query DNS to confirm the change.

**Command** ([[commands/dig-verify-fix]]):

```bash
dig subdomain.example.com
```

> Expected output: NOERROR with A record (e.g., 10.0.48.31) instead of CNAME to unregistered TLD.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/dig-verify-fix]]

## Tools Used

- [[tools/dig]]

## Tags

- [[tld-verification]]
- [[domain-registration]]
- [[subdomain-takeover]]
