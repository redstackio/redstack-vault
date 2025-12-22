---
tags:
  - recon
  - supply-chain
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:23:42.067Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 35cbf8b1-830c-4a4b-8b3d-b52a0449c905
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Examine-Install-Script-for-S3-Dependencies

## Summary

This procedure involves downloading and inspecting the Rocket.Chat install.sh script to identify dependencies on external resources like unclaimed S3 buckets, enabling discovery of supply chain vulnerabilities.

## Description

In the attack scenario, the attacker downloads the latest Rocket.Chat release from GitHub and examines the install.sh script to spot the curl command fetching a tarball from an S3 bucket. This reveals the bucket 'rocketchatbuild' as a potential hijack point. The target environment is any system with access to GitHub and basic file inspection tools. Prerequisites include internet access. Expected outcomes include identification of the vulnerable download URL, setting the stage for bucket claiming and payload injection.

## Requirements

1. Internet access to download Rocket.Chat releases from GitHub
2. Text editor or grep for script analysis
3. Basic Linux environment

## Defense

Defensive measures and detection strategies:

- Review installer scripts for hardcoded external URLs without integrity checks
- Use code signing and checksum verification in installers
- Monitor S3 bucket creations and uploads in AWS environments

## Objectives

1. Identify external dependencies in installation scripts
2. Locate unverified download sources
3. Prepare for exploitation of unclaimed resources

## Instructions

### Step 1: Download Rocket.Chat Release

**Context**: Obtain the install.sh script from the latest release to begin analysis.

Download the release tarball from GitHub and extract it to access install.sh.

### Step 2: Inspect Script for S3 URL

**Context**: Search the script for download commands to find S3 dependencies.

Use grep or a text editor to locate the curl line:

```bash
grep -i s3 install.sh
```

> This reveals the URL https://s3.amazonaws.com/rocketchatbuild/rocket.chat-develop.tgz, indicating an unverified external fetch.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- supply-chain
