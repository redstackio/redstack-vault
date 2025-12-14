---
id: tool-burp-suite-collaborator
url: 'https://portswigger.net/burp/documentation/collaborator'
tags:
  - oob
  - ssrf
  - collaborator
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:45.992Z'
validated: true
submitted: true
---
# Burp-Suite-Collaborator

**Status**: Unverified

## Overview

Burp Suite Collaborator is an OOB testing component that generates unique domains to detect external interactions from applications, such as SSRF callbacks via HTTP or DNS.

## Description

Integrated into Burp Suite, it allows testers to embed payloads in requests and monitor for server-side interactions. Useful for blind vulns where direct responses are absent, providing logs of request details for analysis in web security assessments.

## Features

- Feature 1: Unique domain generation per test
- Feature 2: Multi-protocol support (HTTP, DNS, SMTP)
- Feature 3: Detailed interaction logging with headers

## Installation

### Requirements

- Burp Suite Professional or Community

### Install Commands

```bash
# Included in Burp; no separate install
# Launch Burp and access via Collaborator tab
java -jar burpsuite.jar
```

## Basic Usage

In Burp: Collaborator > Copy to clipboard (generates payload).

### Common Options

| Option | Description |
|--------|-------------|
| Poll now | Manual poll for interactions |
| Config | Set server URL |

## Examples

### Example 1: Basic Usage

Generate payload: oast-123.burpcollaborator.net, embed in request, poll for callbacks.

### Example 2: Advanced Usage

Use in Repeater: Insert payload in XML, send, check Collaborator events.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- DNS lookups to burpcollaborator.net subdomains
- HTTP requests to collaborator endpoints
- Correlate with exploit attempts

## Related Procedures


## Related Tools

- [[tools/interactsh]]

## References

- Official documentation: https://portswigger.net/burp/documentation/collaborator
- Related resources: Burp user forum
