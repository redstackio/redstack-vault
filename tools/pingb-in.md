---
url: 'http://pingb.in'
tags:
  - oob
  - ssrf-testing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.181Z'
id: 6c9b873a-e3e1-494c-ac4a-8de0a1cd901e
validated: true
submitted: true
---
# pingb-in

**Status**: Unverified

## Overview

pingb.in is a simple online service for detecting external interactions via HTTP requests, serving as a lightweight alternative to Burp Collaborator for confirming SSRF by providing unique URLs that log incoming pings or fetches.

## Description

Users generate a unique URL on the site, inject it into the target, and monitor the dashboard for hits. It's ideal for quick tests without installing software, focusing on HTTP-based OOB detection for web vulnerabilities.

## Features

- Feature 1: Instant URL generation for HTTP interaction tracking
- Feature 2: Web-based dashboard for real-time request logging
- Feature 3: No setup required; browser-only access

## Installation

### Requirements

- Web browser
- Internet access

### Install Commands

No installation; access via browser.

```bash
# N/A - Web service
```

## Basic Usage

Visit http://pingb.in, generate URL, inject, and check dashboard.

### Common Options

| Option | Description |
|--------|-------------|
| Generate | Create new unique URL |
| View Logs | Display incoming requests |

## Examples

### Example 1: Basic Usage

Go to http://pingb.in, copy URL like http://x.y.pingb.in, inject into chatbox, refresh dashboard for hits.

### Example 2: Advanced Usage

Use in combination with custom headers for deeper SSRF analysis.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Requests to pingb.in subdomains from servers
- Log patterns matching the service's URL structure

## Related Procedures


## Related Tools

- [[tools/Burp-Collaborator]]

## References

- Official site: http://pingb.in
- Related resources: Security testing blogs on OOB techniques
