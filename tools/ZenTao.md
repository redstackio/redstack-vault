---
id: 123e4567-e89b-12d3-a456-426614174011
name: ZenTao
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.856Z'
platforms:
  - Web
tags:
  - issue-tracker
  - integration
url: 'https://docs.gitlab.com/ee/user/project/integrations/zentao.html'
validated: true
submitted: true
---

# ZenTao

**Status**: Unverified

## Overview

ZenTao is an open-source issue tracking system integrated with GitLab, whose API responses can be exploited for XSS by serving unvalidated data like javascript: URLs and HTML injections.

## Description

In the attack, a mock ZenTao server is set up to respond to GitLab's fetches, delivering payloads that bypass validation in the Ruby serializer, leading to execution on the issue details page.

## Features

- Feature 1: API for issues (/api.php/v1/issues)
- Feature 2: JSON responses for id, url fields
- Feature 3: Integration with DevOps tools like GitLab

## Installation

### Requirements

- PHP and MySQL for full setup (mock uses static files)

### Install Commands

```bash
# For mock, no full install; use Apache static serving
sudo apt install php-mysql
# Download and configure if full
```

## Basic Usage

```bash
# API endpoint example
curl https://zentao.example.com/api.php/v1/issues/story-1
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | API is REST-like |

## Examples

### Example 1: Basic Usage

Respond to GitLab integration fetches with JSON.

### Example 2: Advanced Usage

Mock payload: {"id": "<img src=x onerror=alert(1)>", "web_url": "javascript:alert('XSS')"}

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Tactics

- [[Execution]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unexpected JSON responses with HTML tags
- Integration calls to mock domains
- Breadcrumb anomalies in GitLab UI

## Related Procedures


## Related Tools

- [[tools/GitLab]]
- [[tools/Apache]]

## References

- GitLab integration docs: https://docs.gitlab.com/ee/user/project/integrations/zentao.html
- ZenTao API: Official ZenTao documentation
