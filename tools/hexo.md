---
url: 'https://hexo.io'
tags:
  - blog-generator
  - static-site
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.693Z'
id: 6ea8a9b1-00ba-4189-b1eb-9a46be472a26
validated: true
submitted: true
---
# hexo

**Status**: Unverified

## Overview

Hexo is a fast, simple, and powerful Node.js-based static site generator CLI tool used for creating blogs and websites from Markdown sources.

## Description

Hexo supports themes, plugins, and commands for site generation, serving, and deployment. In security contexts, it's used to build vulnerable sites for testing, like those with admin plugins prone to XSS.

## Features

- Feature 1: Markdown to HTML conversion with templating
- Feature 2: Plugin ecosystem for extensions like admin UIs
- Feature 3: Local server for previewing changes

## Installation

### Requirements

- Node.js >= 10
- npm

### Install Commands

```bash
npm install hexo-cli -g
hexo init site-name
cd site-name
npm install
```

## Basic Usage

```bash
hexo --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v, --version` | Show version number |
| `generate` | Generate static files |

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

- Presence of Hexo CLI in PATH
- .hexo directory or node_modules/hexo

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/hexo-admin]]

## References

- Official documentation: https://hexo.io/docs/
