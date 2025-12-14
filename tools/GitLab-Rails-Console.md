---
url: ''
tags:
  - gitlab
  - console
  - admin
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.633Z'
id: 7502406b-5143-4bd1-8533-890d20987492
validated: true
submitted: true
---
# gitlab-rails-console

**Status**: Unverified

## Overview

The GitLab Rails console is an interactive Ruby shell for executing code directly in the GitLab application context, commonly used for administrative tasks like enabling feature flags in security testing.

## Description

It provides access to GitLab's models, services, and configurations via IRB. In offensive security, it's used to manipulate feature flags or query internal state without API exposure. Requires server access.

## Features

- Feature 1: Execute Ruby code against GitLab's database and logic
- Feature 2: Enable/disable feature flags dynamically
- Feature 3: Inspect and modify user/project data

## Installation

### Requirements

- GitLab self-managed installation
- Sudo access to the server

### Install Commands

```bash
# Already part of GitLab; access via:
sudo gitlab-rails console
```

## Basic Usage

```bash
gitlab-rails console
```

### Common Options

| Option | Description |
|--------|-------------|
| None specific | Runs in production mode by default |

## Examples

### Example 1: Basic Usage

```bash
gitlab-rails console
>> Feature.enable(:custom_emoji)
```

### Example 2: Advanced Usage

```bash
gitlab-rails console
>> User.find_by(username: 'admin').projects
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Console access logs in /var/log/gitlab/
- Audit events for feature changes

## Related Procedures

- [[procedures/Enable-Custom-Emoji-Feature-Flag-in-GitLab]]

## Related Tools

- [[tools/gitlab-rake]]

## References

- GitLab documentation on Rails console
