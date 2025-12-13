---
url: null
tags:
  - hosting
  - oob
  - xxe
type: tool
platforms:
  - Linux
  - Windows
description: >-
  Generic web server for hosting files like external DTDs in out-of-band
  attacks.
id: c9ddc5d2-5eed-44a2-b02f-b3fe6af34a9c
created_at: '2025-12-13T09:00:28.018Z'
updated_at: '2025-12-13T09:00:28.018Z'
verified: false
validated: true
submitted: true
---
# Web Server

**Status**: Unverified

## Overview

A web server (e.g., Apache, Nginx) used to host external files such as DTDs for receiving out-of-band requests in vulnerabilities like XXE.

## Description

In offensive security, web servers host payloads to confirm exploitation by logging incoming requests from vulnerable targets.

## Features

- Feature 1: File hosting over HTTP
- Feature 2: Access logging
- Feature 3: Custom configuration for ports/IPs

## Installation

### Requirements

- OS with package manager
- Network access

### Install Commands

```bash
sudo apt install apache2  # For Apache
```

## Basic Usage

```bash
apache2ctl start
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h` | Help |
| `-v` | Version |

## Examples

### Example 1: Basic Usage

```bash
# Host files in /var/www/html
```

### Example 2: Advanced Usage

```bash
# Configure virtual host for specific IP
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for new server instances
- Detection method 2: Log analysis for hosted files

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]]

## References

- Apache documentation
