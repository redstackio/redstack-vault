---
url: null
tags:
  - network
  - manual
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Networking utility for reading/writing network connections, used for raw HTTP
  sending.
id: ce429be5-7af2-426e-a575-e04895941e84
created_at: '2025-12-13T09:01:21.952Z'
updated_at: '2025-12-13T09:01:21.952Z'
verified: false
validated: true
submitted: true
---
# ncat

**Status**: Unverified

## Overview

ncat is a feature-rich networking tool for creating connections and sending raw data, useful for manual exploitation of HTTP desync by pasting raw requests.

## Description

Part of Nmap suite, it allows SSL connections and raw input, perfect for replicating scripted attacks manually.

## Features

- Feature 1: SSL support
- Feature 2: Raw data sending
- Feature 3: Connection proxying

## Installation

### Requirements

- Nmap installed

### Install Commands

```bash
sudo apt install nmap
```

## Basic Usage

```bash
ncat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--ssl` | Enable SSL |

## Examples

### Example 1: Basic Usage

```bash
ncat example.com 80
```

### Example 2: Advanced Usage

```bash
ncat --ssl target 443
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual ncat processes
- Detection method 2: Raw TCP/SSL traffic

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/cURL]]

## References

- Nmap documentation
