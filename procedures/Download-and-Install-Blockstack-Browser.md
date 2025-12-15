---
tags:
  - setup
  - installation
  - blockstack
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:32:10.205Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 0565c4d7-4384-4384-98b8-c6531ee0b6da
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Download-and-Install-Blockstack-Browser

## Summary

This procedure outlines downloading and installing the Blockstack Browser DMG on macOS, setting the stage for analyzing its network behavior and identifying credential leakage vulnerabilities.

## Description

The Blockstack Browser is a desktop application for interacting with the Blockstack ecosystem. In a security assessment, downloading and installing it allows local execution to observe internal traffic. This step is essential for reproducing the environment where the Core API Password is generated and potentially leaked during sign-up flows. The target environment is macOS, with no special privileges required beyond standard user access.

## Requirements

1. macOS system (e.g., 10.14.4 or later)
2. Internet access for downloading the DMG
3. Sufficient disk space (~100MB)

## Defense

Defensive measures and detection strategies:

- Monitor downloads from GitHub releases for unauthorized software
- Use application whitelisting to restrict installations
- Scan DMG files with antivirus before mounting

## Objectives

1. Acquire the vulnerable Blockstack Browser version
2. Install it locally without errors
3. Prepare for subsequent traffic analysis

## Instructions

### Step 1: Download the DMG File

**Context**: Fetch the specific release version to ensure reproducibility of the vulnerability.

No command required; use a browser to download from the URL.

> Visit https://github.com/blockstack/blockstack-browser/releases/download/v0.36.1/Blockstack-for-macOS-v0.36.1.dmg and save the file.

### Step 2: Install the Application

**Context**: Mount the DMG and drag the app to Applications folder to complete setup.

No command required; follow macOS installer prompts.

> Double-click the DMG, agree to any prompts, and move Blockstack Browser to /Applications.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- setup
- blockstack
- macos
