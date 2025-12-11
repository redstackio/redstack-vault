---
url: null
tags:
  - network
  - reverse-shell
type: tool
platforms:
  - Linux
description: >-
  Utility for reading and writing network connections, used for reverse shell
  listeners.
id: ea355a72-5381-499f-b125-238fb6808c4d
created_at: '2025-12-11T06:10:32.866Z'
updated_at: '2025-12-11T06:10:32.866Z'
verified: false
validated: true
submitted: true
---
# Netcat

**Status**: Unverified

## Overview

Netcat is a networking utility for reading from and writing to network connections using TCP or UDP, commonly used to set up listeners for reverse shells.

## Description

In this attack, it's inferred for listening on port 8080 to receive the reverse shell connection from the exploited server.

## Features

- TCP/UDP client and server
- Port scanning
- Data transfer

## Installation

### Requirements

- Linux environment

### Install Commands

```bash
sudo apt install netcat
```

## Basic Usage

```bash
nc -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-l` | Listen mode |
| `-v` | Verbose |
| `-n` | No DNS |
| `-p` | Port |

## Examples

### Example 1: Basic Usage

```bash
nc -lvnp 8080
```

### Example 2: Advanced Usage

```bash
nc -lvnp 8080 -e /bin/sh
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for listening ports
- Network traffic analysis

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/ImageMagick]]

## References

- Netcat man page
