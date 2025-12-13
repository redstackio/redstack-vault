---
url: null
tags:
  - network
  - redirect
type: tool
platforms:
  - Linux
description: >-
  Multipurpose relay for bidirectional data transfer, used for setting up
  listeners and handling redirects.
id: 61c93252-4509-4172-a28d-a70021945b0a
created_at: '2025-12-13T09:01:17.557Z'
updated_at: '2025-12-13T09:01:17.557Z'
verified: false
validated: true
submitted: true
---
# socat

**Status**: Unverified

## Overview

socat is a command-line utility that establishes two bidirectional byte streams and transfers data between them, commonly used in security testing for creating listeners and handling network connections.

## Description

It supports various protocols and is ideal for offensive security tasks like setting up redirect servers in exploitation chains involving HTTP manipulations.

## Features

- Feature 1: Bidirectional data transfer
- Feature 2: Support for TCP, UDP, and more
- Feature 3: Forking and reuse options for servers

## Installation

### Requirements

- Linux environment
- Standard package manager

### Install Commands

```bash
sudo apt install socat
```

## Basic Usage

```bash
socat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
socat TCP-LISTEN:443 TCP:localhost:8443
```

### Example 2: Advanced Usage

```bash
socat -v TCP-LISTEN:443,fork TCP:example.com:80
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor unusual listeners on non-standard ports
- Detection method 2: Log verbose output in server environments

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/nc]]
- [[tools/netcat]]

## References

- Official man page
- Security tool repositories
