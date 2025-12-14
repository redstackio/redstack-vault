---
id: tool-uuid-3
url: 'https://www.npmjs.com/package/commit-msg'
tags:
  - git-hook
  - vulnerable
type: tool
verified: false
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.244Z'
validated: true
submitted: true
---
# commit-msg

**Status**: Unverified

## Overview

commit-msg is a Node.js module for parsing and validating Git commit messages, vulnerable to RCE in v0.2.3 due to insecure shell command formatting.

## Description

Used as a Git hook, it processes stdin inputs. Exploitation involves injecting payloads that break out of the command string.

## Features

- Feature 1: Commit message validation
- Feature 2: Stdin processing
- Feature 3: Shell-based execution (vulnerable)

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm i commit-msg@0.2.3 -g
```

## Basic Usage

```bash
commit-msg stdin
```

### Common Options

| Option | Description |
|--------|-------------|
| `stdin` | Read from standard input |
| `--help` | Show usage |

## Examples

### Example 1: Basic Usage

```bash
echo "message" | commit-msg stdin
```

### Example 2: Advanced Usage

```bash
echo "malicious||command" | commit-msg stdin
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

- Check for v0.2.3 in node_modules
- Monitor invocations with suspicious inputs

## Related Procedures

- [[procedures/Exploit-RCE-with-Malicious-Commit-Input]]

## Related Tools

- [[tools/npm]]

## References

- HackerOne Report: https://hackerone.com/reports/885031
