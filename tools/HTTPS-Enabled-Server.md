---
url: null
tags:
  - hosting
  - https
type: tool
platforms:
  - Linux
  - Windows
  - Mac
description: Server for hosting payloads over HTTPS
id: aa902bc9-8dba-49c1-ac8a-705d66c80dc0
created_at: '2025-12-11T06:10:22.472Z'
updated_at: '2025-12-11T06:10:22.472Z'
verified: false
validated: true
submitted: true
---
# HTTPS Enabled Server

**Status**: Unverified

## Overview

A server configured with HTTPS to host malicious payloads, such as JavaScript for RCE in Slack exploits.

## Description

Used to serve files securely, bypassing same-origin policies; alternatives include exploiting XSS on files.slack.com.

## Features

- HTTPS support: Secure payload delivery.
- File hosting: Serve HTML/JS files.
- Custom configuration: For specific exploits.

## Installation

### Requirements

- SSL certificate.
- Web server software like Apache or Nginx.

### Install Commands

```bash
sudo apt install nginx
```

## Basic Usage

```bash
nginx -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h` | Show help |
| `-c` | Config file |

## Examples

### Example 1: Basic Usage

```bash
nginx
```

### Example 2: Advanced Usage

```bash
nginx -c /path/to/config
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious outbound connections.
- Hosted malicious content.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/HTTP-Proxy]]

## References

- Nginx documentation
