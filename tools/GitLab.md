---
url: 'https://gitlab.com'
tags:
  - devops
  - ssrf
type: tool
platforms:
  - Linux
  - Ubuntu 18.04
  - Web
description: >-
  Platform for project management, vulnerable to SSRF in project import
  features.
id: fa827fee-ad76-4908-8914-535134b043d2
created_at: '2025-12-11T03:47:39.451Z'
updated_at: '2025-12-11T03:47:39.451Z'
verified: false
validated: true
submitted: true
---
# GitLab

**Status**: Unverified

## Overview

GitLab is a web-based DevOps platform for version control and CI/CD, with vulnerabilities in project import allowing SSRF via unsanitized parameters.

## Description

Running on Ubuntu 18.04 with components like Ruby 2.6.5, Redis 5.0.7, it exposes internal services when exploited, leading to data exfiltration or RCE.

## Features

- Project management: Create, export, import projects.
- Issue tracking: With notes and attachments.
- Integration: With services like Prometheus and Redis.

## Installation

### Requirements

- Ubuntu 18.04 or compatible Linux.
- Omnibus installer.

### Install Commands

```bash
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash
sudo apt-get install gitlab-ee
```

## Basic Usage

```bash
# Web UI usage primarily
```

### Common Options

| Option | Description |
|--------|-------------|
| `--version` | Check GitLab version |
| `--help` | Show help |

## Examples

### Example 1: Basic Usage

Access via web: https://gitlab-instance/

### Example 2: Advanced Usage

Export project via API or UI.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Service Scanning]]

### Tactics

- [[Initial Access]]
- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor project import logs for suspicious URLs.
- Detect anomalous internal network traffic from GitLab.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/CarrierWave]]

## References

- https://gitlab.com
