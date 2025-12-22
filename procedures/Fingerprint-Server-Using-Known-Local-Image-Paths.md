---
tags:
  - fingerprinting
  - ssrf
  - linux
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0e4d2781-5ade-4113-b9a4-cd2ffba190a3
created_at: '2025-12-14T03:46:14.348Z'
updated_at: '2025-12-14T03:46:14.348Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Fingerprint Server Using Known Local Image Paths

## Summary

Leverages the image oracle to test presence of documentation images, identifying installed packages like libpng12-dev on the Linux backend.

## Description

By oracling paths from common Linux packages (e.g., /usr/share/doc/libfreetype6/tutorial/metrics.png), external requests reveal software stack without XXE, aiding in targeted attacks.

## Requirements

1. List of distro-specific image paths (e.g., Ubuntu/Debian docs)
2. Oracle SVG generator

## Defense

Defensive measures and detection strategies:

- Remove or restrict access to doc images in parsers
- Obfuscate package paths
- Detect patterns of local path probes via logs

## Objectives

1. Confirm package installations
2. Infer OS version
3. Build server profile

## Instructions

### Step 1: Select Test Paths

**Context**: Choose known paths.

Paths: /usr/share/doc/libpng12-dev/examples/pngtest.png, /usr/share/doc/libfreetype6/tutorial/metrics.png, /usr/share/doc/libexpat1-dev/expat.html/expat.png

### Step 2: Test via Oracle Uploads

**Context**: Upload SVG with each path in oracle.

For each, check if external request occurs.

> Presence confirms packages.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[fingerprinting]]
- [[server-recon]]
