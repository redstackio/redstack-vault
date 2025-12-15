---
id: tool-uuid-3
url: 'https://www.npmjs.com/package/hekto'
tags:
  - server
  - vulnerable
type: tool
verified: false
platforms:
  - Node.js
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:27.060Z'
configuration: Version 0.2.3
validated: true
submitted: true
---
# hekto

**Status**: Unverified

## Overview

hekto is a Node.js module for exposing directories via HTTP for CRUD operations; version 0.2.3 contains an open redirect vulnerability exploited in phishing setups.

## Description

Provides a simple HTTP server for file management. The vulnerability in bin/hekto.js (line ~184) mishandles paths with double slashes, leading to unvalidated redirects. Used in testing to reproduce the issue locally.

## Features

- Feature 1: HTTP serving of directories
- Feature 2: Basic CRUD endpoints
- Feature 3: Redirect logic (vulnerable)

## Installation

### Requirements

- Node.js
- npm

### Install Commands

```bash
npm install hekto
```

## Basic Usage

```bash
./node_modules/hekto/bin/hekto.js serve
```

### Common Options

| Option | Description |
|--------|-------------|
| serve | Start server |
| --port | Specify port |

## Examples

### Example 1: Basic Usage

```bash
./node_modules/hekto/bin/hekto.js serve
```

### Example 2: Advanced Usage

```bash
./node_modules/hekto/bin/hekto.js serve --port 8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Phishing]] Phishing

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Process listening on non-standard ports
- Requests to local HTTP servers
- Redirect logs showing protocol-relative URLs

## Related Procedures

- [[procedures/Start-Hekto-Server]]

## Related Tools

- [[http-server]]
- [[live-server]]

## References

- npm page: https://www.npmjs.com/package/hekto
- HackerOne report: https://hackerone.com/reports/320693
