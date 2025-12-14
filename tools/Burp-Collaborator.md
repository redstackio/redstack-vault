---
id: tool-2
url: ''
tags:
  - outbound-detection
  - ssrf-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.948Z'
validated: true
submitted: true
---
# Burp-Collaborator

**Status**: Unverified

## Overview

Burp Collaborator is a server-side component of Burp Suite that detects out-of-band interactions, such as DNS resolutions or HTTP requests, to confirm vulnerabilities like SSRF.

## Description

It generates unique domains for payloads; when a server interacts with them (e.g., via SSRF), Collaborator logs the activity. Used here to confirm Nextcloud's outbound connections to external hosts.

## Features

- Feature 1: DNS and HTTP interaction polling
- Feature 2: Unique domain generation
- Feature 3: Integration with Burp payloads

## Installation

### Requirements

- Burp Suite Professional
- Network access for polling

### Install Commands

```bash
# Included in Burp Suite; access via Burp menu: Burp > Burp Collaborator client
```

## Basic Usage

```bash
# In Burp, generate Collaborator payload and poll
# No CLI; GUI-based
```

### Common Options

| Option | Description |
|--------|-------------|
| Poll Now | Manual poll for interactions |
| Copy to Clipboard | Get domain for payload |

## Examples

### Example 1: Basic Usage

Generate domain, insert into imapHost, send request, poll for DNS hit.

### Example 2: Advanced Usage

Monitor TCP connections on custom ports.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Queries to collaborator.burp.net domains
- Unusual DNS lookups from application servers

## Related Procedures

- [[procedures/Confirm-SSRF-with-External-Server]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Burp Documentation: https://portswigger.net/burp/documentation/desktop/collaborator
