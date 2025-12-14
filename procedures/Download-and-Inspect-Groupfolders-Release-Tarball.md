---
id: proc-download-groupfolders-tarball
tags:
  - recon
  - download
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/wget-download]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:27.822Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Download-and-Inspect-Groupfolders-Release-Tarball

## Summary

This procedure involves downloading the production release tarball of Nextcloud's groupfolders app from GitHub and inspecting its contents to identify potential security issues in the package structure.

## Description

In vulnerability research for open-source applications like Nextcloud, starting with the official release artifacts is crucial. The groupfolders app's tarball at version 6.0.2 contains the full app package intended for production deployment. Inspection reveals if development artifacts are mistakenly included, which can introduce risks like exposed testing code. This step sets the foundation for deeper analysis in a PHP-based web environment.

## Requirements

1. Internet access to GitHub releases
2. wget or curl installed for downloading
3. tar utility for extraction
4. Basic file system permissions

## Defense

Defensive measures and detection strategies:

- Use release integrity checks like GPG signatures on GitHub
- Scan release packages with tools like trivy for dev dependencies
- Implement CI/CD pipelines to exclude vendor/test files in production builds

## Objectives

1. Acquire the exact production package for analysis
2. Extract and catalog files to map the app structure
3. Identify any anomalous inclusions early

## Instructions

### Step 1: Download the Tarball

**Context**: Fetch the release from the public GitHub URL to obtain the unaltered package.

**Command** ([[commands/wget-download]]):
```bash
wget https://github.com/nextcloud/groupfolders/releases/download/v6.0.2/groupfolders.tar.gz
```

> This downloads the gzipped tar archive. Expected output: File saved as groupfolders.tar.gz with HTTP 200 status.

### Step 2: Extract and List Contents

**Context**: Unpack the archive to inspect the directory layout, focusing on app files and dependencies.

**Command** (tar extract):
```bash
tar -xzf groupfolders.tar.gz
ls -la
```

> Extracts files and lists them. Expected output: Directory with app root, including lib/, vendor/, and other folders.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/wget-download]]
- tar (built-in)

## Tools Used


## Tags

- recon
- download
- nextcloud
