---
tags:
  - xss
  - recon
  - csgo
type: procedure
tools:
  - '[[tools/unzipping-tool]]'
  - '[[tools/grep]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Windows
  - 'CS:GO'
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9e9d8796-d471-471d-a279-fe6b9b8a149d
created_at: '2025-12-14T00:11:25.224Z'
updated_at: '2025-12-14T00:11:25.224Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract and Identify Panorama UI Vulnerabilities

## Summary

This procedure involves extracting CS:GO Panorama UI files and searching for vulnerable tags that allow raw HTML parsing, identifying XSS vulnerabilities in disconnect and kick messages.

## Description

By unzipping the code.pbin file and grepping for 'html="true"', attackers can locate unsanitized HTML inputs in UI layouts like popup_generic.xml, enabling XSS attacks that lead to code execution via SteamOverlayAPI.

## Requirements

1. Access to CS:GO installation directory
2. Unzipping tool and grep installed
3. Basic knowledge of file searching and XML parsing

## Defense

Defensive measures and detection strategies:

- Patch Panorama UI to sanitize HTML inputs
- Monitor for unusual file extractions or server kicks

## Objectives

1. Identify vulnerable UI components
2. Confirm locations for HTML injection
3. Prepare for payload testing

## Instructions

### Step 1: Extract UI Files

**Context**: Unzip the Panorama code bundle to access layout files.

Use [[tools/unzipping-tool]] to extract steamapps\common\Counter-Strike Global Offensive\csgo\panorama\code.pbin.

> This reveals XML layout files for analysis.

### Step 2: Search for Vulnerable Tags

**Context**: Grep through files to find html="true" attributes.

Use [[tools/grep]]:

```bash
grep -r 'html="true"' panorama/layout/
```

> Expected to find matches in chat.xml and popup_generic.xml.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/unzipping-tool]]
- [[tools/grep]]

## Tags

- [[xss]]
- [[recon]]
- [[csgo]]
