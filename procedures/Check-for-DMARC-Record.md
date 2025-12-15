---
id: proc-uuid-001
tags:
  - dmarc
  - dns-query
  - reconnaissance
type: procedure
tools:
  - '[[tools/DMARC-Inspector]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dmarc-query]]'
verified: false
platforms:
  - Web
  - Email/DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:30:58.787Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Check-for-DMARC-Record

## Summary

This procedure queries a domain's DNS TXT records to check for the presence of a DMARC policy, identifying potential email spoofing vulnerabilities due to misconfiguration.

## Description

DMARC (Domain-based Message Authentication, Reporting, and Conformance) is an email authentication protocol that builds on SPF and DKIM. Without a DMARC record, attackers can spoof emails from the domain, as receiving servers may not enforce alignment checks. This procedure uses online tools or DNS queries to inspect the _dmarc subdomain TXT record. In the scenario for paragonie.com, no record was found, enabling phishing risks despite other mitigations like GPG.

## Requirements

1. Internet access for DNS queries
2. Domain name to inspect (e.g., paragonie.com)
3. Optional: Access to command-line tools like dig for manual verification

## Defense

Defensive measures and detection strategies:

- Publish a DMARC policy (e.g., p=none for monitoring) in DNS TXT records
- Monitor DMARC reports for spoofing attempts
- Use email gateways that enforce DMARC

## Objectives

1. Confirm absence of DMARC record
2. Identify email authentication gaps
3. Assess spoofing potential

## Instructions

### Step 1: Query DNS Using Online Tool

**Context**: Use a web-based inspector to avoid local setup.

**Command** (N/A - Web Tool):

Access [[tools/DMARC-Inspector]] at https://dmarcian.com/dmarc-inspector/paragonie.com and enter the domain.

> The tool queries _dmarc.paragonie.com TXT and reports 'No DMARC record published' if missing.

### Step 2: Manual Verification with DNS Command

**Context**: For offline confirmation, use a DNS resolver.

**Command** ([[commands/dig-dmarc-query]]):

```bash
dig TXT _dmarc.paragonie.com
```

> Expected output: No TXT record or empty response, confirming absence. If present, it would show v=DMARC1; p=... policy.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Network Information

### Sub-Techniques

- N/A

## Commands Used

- [[commands/dig-dmarc-query]]

## Tools Used

- [[tools/DMARC-Inspector]]

## Tags

- dmarc
- dns
- reconnaissance
