---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
url: 'https://designer.mocky.io/design'
tags:
  - mock-server
  - http-testing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:36.250Z'
validated: true
submitted: true
---
# mocky-io

**Status**: Unverified

## Overview

Mocky.io is a web-based tool for generating custom HTTP mock responses, ideal for testing API behaviors, proxy configurations, and header injections in security assessments without needing a local server.

## Description

It allows quick creation of mock endpoints with customizable status codes, bodies, and headers, commonly used in offensive security to simulate malicious backends, such as injecting X-Accel-Redirect for NGINX testing. Supports JSON, XML, and plain text responses; no installation required.

## Features

- Feature 1: Custom HTTP headers, bodies, and status codes
- Feature 2: Instant URL generation for mock endpoints
- Feature 3: Response preview and sharing via unique URLs

## Installation

### Requirements

- Web browser
- Internet connection

### Install Commands

No installation needed; access via browser.

## Basic Usage

Visit https://designer.mocky.io/design to build mocks.

### Common Options

| Option | Description |
|--------|-------------|
| HTTP Headers | Add custom headers like X-Accel-Redirect |
| Body | Set response content |
| Generate | Create unique mock URL |

## Examples

### Example 1: Basic Usage

Design a 200 OK with empty body and generate URL.

### Example 2: Advanced Usage

Set Headers: {"X-Accel-Redirect": "/collections/all"}, Body: "Redirected", Status: 200, then generate.

```bash
# Test the generated URL
curl -I https://run.mocky.io/v3/[uuid]
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Traffic to mocky.io domains from testing environments
- Unusual mock responses in proxy logs

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official site: https://www.mocky.io/
- Documentation: https://designer.mocky.io/
