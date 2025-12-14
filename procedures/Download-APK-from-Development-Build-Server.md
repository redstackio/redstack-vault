---
id: proc-download-apk-001
tags:
  - reconnaissance
  - download
  - apk
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/wget-download-apk]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:24:44.543Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Download APK from Development Build Server

## Summary

This procedure involves downloading publicly accessible Android APK files from a development build server, such as devbuilds.uber.com, to identify potential leaks of sensitive information like internal tokens.

## Description

In scenarios where development builds are hosted without proper access controls, attackers can retrieve APK files via HTTP/HTTPS. This step serves as the initial reconnaissance to obtain the artifact for further analysis. No authentication is required if the files are public, but the process assumes knowledge of the build server URL. Expected outcomes include a local copy of the APK for decompilation, highlighting risks in CI/CD pipelines that expose dev artifacts.

## Requirements

1. Internet access to the target build server (e.g., devbuilds.uber.com).
2. wget or curl installed on a Linux/macOS system.
3. Knowledge of the specific APK URL (discoverable via web search or directory browsing).

## Defense

Defensive measures and detection strategies:

- Restrict access to dev build servers with authentication (e.g., IP whitelisting or API keys).
- Monitor download logs for anomalous traffic to build endpoints.
- Use build pipeline scans to detect hardcoded secrets before artifact generation.

## Objectives

1. Obtain the APK file containing potential leaked credentials.
2. Verify file integrity for subsequent analysis.
3. Enable further reverse engineering without network dependencies.

## Instructions

### Step 1: Identify and Download the APK

**Context**: Locate the public URL for the development APK and fetch it using wget to save locally.

**Command** ([[commands/wget-download-apk]]):
```bash
wget https://devbuilds.uber.com/path/to/development-app.apk -O uber-dev.apk
```

> This command downloads the APK from the specified URL and saves it as uber-dev.apk. Expected output includes progress bars and a confirmation message like "saved 12345678/12345678 bytes". If the URL is incorrect, it will return a 404 error.

### Step 2: Verify Download

**Context**: Confirm the file is a valid APK (ZIP archive) to ensure usability in analysis.

**Command** ([[commands/unzip-test]]):
```bash
unzip -t uber-dev.apk
```

> Tests the archive integrity without extracting. Successful output: "No errors detected in compressed data." Failure indicates corruption or invalid file.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used

- [[commands/wget-download-apk]]
- [[commands/unzip-test]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[download]]
- [[apk]]
