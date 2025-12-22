---
url: 'https://www.npmjs.com/package/atlasboard'
tags:
  - dashboard
  - framework
type: tool
verified: false
platforms:
  - Node.js
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.319Z'
id: 000b9685-3f94-4848-ae1f-3980749b4c19
validated: true
submitted: true
---
# atlasboard

**Status**: Unverified

## Overview

Atlasboard is a Node.js framework for creating customizable dashboards that integrate with tools like JIRA, providing widgets for data visualization in security testing and monitoring.

## Description

It allows CLI-based project creation, configuration of widgets, and server hosting for real-time dashboards. In this context, it's used to demonstrate XSS in integrated packages. Supports JSON configs for data sources and custom widgets.

## Features

- Feature 1: CLI for scaffolding and starting dashboards
- Feature 2: Modular widget system for integrations like JIRA
- Feature 3: Local server hosting with configurable ports

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install -g atlasboard
```

## Basic Usage

```bash
atlasboard --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `new` | Create new project |
| `start` | Launch server |
| `--port` | Specify port |

## Examples

### Example 1: Basic Usage

```bash
atlasboard new mydashboard
```

### Example 2: Advanced Usage

```bash
atlasboard start --port 8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process 'atlasboard' or 'node start.js' running on port 3000
- Localhost traffic to /example1 endpoints
- npm global package logs

## Related Procedures

- [[procedures/Setup-Atlasboard-Environment]]
- [[procedures/Launch-Dashboard-and-Trigger-XSS]]

## Related Tools

- [[tools/npm]]
- [[tools/node]]

## References

- Official documentation: https://www.npmjs.com/package/atlasboard
