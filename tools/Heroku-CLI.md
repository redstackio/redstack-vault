---
id: k1l2m3n4-o5p6-7890-klmn-123456789012
url: 'https://devcenter.heroku.com/articles/heroku-cli'
name: Heroku-CLI
tags:
  - cloud
  - deployment
  - heroku
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:18.208Z'
validated: true
submitted: true
---
# Heroku-CLI

**Status**: Unverified

## Overview

Heroku CLI is the official command-line interface for managing Heroku Platform as a Service (PaaS) applications, enabling creation, deployment, and scaling of apps in the cloud.

## Description

In security contexts, it's used to claim and deploy to dangling app names for subdomain takeovers. It handles authentication, Git-based deployments, and configuration, making it essential for cloud exploitation scenarios.

## Features

- Feature 1: App creation and management
- Feature 2: Git integration for deployments
- Feature 3: Plugin support for extended functionality

## Installation

### Requirements

- Node.js or direct binary download

### Install Commands

```bash
# For macOS/Linux
curl https://cli-assets.heroku.com/install.sh | sh
# For Windows: Download from heroku.com
```

## Basic Usage

```bash
heroku --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --version` | Display version |
| `--app` | Target specific app |

## Examples

### Example 1: Basic Usage

```bash
heroku create myapp
```

### Example 2: Advanced Usage

```bash
heroku apps:info --app myapp
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Heroku API logs showing unauthorized app creations
- Detection method 2: CLI authentication attempts in auth logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/AWS-CLI]]
- [[tools/Terraform]]

## References

- Official documentation: https://devcenter.heroku.com/articles/heroku-cli
- Related resources: Heroku Dev Center
