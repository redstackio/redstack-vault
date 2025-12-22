---
url: ''
tags:
  - process
  - discovery
type: tool
platforms:
  - Linux
description: Utility to search for processes based on name or command line.
id: adc837d8-4c6f-4027-bb6b-1cffd986ea33
created_at: '2025-12-14T17:24:19.369Z'
updated_at: '2025-12-14T17:24:19.369Z'
verified: false
validated: true
submitted: true
---
# pgrep

**Status**: Unverified

## Overview

pgrep searches for processes matching a pattern, used here to detect curl executions for automation in the exploit chain.

## Description

Part of procps package; with -l -f flags, lists PIDs and full command lines, enabling arg extraction for dynamic targeting.

## Features

- Feature 1: Pattern matching on full command (-f)
- Feature 2: List with command names (-l)
- Feature 3: PID output for further querying

## Installation

### Requirements

- procps package

### Install Commands

```bash
# On Debian/Ubuntu
apt install procps
```

## Basic Usage

```bash
pgrep --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -l | List full command |
| -f | Match full command line |

## Examples

### Example 1: Basic Usage

```bash
pgrep curl
```

### Example 2: Advanced Usage

```bash
pgrep -l -f curl  # 1234 curl --cookie-jar a
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]] Process Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Frequent pgrep calls in scripts
- Detection method 2: Audit logs for process enumeration

## Related Procedures

- [[procedures/Monitor-Curl-Processes-for-Automation]]

## Related Tools

- [[tools/cut]]

## References

- Man page: pgrep(1)
