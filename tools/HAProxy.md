---
url: null
tags:
  - proxy
  - haproxy
type: tool
platforms:
  - Web
  - Linux
description: High-performance proxy server used for load balancing and access control.
id: c8e482d1-bad6-4787-ad0e-e0b04a482067
created_at: '2025-12-13T09:01:22.195Z'
updated_at: '2025-12-13T09:01:22.195Z'
verified: false
validated: true
submitted: true
---
# HAProxy

**Status**: Unverified

## Overview

HAProxy is a free, open-source load balancer and proxy server commonly used in security testing to simulate restricted environments and demonstrate bypass techniques.

## Description

Provides high availability, load balancing, and proxying for TCP and HTTP-based applications. In this context, used to restrict URIs via ACLs.

## Features

- ACL-based access control
- HTTP mode for request inspection
- Backend forwarding

## Installation

### Requirements

- Linux environment
- Version 1.5.3 or compatible

### Install Commands

```bash
sudo apt install haproxy
```

## Basic Usage

```bash
haproxy -f config.cfg
```

### Common Options

| Option | Description |
|--------|-------------|
| `-f` | Configuration file |
| `-D` | Daemon mode |

## Examples

### Example 1: Basic Usage

```bash
haproxy -f haproxy.cfg
```

### Example 2: Advanced Usage

Configure with ACL: acl forbidden path_beg /flag http-request deny if forbidden

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Defense Evasion]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor proxy logs for denied requests
- Anomalous traffic patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/WEBrick]]

## References

- Official HAProxy documentation
