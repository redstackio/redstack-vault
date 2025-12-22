---
url: ''
tags:
  - scanning
  - xxe
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Burp extension for upload vulnerabilities
id: 803a65f7-b6a2-41c2-bc70-6f7c78223238
created_at: '2025-12-13T09:00:33.661Z'
updated_at: '2025-12-13T09:00:33.661Z'
verified: false
validated: true
submitted: true
---
# Upload Scanner

**Status**: Unverified

## Overview

Burp Suite extension to scan file uploads for vulnerabilities like XXE.

## Description

Injects payloads into metadata and checks for exploitation.

## Features

- Payload injection
- Automated testing

## Installation

### Requirements

- Burp Suite

### Install Commands

```bash
# Install via Extender tab
```

## Basic Usage

```bash
# Configure in Burp
```

## Examples

### Example 1: Basic Usage

```bash
# Scan upload
```

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

- Scan logs

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

- Burp Extensions
