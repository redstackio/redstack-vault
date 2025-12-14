---
url: ''
tags:
  - gitlab
  - rake
  - admin
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.606Z'
id: a11846c6-7f30-489b-a408-0f0fca7769a8
validated: true
submitted: true
---
# gitlab-rake

**Status**: Unverified

## Overview

GitLab Rake is a command-line tool wrapper around Ruby's Rake for running maintenance and info tasks on GitLab instances, such as gathering environment details for reports.

## Description

It executes predefined tasks like env:info without needing the Rails console. Useful in security reports to document the target environment, including versions that confirm vulnerability presence.

## Features

- Feature 1: Run GitLab-specific Rake tasks
- Feature 2: Environment checks and migrations
- Feature 3: Backup and diagnostic functions

## Installation

### Requirements

- GitLab installation
- Access to /opt/gitlab/bin/

### Install Commands

```bash
# Part of GitLab; use directly
sudo gitlab-rake <task>
```

## Basic Usage

```bash
gitlab-rake gitlab:env:info
```

### Common Options

| Option | Description |
|--------|-------------|
| -T | List all tasks |

## Examples

### Example 1: Basic Usage

```bash
gitlab-rake gitlab:env:info
```

### Example 2: Advanced Usage

```bash
gitlab-rake gitlab:check
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques


### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Command logs in system audit
- Output files from tasks

## Related Procedures


## Related Tools

- [[tools/gitlab-rails-console]]

## References

- GitLab Rake tasks documentation
