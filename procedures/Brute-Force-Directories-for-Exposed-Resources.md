---
tags:
  - directory-brute-force
  - information-disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/turbo-intruder-directory-brute]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:58.008Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: e68ee1a0-315f-4124-81cb-c30475155d34
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Brute Force Directories for Exposed Resources

## Summary

Brute-force web directories on a target to uncover hidden files like .git repositories, leading to credential leaks.

## Description

Directory brute-forcing uses wordlists to probe endpoints. In this case, SecLists common web content wordlist targets app.bountypay.h1ctf.com, revealing .git/HEAD and .git/config for repo exposure.

## Requirements

1. Burp Suite with Turbo Intruder
2. SecLists wordlist for directories
3. Proxy setup for traffic interception

## Defense

Defensive measures: Use web application firewalls (WAF) to block fuzzing patterns; Detection: Alert on repeated 404s or unusual paths.

## Objectives

1. Discover exposed directories
2. Access sensitive files
3. Expected outcome: .git config details

## Instructions

### Step 1: Launch Brute Force

**Context**: Fuzz directories for exposures.

**Command** ([[commands/turbo-intruder-directory-brute]]):
```bash
# Turbo Intruder in Burp: GET §s HTTP/1.1\nHost: app.bountypay.h1ctf.com, payloads from SecLists
```

> Probes paths like /.git/HEAD. Expected output: 200 responses for exposed files.

### Step 2: Verify Exposure

**Context**: Download and inspect found files.

Access via browser: app.bountypay.h1ctf.com/.git/config.

> Expected output: Git remote URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/turbo-intruder-directory-brute]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Turbo-Intruder]]

## Tags

- directory-brute-force
- information-disclosure
