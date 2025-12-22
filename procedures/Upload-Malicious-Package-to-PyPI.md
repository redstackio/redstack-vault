---
id: proc-upload-pypi
tags:
  - pypi
  - upload
  - package-distribution
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.187Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Malicious-Package-to-PyPI

## Summary

This procedure uploads a crafted Python package containing XSS payloads in metadata to the public PyPI repository, making it available for mirroring by services like Uber's archive.uber.com.

## Description

The upload leverages standard PyPI tools to publish the package, where the malicious home_page and download_url fields are stored in the repository's metadata. Once uploaded, any mirroring process that fetches and displays this metadata without validation becomes vulnerable. This step requires a registered PyPI account and uses tools like twine for secure upload. Expected outcomes include the package being publicly accessible and indexed on PyPI.

## Requirements

1. Registered PyPI account with upload permissions
2. Python package built as .tar.gz
3. twine or setuptools installed for upload

## Defense

Defensive measures and detection strategies:

- PyPI-side validation of metadata URLs to reject javascript: schemes
- Rate limiting on package uploads to prevent abuse
- Automated scanning of new packages for malicious payloads

## Objectives

1. Distribute the malicious package publicly
2. Propagate XSS payload to dependent mirrors
3. Enable downstream exploitation without direct target access

## Instructions

### Step 1: Install Upload Tool

**Context**: Ensure twine is available for secure PyPI uploads.

```bash
pip install twine
```

> Twine handles authentication and upload securely.

### Step 2: Upload the Package

**Context**: Submit the built .tar.gz to PyPI.

```bash
twine upload dist/ignore-me-1.0.tar.gz
```

> Enter PyPI credentials when prompted; successful upload confirms the package is now live on PyPI.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- pypi
- upload
- distribution
