---
id: tool-uuid-2
url: 'https://www.npmjs.com/package/public'
tags:
  - web-server
  - static-hosting
  - vulnerable
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.865Z'
description: Vulnerable static file hosting server for Node.js with directory indexing
validated: true
submitted: true
---
# public-module

**Status**: Unverified

## Overview

The 'public' module is a lightweight Node.js static file server that supports directory listings, vulnerable to stored XSS in version 0.1.3 due to unsanitized filename output.

## Description

It serves files and generates HTML indexes like Apache. Used in testing for XSS exploits via filenames. Features include port binding and dir serving; vuln at bin/public line 106.

## Features

- Feature 1: Directory indexing for file browsing
- Feature 2: Simple CLI binary for quick serving
- Feature 3: Supports custom ports and paths

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install public@0.1.3
```

## Basic Usage

```bash
./node_modules/public/bin/public
```

### Common Options

| Option | Description |
|--------|-------------|
| <dir> | Directory to serve | 
| <port> | Port to bind | 

## Examples

### Example 1: Basic Usage

```bash
./node_modules/public/bin/public ./ 8000
```

### Example 2: Advanced Usage

```bash
./node_modules/public/bin/public /var/www 8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Port listening on non-standard ports like 8000
- Process named 'public' or node with public.js
- HTML responses with unsanitized <li><a> tags

## Related Procedures

- [[procedures/Run-Public-Server]]

## Related Tools

- [[tools/npm]]

## References

- Official documentation: https://www.npmjs.com/package/public
- Related resources: HackerOne report #316346
