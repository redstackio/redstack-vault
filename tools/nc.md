---
url: ''
tags:
  - shell
type: tool
platforms:
  - Linux
description: Network tool for connections and shells
id: 0fb5fff2-1d16-4662-8d62-944e5db1bcf6
created_at: '2025-12-11T03:48:05.950Z'
updated_at: '2025-12-11T03:48:05.950Z'
verified: false
validated: true
submitted: true
---
# nc

**Status**: Unverified

## Overview

Netcat for creating listeners and handling reverse shells.

## Description

Versatile tool for network debugging and exploitation.

## Features

- Listening
- Connecting
- Port scanning

## Installation

### Requirements

- Installed on most systems

### Install Commands

```bash
apt install netcat
```

## Basic Usage

```bash
nc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-vnlkp` | Listen options |

## Examples

### Example 1: Basic Usage

```bash
nc -vnlkp 12345
```

## MITRE ATT&CK Mapping

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

- Monitor ports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Netcat]]

## References

- Nc man page
