---
id: proc-uuid-1
tags:
  - recon
  - download
  - rskj
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:56.344Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Obtain-Vulnerable-RSKJ-Software

## Summary

This procedure involves downloading the specific vulnerable version of the RSKJ core JAR file from the official GitHub releases, enabling setup of the target environment for reproducing the denial-of-service vulnerability in the RLP decoding function.

## Description

The RSKJ server in version 5.0.0-FINGERROOT contains an uncontrolled resource consumption issue in the RLP.java file. To exploit this, the attacker first obtains the vulnerable software package. This step requires internet access to the GitHub repository and focuses on acquiring rskj-core-5.0.0-FINGERROOT-all.jar, which includes the flawed decode2 function. Expected outcome is possession of the JAR file, verified by file presence and size, preparing for server launch. Prerequisites include a Linux environment with wget or curl for download.

## Requirements

1. Internet access to GitHub releases page
2. Basic file management tools (e.g., wget, curl)
3. Linux OS for handling JAR files

## Defense

Defensive measures and detection strategies:

- Monitor downloads of known vulnerable software versions from public repositories
- Implement software version pinning and automated updates to patch levels
- Use endpoint detection to flag unauthorized downloads of executable JARs

## Objectives

1. Acquire the exact vulnerable RSKJ JAR for controlled exploitation testing
2. Verify file integrity to ensure reproducibility
3. Set foundation for launching the vulnerable node

## Instructions

### Step 1: Access GitHub Releases

**Context**: Navigate to the RSKJ GitHub repository releases to locate the vulnerable version.

No command required; use browser or wget to download from https://github.com/rsksmart/rskj/releases/tag/v5.0.0-FINGERROOT.

> Download rskj-core-5.0.0-FINGERROOT-all.jar directly.

### Step 2: Verify Download

**Context**: Confirm the file is obtained and matches expected size (~50MB).

Use ls -l to check:

```bash
ls -l rskj-core-5.0.0-FINGERROOT-all.jar
```

> Expected output: File listing with correct size and timestamp.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[download]]
- [[rskj]]
