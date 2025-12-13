---
url: 'http://wallarm.tools'
tags:
  - scanner
  - ssrf
  - oob
type: tool
platforms:
  - Web
  - Linux
description: >-
  A scanning tool used to host test endpoints for detecting out-of-band requests
  in vulnerabilities like SSRF.
id: a04568b7-67bf-4dcc-a7d0-a70cd6e6cb46
created_at: '2025-12-13T09:00:27.175Z'
updated_at: '2025-12-13T09:00:27.175Z'
verified: false
validated: true
submitted: true
---
# Wallarm Scanner

**Status**: Unverified

## Overview

Wallarm Scanner is a security tool designed for vulnerability scanning, particularly useful for hosting endpoints to detect out-of-band interactions in attacks like SSRF or XXE.

## Description

It provides hosted URLs (e.g., http://wallarm.tools/ok) that log incoming requests, allowing attackers or testers to confirm server-side behaviors without in-band responses. Commonly used in offensive security for proof-of-concept demonstrations.

## Features

- Feature 1: Hosted test endpoints for OOB detection
- Feature 2: Access log monitoring for request verification
- Feature 3: Integration with scanning workflows

## Installation

### Requirements

- Web access
- No local install needed (cloud-hosted)

### Install Commands

```bash
# No installation required; access via URL
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
# Use URL in payload: http://wallarm.tools/ok
```

### Example 2: Advanced Usage

Monitor logs after triggering a payload.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for requests to wallarm.tools domains
- Detection method 2: Log unexpected outbound HTTP traffic

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
- [[ZAP]]

## References

- Official documentation: http://wallarm.tools
