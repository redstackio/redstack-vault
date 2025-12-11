---
id: ac3f59d5-9ef2-404a-8e3d-6e0b71178a38
name: GitLab
type: tool
verified: false
created_at: '2025-12-11T06:10:28.467Z'
updated_at: '2025-12-11T06:10:28.467Z'
platforms:
  - Web
  - Linux
tags:
  - devops
  - version-control
  - wiki
url: 'https://gitlab.com'
description: Web-based DevOps platform where the vulnerability exists in Wiki feature.
validated: true
submitted: true
---

# GitLab

**Status**: Unverified

## Overview

GitLab is a web-based platform for version control, CI/CD, and collaboration, with features like wikis that can be vulnerable to attacks like XSS.

## Description

Enterprise Edition 11.9.4-ee was used in this vulnerability demonstration, running on services like PostgreSQL and Redis.

## Features

- Feature 1: Wiki for documentation
- Feature 2: Project management
- Feature 3: Integration with tools like [[tools/Docker]]

## Installation

### Requirements

- Linux server
- Docker or direct install

### Install Commands

```bash
# Use official Docker image: docker run gitlab/gitlab-ee:11.9.4-ee
```

## Basic Usage

Access via web interface at the hosted URL.

### Common Options

N/A (web-based)

## Examples

### Example 1: Basic Usage

Navigate to project wiki.

### Example 2: Advanced Usage

Create wiki page with Markdown.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor wiki edit logs
- Scan for vulnerable versions

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[GitHub]]
- [[Bitbucket]]

## References

- https://about.gitlab.com
