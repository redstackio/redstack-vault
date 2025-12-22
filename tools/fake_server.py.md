---
url: ''
tags:
  - python
  - flask
  - exploit
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: Python script to mimic GitLab import API for injecting malicious URLs.
id: 2847b2d7-cc2f-408a-b919-65eab3931977
created_at: '2025-12-11T03:47:59.477Z'
updated_at: '2025-12-11T03:47:59.477Z'
verified: false
validated: true
submitted: true
---
# fake_server.py

**Status**: Unverified

## Overview

A custom Python script using Flask to fake GitLab API responses, specifically for exploiting repository import vulnerabilities by providing 'file://' URLs.

## Description

The script handles requests to mimic project listing and details, returning crafted JSON with malicious repository URLs. Used in offensive security to demonstrate access control bypasses in GitLab.

## Features

- Mimics GitLab API endpoints
- Injectable repository paths
- Supports development mode for testing

## Installation

### Requirements

- Python 3.x
- Flask library

### Install Commands

```bash
pip install flask
```

## Basic Usage

```bash
FLASK_APP=fake_server.py flask run
```

### Common Options

| Option | Description |
|--------|-------------|
| `--host` | Set host |
| `--port` | Set port |

## Examples

### Example 1: Basic Usage

```bash
FLASK_APP=fake_server.py FLASK_ENV=development flask run
```

### Example 2: Advanced Usage

Edit script and run with custom port.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Information Repositories]]

### Tactics

- [[Initial Access]]
- [[Persistence]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Flask server logs
- Network traffic to fake API endpoints

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Flask]]
- #ngrok

## References

- HackerOne report: https://hackerone.com/reports/1685822
