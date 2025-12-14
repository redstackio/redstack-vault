---
id: tool-metascraper
url: 'https://www.npmjs.com/package/metascraper'
tags:
  - scraper
  - xss-vulnerable
type: tool
verified: false
platforms:
  - Node.js
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.476Z'
validated: true
submitted: true
---
# metascraper

**Status**: Unverified

## Overview

Metascraper is a Node.js library for extracting Open Graph and HTML meta metadata from web pages; vulnerable to stored XSS due to lack of sanitization on extracted values.

## Description

It parses HTML to pull properties like og:site_name without escaping, allowing injected scripts to propagate. Used in attacks to chain malicious sites with rendering apps.

## Features

- Feature 1: Supports Open Graph, Twitter Cards
- Feature 2: Modular rules for custom extraction
- Feature 3: Async promise-based API

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm install metascraper
```

## Basic Usage

```bash
const metascraper = require('metascraper')();
metascraper({ html, url }).then(metadata => console.log(metadata));
```

### Common Options

| Option | Description |
|--------|-------------|
| rules | Custom extraction rules |
| html | Input HTML string |
| url | Source URL |

## Examples

### Example 1: Basic Usage

```bash
# In script
await metascraper({ html: '<meta property="og:title" content="Test">', url: 'http://example.com' });
```

### Example 2: Advanced Usage

```bash
# With custom rules
metascraper([rule1, rule2], { html, url });
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript (via XSS)

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Import of 'metascraper' in code
- Scraping requests in logs
- Unsanitized metadata in outputs

## Related Procedures


## Related Tools

- [[tools/got]]

## References

- https://www.npmjs.com/package/metascraper
