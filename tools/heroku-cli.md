---
id: t2j3k4l5-m6n7-8903-jklm-0123456789
url: 'https://devcenter.heroku.com/articles/heroku-cli'
tags:
  - cloud
  - deployment
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:51:10.609Z'
validated: true
submitted: true
---
# Heroku-CLI

**Status**: Unverified

## Overview

Heroku CLI is the official command-line tool for interacting with Heroku cloud platform, used for deploying apps and managing resources.

## Description

In offensive security, it's used to deploy content to taken-over Heroku apps linked to dangling DNS records. Supports Git-based deployments and app configuration.

## Features

- Feature 1: Git integration for pushes
- Feature 2: App management (scale, logs)
- Feature 3: Plugin ecosystem

## Installation

### Requirements

- Node.js or direct installer

### Install Commands

```bash
# Linux/macOS
curl https://cli-assets.heroku.com/install.sh | sh
```

## Basic Usage

```bash
heroku --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `login` | Authenticate |
| `git:remote` | Add Git remote |
| `ps:scale` | Scale dynos |

## Examples

### Example 1: Basic Usage

```bash
heroku create app-name
```

### Example 2: Advanced Usage

```bash
heroku git:remote -a app-name
git push heroku main
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- CLI authentication to Heroku from suspicious IPs
- New app creations matching domain names

## Related Procedures

- [[procedures/Host-Arbitrary-Content-on-Taken-Over-Subdomain]]

## Related Tools

- [[Git]]

## References

- Heroku Dev Center
