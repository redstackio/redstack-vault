---
url: 'https://github.com/skylot/jadx'
tags:
  - decompiler
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.874Z'
id: 73cd4fbe-b167-4520-b6eb-b747f85d3389
validated: true
submitted: true
---
# JADX

**Status**: Unverified

## Overview

Android APK decompiler to Java source.

## Description

GUI and CLI for reverse engineering APKs, extracting manifests and code.

## Features

- Feature 1: Dex to Java decompilation
- Feature 2: Resource viewing
- Feature 3: Searchable output

## Installation

### Requirements

- Java

### Install Commands

```bash
# Download release, run jadx-gui
```

## Basic Usage

```bash
jadx-gui file.apk
```

### Common Options

| Option | Description |
|--------|-------------|
| -d | Output dir |

## Examples

### Example 1: Basic Usage

Decompile APK.

### Example 2: Advanced Usage

CLI mode.

## MITRE ATT&CK Mapping

### Techniques

- [[T1407]] Structure Consumption

### Tactics

- [[Discovery]] Discovery

## Detection

File access to APKs.

## Related Procedures

- [[procedures/Download-and-Reverse-Engineer-APK]]

## Related Tools

- [[tools/ADB]]

## References

- GitHub repo
