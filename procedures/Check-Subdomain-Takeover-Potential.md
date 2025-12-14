---
tags:
  - subdomain-takeover
  - dns
type: procedure
tools:
  - '[[tools/Subjack]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T03:16:20.691Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 46353d27-8124-4f80-aa61-547adbb6f777
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Check-Subdomain-Takeover-Potential

## Summary

This procedure scans unresolved subdomains for takeover vulnerabilities by checking against known cloud providers and services that allow claiming unused pointers.

## Description

For targets like presentatie.werkenbijmcdonalds.nl, this involves fingerprinting DNS records for dangling CNAMEs to services such as AWS S3, GitHub Pages, or Heroku. If the service is unused, attackers can register it to control the subdomain. Requires tool installation; expected outcome is a vulnerability report enabling exploitation.

## Requirements

1. List of subdomains (e.g., from enumeration)
2. Installed takeover detection tool
3. Network access to target DNS

## Defense

Defensive measures and detection strategies:

- Remove or redirect dangling DNS records
- Implement monitoring for subdomain claims
- Use private DNS for sensitive subdomains

## Objectives

1. Fingerprint potential takeover services
2. Confirm claimability
3. Generate exploitation report

## Instructions

### Step 1: Prepare Subdomain List

**Context**: Create a file with target subdomains for scanning.

**Instructions**: Echo the target into a file:

```bash
echo "presentatie.werkenbijmcdonalds.nl" > subdomains.txt
```

### Step 2: Run Takeover Scan

**Context**: Use the tool to check for vulnerabilities.

**Command** ([[tools/Subjack]]):
```bash
subjack -w subdomains.txt -t 100 -o takeover_results.json -ssl
```

> The tool queries each subdomain and matches against 50+ providers. Expected output: JSON with vulnerable flags if the subdomain points to a claimable service.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Subjack]]

## Tags

- [[subdomain-takeover]]
- [[DNS]]
