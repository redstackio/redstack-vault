---
tags:
  - xxe
  - payload-preparation
  - file-upload
type: procedure
tools:
  - '[[tools/Hex-Editor]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - PHP 8
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 563a7bd0-9dbb-401e-865b-0f0f1a565a5a
created_at: '2025-12-13T09:00:27.989Z'
updated_at: '2025-12-13T09:00:27.989Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare XXE Payload in WAV File

## Summary

This procedure involves modifying PoC files and editing a .wav file with a hex editor to embed an XXE payload pointing to an attacker's server, enabling exploitation in WordPress Media Library.

## Description

The procedure prepares a malicious .wav file that embeds XML payloads exploiting the XXE vulnerability in WordPress on PHP 8. By adapting addresses in PoC files and hex-editing the .wav, attackers can ensure the payload triggers entity substitution during parsing, leading to data exfiltration or other attacks.

## Requirements

1. Access to xxe.zip PoC archive
2. Hex editor tool installed
3. Controlled web server URL

## Defense

Defensive measures and detection strategies:

- Disable external entity loading in XML parsers
- Monitor media uploads for anomalous file structures
- Use WAF rules to detect XXE patterns

## Objectives

1. Create a valid malicious .wav file with embedded XXE payload
2. Ensure payload points to attacker's server
3. Prepare for upload without file corruption

## Instructions

### Step 1: Adapt PoC Files

**Context**: Modify the files to include the attacker's server URL.

Extract and edit the two files in xxe.zip to point to your web server.

> This sets up the payload for data retrieval.

### Step 2: Hex Edit WAV File

**Context**: Insert server address at specific offset.

Use [[tools/Hex-Editor]] to modify xxe.wav at offset 0x000338CD with your server address.

> Ensures the file remains intact while embedding the payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Hex-Editor]]

## Tags

- xxe
- payload-preparation
