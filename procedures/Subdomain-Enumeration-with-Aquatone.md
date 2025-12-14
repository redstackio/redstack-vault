---
id: proc-aquatone-enum-zomato
tags:
  - subdomain-enum
  - recon
type: procedure
tools:
  - '[[tools/Aquatone]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/aquatone-enumerate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T03:46:32.259Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Subdomain-Enumeration-with-Aquatone

## Summary

Use Aquatone to enumerate and screenshot hidden subdomains for Zomato, discovering assets like auth.zomato.com.

## Description

Aquatone performs subdomain brute-forcing and visualization, aiding in mapping the target's domain footprint.

## Requirements

1. Aquatone installed
2. Target domain
3. Wordlist for brute-force

## Defense

- Monitor for subdomain brute-force attempts
- Use certificate transparency logs

## Objectives

1. List subdomains
2. Screenshot for verification
3. Identify hidden assets

## Instructions

### Step 1: Discover Subdomains

**Context**: Run discovery on target.

**Command** ([[commands/aquatone-enumerate]]):
```bash
aquatone-discover --domain zomato.com
```

> Generates list and screenshots of subdomains.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/aquatone-enumerate]]

## Tools Used

- [[tools/Aquatone]]

## Tags

- [[subdomain-enum]]
- [[recon]]
