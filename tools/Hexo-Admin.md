---
id: j0k1l2m3-n4o5-6789-jklm-012345678901
name: Hexo-Admin
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.002Z'
platforms:
  - Web
  - Node.js
tags:
  - admin-ui
  - plugin
  - xss-vulnerable
url: 'https://github.com/jaredly/hexo-admin'
validated: true
submitted: true
---

# Hexo-Admin

**Status**: Unverified

## Overview

Hexo-Admin is a plugin providing a web-based administrative interface for Hexo blogs, allowing post creation and editing, but version 3.9.0 contains a stored XSS vulnerability in the post content field due to missing sanitization.

## Description

The plugin adds a /admin route with login, enabling CRUD operations on posts via a browser UI. It renders content directly without escaping, allowing stored XSS payloads to execute in the editor and persist in generated pages, affecting users viewing posts.

## Features

- Feature 1: Dashboard for posts, pages, and settings management
- Feature 2: Inline editing with preview for content
- Feature 3: Basic authentication support

## Installation

### Requirements

- Hexo project setup
- Node.js

### Install Commands

```bash
npm install hexo-admin@3.9.0 --save
```

## Basic Usage

```bash
hexo server -d
```
Access at http://localhost:4000/admin

### Common Options

| Option | Description |
|--------|-------------|
| No CLI options; configured via _config.yml | Username/password setup |

## Examples

### Example 1: Basic Usage

Install and start server to access UI.

### Example 2: Advanced Usage

Configure in _config.yml for custom auth.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- /admin route active on Hexo server
- npm dependencies include hexo-admin
- Logs showing post saves with script content

## Related Procedures


## Related Tools

- [[tools/HexoJS]]

## References

- GitHub repository
- HackerOne report: https://hackerone.com/reports/716570
