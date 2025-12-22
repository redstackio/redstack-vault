---
url: 'https://mermaid-js.github.io/mermaid/'
tags:
  - diagram
  - xss
type: tool
platforms:
  - Web
description: >-
  JavaScript library for generating diagrams from text, integrated in GitLab for
  rendering charts in issues.
id: f120ba85-9c9b-4e0c-ae5e-86818ff3a515
created_at: '2025-12-13T23:52:24.561Z'
updated_at: '2025-12-13T23:52:24.561Z'
verified: false
validated: true
submitted: true
---
# Mermaid

**Status**: Unverified

## Overview

Mermaid is a diagramming tool that parses text to create flowcharts, sequence diagrams, etc., commonly used in Markdown for documentation. In security testing, it's exploited for injection vulnerabilities due to unsanitized config handling.

## Description

The library supports directives like `%%{init: {...}}%%` for theming, merging user JSON into CSS via Stylis without validation, enabling DOM XSS in integrations like GitLab.

## Features

- Feature 1: Text-to-diagram rendering
- Feature 2: Custom config directives for themes
- Feature 3: innerHTML insertion for styles

## Installation

### Requirements

- Node.js for standalone use

### Install Commands

```bash
npm install mermaid
```

## Basic Usage

```bash
mermaid --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --version` | Show version |

## Examples

### Example 1: Basic Usage

```javascript
import mermaid from 'mermaid';
mermaid.initialize({});
mermaid.render('diagram', 'graph TD; A-->B');
```

### Example 2: Advanced Usage

```javascript
mermaid.initialize({ fontFamily: 'Arial' });
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for anomalous directive payloads in logs
- Scan rendered HTML for injection artifacts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Stylis]]

## References

- Official documentation
