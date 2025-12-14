---
url: 'https://www.npmjs.com/package/logkitty'
tags:
  - log-viewer
  - rce-vulnerable
type: tool
verified: false
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.468Z'
id: 23641c96-f399-431a-9189-e773a0b76faa
validated: true
submitted: true
---
# logkitty

**Status**: Unverified

## Overview

Logkitty is a CLI tool for displaying formatted logs from Android and iOS devices, vulnerable in version 0.7.0 to RCE via command injection in ADB handling.

## Description

It parses and prettifies device logs using ADB for Android, but the vulnerability allows arbitrary command execution by injecting shell metacharacters into the app name parameter. Used in security testing to demonstrate client-side RCE in development tools.

## Features

- Feature 1: Formatted log output for Android/iOS
- Feature 2: App-specific log filtering
- Feature 3: Archive and search capabilities

## Installation

### Requirements

- Node.js
- ADB for Android mode

### Install Commands

```bash
npm i logkitty@0.7.0
```

## Basic Usage

```bash
logkitty --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `android` | Android mode |
| `app` | Target specific app |

## Examples

### Example 1: Basic Usage

```bash
logkitty android app com.example
```

### Example 2: Advanced Usage (Exploitation)

```bash
logkitty android app 'test; touch HACKED'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor executions of logkitty with suspicious app names
- Check for unexpected file creations post-execution

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/npm]]

## References

- Official documentation: https://www.npmjs.com/package/logkitty
- HackerOne Report: https://hackerone.com/reports/825729
