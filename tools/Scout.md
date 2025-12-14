---
id: tool-uuid-2
url: 'https://github.com/projectdiscovery/scout'
tags:
  - api
  - recon
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.589Z'
validated: true
submitted: true
---
# Scout

**Status**: Unverified

## Overview

Scout is a tool for discovering API endpoints through fuzzing and reconnaissance.

## Description

Specialized for API surface mapping in web apps.

## Features

- Endpoint enumeration
- Silent scanning

## Installation

### Requirements

- Go 1.16+

### Install Commands

```bash
go install -v github.com/projectdiscovery/scout/cmd/scout@latest
```

## Basic Usage

```bash
scout url -s URL
```

### Common Options

| Option | Description |
|--------|-------------|
| -s | Silent |
| url | Target |

## Examples

### Example 1: Basic Usage

```bash
scout url https://api.example.com
```

### Example 2: Advanced Usage

```bash
scout url -s https://api
```

## MITRE ATT&CK Mapping

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

- API probe patterns

## Related Procedures

- [[procedures/Fuzz-API-Endpoints-and-Extract-UUID-for-IDOR]]

## Related Tools

- [[tools/Wfuzz]]

## References

- ProjectDiscovery docs
