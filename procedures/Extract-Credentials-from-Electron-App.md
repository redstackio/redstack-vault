---
tags:
  - credential-exposure
  - electron
type: procedure
tools:
  - '[[tools/npx]]'
  - '[[tools/asar]]'
  - '[[tools/curl]]'
  - '[[tools/git]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/npx-asar-extract]]'
  - '[[commands/asar-extract]]'
  - '[[commands/curl-github-user-auth]]'
platforms:
  - macOS
  - Electron
techniques:
  - '[[Unsecured Credentials]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Credentials in Files]]'
id: 6863ea82-5a28-4108-b35a-c0603e527806
created_at: '2025-12-11T06:10:40.500Z'
updated_at: '2025-12-11T06:10:40.500Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1552]]'
---
# Extract Credentials from Electron App

## Summary

This procedure involves downloading a public Electron app and extracting its asar archive to uncover leftover credentials in files like .env, which may have been included accidentally during the build process.

## Description

In this attack scenario, an attacker targets a public macOS Electron app from Shopify, extracts the app.asar file using asar tools, and examines the contents to find an exposed GitHub Personal Access Token (PAT) in a .env file. This credential exposure allows potential access to private repositories. The procedure assumes access to the public download link and requires tools like npx and asar. Expected outcomes include revealing the GH_TOKEN for further exploitation.

## Requirements

1. Access to the public download link for the macOS Electron app
2. Node.js environment for running npx and asar
3. Basic command-line proficiency

## Defense

Defensive measures and detection strategies:

- Ensure build processes remove sensitive files like .env before packaging
- Monitor for unusual extractions or API calls to GitHub from unknown IPs

## Objectives

1. Uncover embedded credentials in app artifacts
2. Obtain valid GitHub PAT
3. Prepare for token validation and access testing

## Instructions

### Step 1: Download the Electron App

**Context**: Obtain the macOS version of the public Electron app to begin extraction.

Download from the provided link.

### Step 2: Extract app.asar

**Context**: Dissect the app to access internal files.

**Command** ([[commands/npx-asar-extract]]):
```bash
npx asar extract path/to/app.asar extracted/path
```

> This extracts the asar archive, revealing files including .env.

Alternatively, use ([[commands/asar-extract]]):
```bash
asar extract app.asar asar-out-dir
```

> Outputs to a directory containing the .env file with GH_TOKEN.

### Step 3: Examine .env File

**Context**: Review the extracted .env for credentials.

Manually inspect the file to identify GH_TOKEN.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials in Files]]

## Commands Used

- [[commands/npx-asar-extract]]
- [[commands/asar-extract]]

## Tools Used

- [[tools/npx]]
- [[tools/asar]]

## Tags

- [[credential-exposure]]
- [[electron]]
