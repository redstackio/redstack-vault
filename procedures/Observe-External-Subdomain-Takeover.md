---
id: proc-observe-takeover
tags:
  - subdomain-takeover
  - dns
  - impact
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.416Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe External Subdomain Takeover

## Summary

This procedure monitors and documents when an external party claims the subdomain after tester removal, demonstrating full takeover impact.

## Description

Post-cart removal, another user (e.g., with a US credit card) claims the hostname, gaining control to host arbitrary content. The procedure involves re-checking DNS and accessing the site to observe changes. Target: Post-claim subdomain; outcomes: Proof of control transfer, enabling phishing/XSS/malware.

## Requirements

1. Monitoring tools for DNS changes
2. Access to the subdomain URL
3. Timeline awareness post-removal

## Defense

Defensive measures and detection strategies:

- Implement real-time DNS monitoring with anomaly detection
- Use WHOIS alerts for subdomain registrations
- Enforce strict access controls on DNS providers

## Objectives

1. Detect claim by external actor
2. Verify content hosting changes
3. Assess impact on brand/security

## Instructions

### Step 1: Re-Query DNS

**Context**: Check for updates after removal.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig web.mopub.com
```

> Expected: Records now point to claimant's configuration.

### Step 2: Access and Inspect Content

**Context**: Visit the subdomain to confirm takeover.

Use browser to load http://web.mopub.com and note any new content.

> Expected: Arbitrary or malicious pages hosted, indicating full control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[Impact]]
