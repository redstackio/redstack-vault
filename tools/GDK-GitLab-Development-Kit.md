---
id: tool-gdk
url: 'https://gitlab.com/gitlab-org/gitlab-development-kit'
tags:
  - development
  - gitlab
  - testing
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.765Z'
validated: true
submitted: true
---
# GDK-GitLab-Development-Kit

**Status**: Unverified

## Overview

GDK (GitLab Development Kit) is a local development environment for GitLab, allowing safe testing of vulnerabilities like XSS without impacting production instances such as gitlab.com.

## Description

GDK bundles GitLab CE/EE with dependencies like Ruby on Rails, PostgreSQL, and Redis, running on a local server (default port 3000). It's essential for reproducing issues in email notifications and UI interactions. Used in offensive security for controlled exploit demos.

## Features

- Feature 1: Full GitLab stack emulation locally.
- Feature 2: Includes dev tools like Letter Opener for email testing.
- Feature 3: Easy configuration for CE/EE versions.

## Installation

### Requirements

- Ruby 2.7+, Bundler, Git.
- 4GB+ RAM, Linux/macOS.

### Install Commands

```bash
# Clone and setup
curl -s https://raw.githubusercontent.com/gitlab-org/gitlab-development-kit/main/scripts/install | bash
gdk init
```

## Basic Usage

```bash
gdk start
```

### Common Options

| Option | Description |
|--------|-------------|
| `gdk start` | Start all services |
| `gdk stop` | Stop services |
| `gdk install` | Install GitLab |

## Examples

### Example 1: Basic Usage

```bash
gdk start
# Access at http://localhost:3000
```

### Example 2: Advanced Usage

```bash
gdk install gitlab-ee
# For Enterprise Edition testing
```

## Expected Output

Services start; GitLab UI available at port 3000 with login.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Local port 3000 traffic.
- GDK processes in task manager.

## Related Procedures


## Related Tools

- [[tools/Letter-Opener]]

## References

- Official documentation: https://gitlab.com/gitlab-org/gitlab-development-kit
- Setup guide: GDK wiki
