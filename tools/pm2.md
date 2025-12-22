---
id: uuid-pm2-tool
url: 'https://www.npmjs.com/package/pm2'
tags:
  - process-manager
  - vulnerable
type: tool
verified: false
platforms:
  - Node.js
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.527Z'
configuration: Version 3.5.1
validated: true
submitted: true
---
# pm2

**Status**: Unverified

## Overview

PM2 is a production process manager for Node.js applications, handling clustering, logging, and monitoring. Version 3.5.1 is vulnerable to command injection in pm2.install(), making it a target for RCE exploits in security assessments.

## Description

PM2 daemonizes Node apps, supports ecosystem files, and provides API for programmatic control. In offensive security, its modular installation feature (local/remote tar.gz) exposes sinks for injection via spawn with shell:true. Features include zero-downtime reloads and resource monitoring.

## Features

- Feature 1: Process clustering and load balancing
- Feature 2: API for scripting (e.g., pm2.connect())
- Feature 3: Module installation from URLs or files

## Installation

### Requirements

- Node.js 10+

### Install Commands

```bash
npm i pm2@3.5.1
```

## Basic Usage

```bash
pm2 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `start` | Start PM2 daemon or app |
| `install` | Install modules (vulnerable) |
| `stop` | Stop processes |

## Examples

### Example 1: Basic Usage

```bash
pm2 start app.js
```

### Example 2: Advanced Usage

```bash
pm2 install "malicious.tar.gz;id"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- PM2 daemon process (pm2-daemon)
- Logs in ~/.pm2/logs
- Anomalous spawn calls to tar/wget

## Related Procedures

- [[procedures/Exploit-PM2-CLI-Command-Injection]]

## Related Tools

- [[tools/npm]]
- [[tools/node]]

## References

- Official documentation: https://pm2.keymetrics.io/docs
- HackerOne report: https://hackerone.com/reports/630227
