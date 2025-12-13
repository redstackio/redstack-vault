---
url: null
tags:
  - binary-editing
  - payload-crafting
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  A hex editor for modifying binary files at specific offsets, used to embed
  payloads without corruption.
id: f43a8457-2094-4389-93fd-89f5de5afe50
created_at: '2025-12-13T09:00:27.960Z'
updated_at: '2025-12-13T09:00:27.960Z'
verified: false
validated: true
submitted: true
---
# Hex Editor

**Status**: Unverified

## Overview

Hex editors allow byte-level modification of files, essential for embedding payloads in media files like .wav without altering their structure or validity.

## Description

Tools like HxD or Bless enable precise editing at offsets, used in this context to insert attacker server addresses into .wav files for XXE exploitation.

## Features

- Byte-level editing
- Offset navigation
- File integrity preservation

## Installation

### Requirements

- Compatible OS

### Install Commands

```bash
# For example, install Bless on Ubuntu
sudo apt install bless
```

## Basic Usage

```bash
bless xxe.wav
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h` | Help |

## Examples

### Example 1: Basic Usage

```bash
bless xxe.wav
```

### Example 2: Advanced Usage

Open and edit at offset 0x000338CD.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for hex editor processes
- Check file modification timestamps

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Web-Server]]

## References

- General hex editor documentation
