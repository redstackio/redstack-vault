---
id: i9j0k1l2-m3n4-5678-ijkl-901234567890
name: HexoJS
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.007Z'
platforms:
  - Node.js
tags:
  - blog-generator
  - static-site
url: 'https://hexo.io/'
validated: true
submitted: true
---

# HexoJS

**Status**: Unverified

## Overview

Hexo is a fast, simple, and powerful Node.js static site generator optimized for blogging, serving as the base platform for plugins like hexo-admin where vulnerabilities such as stored XSS can be exploited.

## Description

Hexo uses Markdown for content and templates for layouts, generating static HTML via CLI commands. It's commonly used for personal blogs and integrates plugins for extended functionality, but older versions or misconfigurations can expose injection flaws in admin interfaces.

## Features

- Feature 1: CLI-based generation and serving for local development
- Feature 2: Plugin ecosystem for themes and administration
- Feature 3: Support for Markdown and custom post processing

## Installation

### Requirements

- Node.js 14+
- npm

### Install Commands

```bash
npm install hexo-cli -g
hexo init myblog
cd myblog && npm install
```

## Basic Usage

```bash
hexo --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --version` | Display version info |

## Examples

### Example 1: Basic Usage

```bash
hexo generate
```

### Example 2: Advanced Usage

```bash
hexo server -d
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Node.js processes running hexo CLI
- Local port 4000 listening
- public/ directory with generated HTML

## Related Procedures


## Related Tools

- [[tools/Hexo-Admin]]

## References

- Official documentation: https://hexo.io/docs/
- GitHub: https://github.com/hexojs/hexo
