---
tags:
  - dns
  - verification
  - takeover
type: procedure
tools:
  - '[[tools/Subjack]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T05:32:23.237Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ba65f6da-6713-4047-a6c3-36ebd38de9ed
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Verify Dangling DNS Record

## Summary

This procedure checks DNS records of enumerated subdomains for pointers to decommissioned third-party services, verifying takeover potential as in the blog.owox.com vulnerability.

## Description

After enumeration, inspect CNAME or other DNS records to identify dangling pointers (e.g., to unused AWS S3 buckets or Heroku apps). Tools like dig query records, and specialized scanners check if the service is claimable. In the OWOX case, the record allowed claiming the subdomain for impersonation. Prerequisites include enumerated subdomain list; outcomes include confirmation of exploitable misconfigurations.

## Requirements

1. List of subdomains from prior enumeration
2. Access to DNS resolution tools
3. Knowledge of common third-party services (e.g., GitHub Pages, Heroku)

## Defense

Defensive measures and detection strategies:

- Regularly audit and cleanup unused DNS records
- Implement monitoring for DNS changes via tools like DNSSec
- Use subdomain management tools to track third-party integrations

## Objectives

1. Query DNS for misconfigured records
2. Confirm service is decommissioned and claimable
3. Prioritize high-impact subdomains like 'blog'

## Instructions

### Step 1: DNS Record Lookup

**Context**: Resolve the CNAME or A record for the subdomain to identify the pointing service.

**Command** ([[commands/dig-dns-lookup]]):
```bash
 dig CNAME blog.owox.com
```

> This queries the CNAME record. Expected output: Points to a service like 'decommissioned.herokuapp.com' if dangling.

### Step 2: Takeover Vulnerability Scan

**Context**: Use a scanner to check if the pointed service allows claiming.

**Command** (Subjack usage):
```bash
subjack -w live-subdomains.txt -t 100 -timeout 30 -o takeovers.json -ssl
```

> This tests against known takeover fingerprints. Expected output: JSON with vulnerable subdomains.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/Subjack]]

## Tags

- [[DNS]]
- [[verification]]
