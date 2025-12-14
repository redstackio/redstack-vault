---
url: 'https://nodejs.org/'
tags:
  - runtime
  - javascript
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.044Z'
id: 63ae6a35-0524-4224-b4a8-86b01ab6dd01
validated: true
submitted: true
---
# Node.js-Runtime

**Status**: Unverified

## Overview

Node.js is a JavaScript runtime built on Chrome's V8 engine, used to execute server-side code including vulnerable modules like query-mysql for SQL injection demos.

## Description

It enables non-blocking I/O for web apps and modules. In pentesting, it's used to run exploitation scripts against local databases, simulating app vulnerabilities.

## Features

- Feature 1: Event-driven architecture
- Feature 2: Module loading via require()
- Feature 3: REPL for interactive testing

## Installation

### Requirements

- Compatible OS

### Install Commands

```bash
# Download from nodejs.org; for v8.9.3:
# Verify: node -v  # v8.9.3
```

## Basic Usage

```bash
node --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -v, --version | Show version |
| -e | Execute string |
| -i | Interactive REPL |

## Examples

### Example 1: Basic Usage

```bash
node app.js
```

### Example 2: Advanced Usage

```bash
node -e "console.log('Hello')"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- node process
- JavaScript file executions
- Port listening for apps

## Related Procedures

- [[procedures/Demonstrate-Normal-Data-Fetch]]
- [[procedures/Exploit-SQL-Injection-with-Malicious-Input]]

## Related Tools

- [[npm]]
- [[Yarn]]

## References

- Official documentation: https://nodejs.org/en/docs
- Related resources: Node.js security advisories
