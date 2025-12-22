---
id: tool-uuid-1
url: 'https://gitlab.com'
tags:
  - devops
  - version-control
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.851Z'
validated: true
submitted: true
---
# GitLab

**Status**: Unverified

## Overview

GitLab is a web-based DevOps lifecycle tool providing project management, version control, and CI/CD features, commonly used for exploiting import/export vulnerabilities like persistent XSS in Note objects.

## Description

GitLab's project export/import functionality serializes data into JSON, including Note objects in merge requests. This can be manipulated to inject XSS payloads, bypassing cache logic in Ruby on Rails backend.

## Features

- Feature 1: Project export to tar.gz with JSON metadata
- Feature 2: Import processing with cache invalidation via CacheMarkdownField
- Feature 3: Merge request discussions rendering HTML notes

## Installation

### Requirements

- Web browser for UI access
- Account on GitLab.com or self-hosted instance

### Install Commands

No installation needed for cloud; for self-hosted:

```bash
# Follow official docs for Docker or Omnibus
```

## Basic Usage

```bash
# Access via browser: https://gitlab.com
```

### Common Options

| Option | Description |
|--------|-------------|
| Export Project | Download project data |
| Import Project | Upload and process export |

## Examples

### Example 1: Basic Usage

Log in and export a project from UI.

### Example 2: Advanced Usage

Create MR, add discussion, export, modify JSON, import.

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

- Audit logs for frequent exports/imports
- Monitor JSON payloads for malicious content

## Related Procedures


## Related Tools

- [[tools/Web-Browser]]

## References

- Official documentation: https://docs.gitlab.com
- HackerOne Report: https://hackerone.com/reports/508184
