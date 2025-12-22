---
url: ''
tags:
  - discovery
type: tool
platforms:
  - Linux
description: Displays the current user identity.
id: f2e1188b-d885-467c-b706-279f29b956a1
created_at: '2025-12-11T06:10:22.575Z'
updated_at: '2025-12-11T06:10:22.575Z'
verified: false
validated: true
submitted: true
---
# whoami

**Status**: Unverified

## Overview

Whoami prints the effective username, used to confirm access post-exploit.

## Description

Simple tool for user discovery in compromised environments.

## Features

- User identification

## Installation

### Requirements

- Linux system (coreutils)

### Install Commands

Pre-installed.

## Basic Usage

```bash
whoami
```

### Common Options

| Option | Description |
|--------|-------------|
| (none) | Default behavior |

## Examples

### Example 1: Basic Usage

```bash
whoami
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Owner-User Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Command execution logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[id]]

## References

- Man page: whoami(1)
