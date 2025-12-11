---
url: null
tags:
  - network
  - discovery
type: tool
platforms:
  - Windows
  - Linux
description: Command-line tool for displaying network connections.
id: b61f147f-0d3f-4866-8f52-7b29eab65144
created_at: '2025-12-11T03:47:56.446Z'
updated_at: '2025-12-11T03:47:56.446Z'
verified: false
validated: true
submitted: true
---
# netstat

**Status**: Unverified

## Overview

netstat is a built-in command-line tool for displaying active network connections, routing tables, and interface statistics, used here to identify local servers like the WebSocket on port 1235.

## Description

It helps in network troubleshooting and security audits by showing listening ports and associated processes.

## Features

- Feature 1: Display connections
- Feature 2: Show process names with -b
- Feature 3: Numerical output with -n

## Installation

### Requirements

- Built-in on Windows and most Linux distros

### Install Commands

```bash
# No installation needed
```

## Basic Usage

```bash
netstat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-a` | All connections |
| `-n` | Numerical |
| `-b` | Show executables |

## Examples

### Example 1: Basic Usage

```bash
netstat -anb
```

### Example 2: Advanced Usage

```bash
netstat -anb | grep 1235
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Command-line logging
- Detection method 2: Process monitoring

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Process-Monitor]]

## References

- Built-in documentation
