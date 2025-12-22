---
id: t2b2c3d4-e5f6-7890-abcd-ef1234567899
name: Malstaller-Batch-Script
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.810Z'
platforms:
  - Windows
tags:
  - batch
  - rce
url: null
validated: true
submitted: true
---

# Malstaller-Batch-Script

**Status**: Unverified

## Overview

Malstaller.bat is a custom malicious batch script used in the Malstaller attack to log triggered URLs to protected areas and launch the browser, demonstrating RCE with elevated privileges via registry hijacking.

## Description

This script captures %1 (URL), logs it with date to C:\mal_log.txt, and executes Firefox to mask activity. It's designed for local deployment on Windows desktops and executes silently in elevated contexts triggered by installers.

## Features

- Feature 1: URL argument capture and persistence
- Feature 2: Elevated file writing for proof-of-concept
- Feature 3: Stealthy browser launch to evade detection

## Installation

### Requirements

- Windows with Command Prompt access
- Firefox installed

### Install Commands

```cmd
# Create via echo or notepad
notepad C:\Users\%USERNAME%\Desktop\malstaller.bat
```

## Basic Usage

```cmd
C:\Users\%USERNAME%\Desktop\malstaller.bat https://example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| %1 | URL parameter | Required |

## Examples

### Example 1: Basic Usage

```cmd
malstaller.bat https://privacy-policy.com
```

> Logs URL and opens browser.

### Example 2: Advanced Usage

```cmd
# In elevated context via hijack
malstaller.bat %1
```

> Runs during installer trigger.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]] Windows Command Shell

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Hash-based detection of .bat files with echo and browser launch patterns
- Monitor desktop for new batch files via file integrity monitoring

## Related Procedures

- [[procedures/Create-Malicious-Batch-Script-for-URL-Logging]]

## Related Tools

- [[tools/Registry-Editor]]

## References

- HackerOne Report: https://hackerone.com/reports/165969
