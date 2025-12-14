---
id: tool-xssjacking-001
url: 'https://github.com/dxa4481/XSSJacking'
tags:
  - xss-escalation
  - self-xss
  - exploit-kit
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.226Z'
validated: true
submitted: true
---
# XSSJacking

**Status**: Unverified

## Overview

XSSJacking is an exploit kit designed to escalate self-XSS vulnerabilities into more impactful attacks, such as session hijacking or phishing, by leveraging social engineering.

## Description

It provides scripts and templates to chain self-XSS with UI redressing or keylogging. In the context of the Nextcloud self-XSS, it can be used post-exploitation to trick users into executing payloads in their own browsers, though the base vuln remains low severity.

## Features

- Feature 1: Self-XSS to full XSS escalation templates
- Feature 2: Social engineering payload generators
- Feature 3: Integration with browser automation for testing

## Installation

### Requirements

- Git
- Node.js (for some scripts)

### Install Commands

```bash
# Clone repository
git clone https://github.com/dxa4481/XSSJacking.git
cd XSSJacking
npm install  # If applicable
```

## Basic Usage

```bash
node xssjacking.js --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-t, --target` | Specify target URL |

## Examples

### Example 1: Basic Usage

Generate a basic escalation payload:

```bash
node generate-payload.js --type self-xss --output payload.html
```

### Example 2: Advanced Usage

Chain with the Nextcloud vuln:

```bash
node exploit.js --url https://nextcloud.com/about/ --payload alert(205)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[T1566.001]]

### Tactics

- [[Execution]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious JavaScript files hosted externally
- User reports of unexpected browser prompts
- Anomalous DOM manipulations in page source

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/BeEF]]
- [[tools/XSStrike]]

## References

- Official documentation: https://github.com/dxa4481/XSSJacking
- Related resources: XSS escalation guides
