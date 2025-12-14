---
id: tool-uuid-2
url: 'https://www.npmjs.com/package/bunyan'
tags:
  - logging
  - cli
type: tool
verified: false
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.098Z'
validated: true
submitted: true
---
# bunyan

**Status**: Unverified

## Overview

Bunyan is a JSON logging library for Node.js with a CLI tool for processing log files, vulnerable to command injection in version 1.8.12's PID search feature.

## Description

The bunyan CLI (bin/bunyan) supports options like -p for PID filtering via shell commands, which in vulnerable versions allows injection. Used in security testing to demonstrate RCE in logging utilities.

## Features

- Feature 1: JSON log formatting and parsing
- Feature 2: PID and process filtering
- Feature 3: Streaming log output

## Installation

### Requirements

- Node.js
- npm

### Install Commands

```bash
npm install bunyan@1.8.12
```

## Basic Usage

```bash
bunyan --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p` | PID search pattern |
| `-f` | Filter by field |

## Examples

### Example 1: Basic Usage

```bash
bunyan log.json
```

### Example 2: Advanced Usage

```bash
bunyan -p "S'11;touch hacked ;'"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]]
- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Execution of bin/bunyan with -p flag
- child_process.exec calls to ps/grep
- Unexpected file creations post-execution

## Related Procedures

- [[procedures/Exploit-Bunyan-PID-Search-Injection]]

## Related Tools

- [[winston]]

## References

- Official documentation: https://github.com/trentm/node-bunyan
