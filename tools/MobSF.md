---
url: 'https://github.com/MobSF/Mobile-Security-Framework-MobSF'
tags:
  - mobile-analysis
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.150Z'
id: 7b067ed6-f749-43f6-84f1-088d0cbcbdc9
validated: true
submitted: true
---
# MobSF

**Status**: Unverified

## Overview

Mobile Security Framework (MobSF) is an automated testing framework for mobile app security analysis.

## Description

Supports static and dynamic analysis of Android APKs, identifying insecure storage and more.

## Features

- Feature 1: Static code analysis
- Feature 2: Dynamic instrumentation
- Feature 3: Report generation

## Installation

### Requirements

- Docker or Python/Django

### Install Commands

```bash
docker pull opensecurity/mobile-security-framework-mobsf
```

## Basic Usage

```bash
# Run server
docker run -it -p 8000:8000 opensecurity/mobile-security-framework-mobsf
```

### Common Options

Web UI upload.

## Examples

### Example 1: Basic Usage

Upload APK to http://localhost:8000.

### Example 2: Advanced Usage

Integrate with CI/CD.

## MITRE ATT&CK Mapping

### Techniques

- [[T1417]] Input Capture (mobile)

### Tactics

- [[Collection]] Collection

## Detection

N/A for analysis tool.

## Related Procedures

- [[procedures/Android-APK-Reverse-Engineering]]

## Related Tools

- [[tools/Jadx]]
- [[tools/Apktool]]

## References

- GitHub repo
