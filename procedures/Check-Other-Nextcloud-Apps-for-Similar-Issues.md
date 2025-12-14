---
id: proc-check-other-apps
tags:
  - recon
  - nextcloud
  - supply-chain
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/wget-download]]'
  - '[[commands/find-phpunit]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:23:27.787Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Check-Other-Nextcloud-Apps-for-Similar-Issues

## Summary

This procedure extends the vulnerability research by downloading and inspecting other Nextcloud apps (carnet, discoursesso, extract) for similar inclusions of PHPUnit in their production releases.

## Description

The groupfolders issue may indicate a broader packaging problem in the Nextcloud app ecosystem. By replicating the inspection on apps listed at https://apps.nextcloud.com, researchers can identify patterns of dev dependency leakage, amplifying the report's impact.

## Requirements

1. List of target app URLs from apps.nextcloud.com
2. wget and find commands
3. Extracted tarballs for each app

## Defense

Defensive measures and detection strategies:

- Standardize release processes across Nextcloud apps with automated dev exclusion
- Community audits via Nextcloud's security team
- Dependency scanning in app submission guidelines

## Objectives

1. Download releases for specified apps
2. Search for PHPUnit inclusions
3. Document findings for comprehensive reporting

## Instructions

### Step 1: Download Target App Tarballs

**Context**: Fetch releases similar to groupfolders.

**Command** ([[commands/wget-download]]):
```bash
wget https://github.com/nextcloud/carnet/releases/download/v3.7.0/carnet.tar.gz
# Repeat for discoursesso and extract
```

> Expected output: Tarballs saved for each app.

### Step 2: Extract and Search for PHPUnit

**Context**: Inspect each for vendor/phpunit.

**Command** ([[commands/find-phpunit]]):
```bash
tar -xzf carnet.tar.gz
find . -name "*phpunit*"
# Repeat for other apps
```

> Expected output: PHPUnit paths if present, confirming similar issues.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/wget-download]]
- [[commands/find-phpunit]]

## Tools Used


## Tags

- recon
- nextcloud
- supply-chain
