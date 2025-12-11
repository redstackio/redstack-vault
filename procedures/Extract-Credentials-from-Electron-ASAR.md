---
tags:
  - credential-exposure
  - electron
  - asar
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - macOS
  - Electron
techniques:
  - '[[Unsecured Credentials]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Credentials in Files]]'
id: 49eb088e-5ef8-4cce-b66a-e9e2e58e5306
created_at: '2025-12-11T03:48:06.069Z'
updated_at: '2025-12-11T03:48:06.069Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1552]]'
---
# Extract Credentials from Electron ASAR

## Summary

This procedure involves downloading and extracting an Electron app's ASAR archive to uncover exposed credentials, such as a GitHub PAT in a leftover .env file from the build process.

## Description

Electron apps package code into ASAR archives, which can inadvertently include sensitive files like .env if not properly cleaned during builds. This technique targets public app distributions to extract and identify credentials for further exploitation.

## Requirements

1. Access to the public Electron app DMG file
2. Node.js installed for npx asar tool
3. Basic file extraction capabilities on macOS or similar

## Defense

Defensive measures and detection strategies:

- Ensure build processes remove sensitive files before packaging
- Scan releases for credentials using tools like truffleHog

## Objectives

1. Extract ASAR contents
2. Identify exposed tokens
3. Confirm they are unused build leftovers

## Instructions

### Step 1: Download and Locate ASAR

**Context**: Obtain the app and find the ASAR file.

Download the DMG, mount it, and navigate to AppName.app/Contents/Resources/app.asar.

> No specific command; manual file handling.

### Step 2: Extract ASAR Archive

**Context**: Unpack the archive to reveal files.

Execute [[commands/npx-asar-extract]]:

```bash
npx asar extract path/to/app.asar extracted/path
```

> Extracts files including .env with GH_TOKEN.

### Step 3: Examine .env File

**Context**: Review for credentials.

Open .env and note GH_TOKEN; confirm it's not loaded by app code.

> Manual inspection; look for GitHub token format.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials in Files]]

## Commands Used

- [[commands/npx-asar-extract]]

## Tools Used

- #asar

## Tags

- credential-exposure
- electron
