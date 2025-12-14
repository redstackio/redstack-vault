---
url: 'http://sec101.sourceforge.net/referer-xss/'
tags:
  - xss
  - poc
  - referer
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.006Z'
id: b6ece934-6099-4c80-9fea-3bc955eb6c4a
validated: true
submitted: true
---
# sec101-referer-xss-poc

**Status**: Unverified

## Overview

A proof-of-concept web tool for demonstrating Referer-based XSS vulnerabilities by generating and testing malicious Referer headers against target URLs.

## Description

This online POC allows users to input a target URL and script payload, generating a full malicious Referer that can be used in requests. It's designed for educational purposes in security testing, specifically for apps like ownCloud where Referer is reflected unsafely. Common use: Crafting payloads for attribute injection in onclick or similar contexts.

## Features

- Feature 1: Payload generator for Referer XSS
- Feature 2: Direct testing against provided URLs
- Feature 3: Encoded output for various injection points

## Installation

### Requirements

- Web browser
- No local install needed; web-based

### Install Commands

```bash
# No installation; access via URL
```

## Basic Usage

```bash
tool-name --help
```

Visit http://sec101.sourceforge.net/referer-xss/ and input parameters.

### Common Options

| Option | Description |
|--------|-------------|
| s | Script payload |
| u | Target URL |

## Examples

### Example 1: Basic Usage

Input s=""><img src=1 onerror=alert(1)> and u=https://apps.owncloud.com/messages/?action=newmessage&username=anderslund to generate POC Referer.

### Example 2: Advanced Usage

Use for complex payloads: s=alert(document.domain+String.fromCharCode(58,10,10,82,101,102,101,114,101,114,45,98,97,115,101,100,32,88,83,83,32,80,114,111,111,102,45,111,102,45,67,111,110,99,101,112,116,33))

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Traffic to sourceforge.net/referer-xss from testing environments
- Generated Referer patterns in logs

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
- [[curl]]

## References

- Official: http://sec101.sourceforge.net/referer-xss/
- HackerOne Report: https://hackerone.com/reports/83374
