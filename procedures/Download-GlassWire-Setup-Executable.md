---
tags:
  - download
  - installer
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f941a95d-0ccb-4340-a766-21cc39b8107e
created_at: '2025-12-14T17:32:20.741Z'
updated_at: '2025-12-14T17:32:20.741Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Download-GlassWire-Setup-Executable

## Summary

This procedure outlines downloading the GlassWire setup executable from the official source, serving as the initial step to access the vulnerable binary containing hardcoded credentials.

## Description

In the context of analyzing the GlassWire vulnerability, this procedure involves retrieving the GlassWireSetup.exe installer (version 1.1.26.0b) which embeds the GlassWire.exe file with exposed Facebook credentials. It requires only basic internet access and targets the official download site, setting up for subsequent binary analysis.

## Requirements

1. Internet access to reach the GlassWire download page
2. Web browser or download tool
3. Local storage space for the executable file

## Defense

Defensive measures and detection strategies:

- Monitor downloads from official software sites for anomalous patterns
- Use endpoint detection to flag executable downloads in security research contexts

## Objectives

1. Acquire the vulnerable installer file
2. Confirm file integrity and version
3. Prepare for binary extraction

## Instructions

### Step 1: Access Official Download Page

**Context**: Navigate to the legitimate GlassWire website to ensure authenticity of the download.

No command required; use a web browser to visit https://www.glasswire.com/download/ and select the Windows installer for version 1.1.26.0b.

> Download the file named GlassWireSetup.exe.

### Step 2: Verify Download

**Context**: Confirm the file is complete and matches the expected version.

Check file properties to verify size and version details.

**Expected Output**: File saved locally with version 1.1.26.0b confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[download]]
- [[installer]]

