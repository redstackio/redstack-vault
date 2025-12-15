---
url: 'https://github.com/jaredly/hexo-admin'
tags:
  - admin-ui
  - plugin
type: tool
verified: false
platforms:
  - Web
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.691Z'
configuration: Version 3.9.0
id: 369d6e5d-882e-4e68-970a-374f318067d5
validated: true
submitted: true
---
# hexo-admin

**Status**: Unverified

## Overview

Hexo-admin is a plugin providing a web-based administrative interface for Hexo blogs, allowing post creation and editing via a browser.

## Description

It offers a simple UI for managing content without CLI, but version 3.9.0 has a stored XSS flaw in the post editor due to unsanitized inputs. Used in pentesting to demonstrate web vuln exploitation.

## Features

- Feature 1: Browser-based post editor
- Feature 2: Live preview of content
- Feature 3: Integration with Hexo themes

## Installation

### Requirements

- Installed Hexo site

### Install Commands

```bash
npm install hexo-admin --save
```

Add to _config.yml: admin: { }

## Basic Usage

```bash
hexo server -d
```
Access at /admin.

### Common Options

| Option | Description |
|--------|-------------|
No CLI options; UI-driven.

## Examples

### Example 1: Basic Usage

Start server and visit http://localhost:4000/admin.

### Example 2: Advanced Usage

Create post via UI, inject payloads in content.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- /admin endpoint exposed
- node_modules/hexo-admin directory

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/hexo]]

## References

- GitHub repo: https://github.com/jaredly/hexo-admin
