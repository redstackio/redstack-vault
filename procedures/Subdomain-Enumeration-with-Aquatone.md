---
id: proc-aquatone-enum-927413
tags:
  - subdomain-enum
  - osint
type: procedure
tools:
  - '[[tools/Aquatone]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/aquatone-enum]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:27:35.652Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Subdomain-Enumeration-with-Aquatone

## Summary

Aquatone enumerates and screenshots subdomains of the target, revealing hidden domains like auth.zomato.com for Zomato reconnaissance.

## Description

Aquatone uses passive and active techniques to find subdomains, generating screenshots for visual verification. In this case, it uncovers hidden parts of Zomato's domain structure, expanding the attack surface.

## Requirements

1. Aquatone installed (Go-based)
2. Target domain
3. Wordlist for brute-force (optional)

## Defense

Defensive measures and detection strategies:

- Implement subdomain takeover protections
- Monitor DNS query patterns

## Objectives

1. List all subdomains
2. Screenshot services for analysis
3. Identify hidden assets

## Instructions

### Step 1: Discover Subdomains

**Context**: Run discovery to enumerate subdomains.

**Command** ([[commands/aquatone-enum]]):
```bash
aquatone-discover --domain zomato.com --threads 10
```

> Outputs a list of discovered subdomains; follow with screenshotting.

### Step 2: Screenshot and Verify

**Context**: Capture visuals of active subdomains.

```bash
aquatone-takeover --domain zomato.com
```

> Generates screenshots; review for exposed services.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/aquatone-enum]]

## Tools Used

- [[tools/Aquatone]]

## Tags

- [[subdomain-enum]]
- [[osint]]
