---
url: ''
tags:
  - ruby
  - console
type: tool
verified: false
platforms:
  - GitLab
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.395Z'
id: 0c83f49a-e926-41ca-99e5-c25339d9d0d9
validated: true
submitted: true
---
# IRB

**Status**: Unverified

## Overview

Interactive Ruby Shell (IRB), used in GitLab's Rails console to test code, permissions, and object interactions during vulnerability research.

## Description

IRB is Ruby's REPL, extended in GitLab via 'gitlab-rails console' for backend testing. In security testing, it's crucial for verifying authorization logic like Ability.allowed? without type checks, aiding in exploit validation.

## Features

- Feature 1: Live code execution in Rails environment
- Feature 2: Access to models like User, Project, Group
- Feature 3: Permission and ability testing

## Installation

### Requirements

- GitLab installation
- SSH/root access to server

### Install Commands

```bash
# Enter Rails console
sudo gitlab-rails console
```

## Basic Usage

```bash
gitlab-rails console
irb(main):001:0>
```

### Common Options

| Option | Description |
|--------|-------------|
| -r file | Require a library |
| exit | Quit IRB |

## Examples

### Example 1: Basic Usage

```ruby
User.find(1)
```

### Example 2: Advanced Usage

Test permissions:

```ruby
Ability.allowed?(User.find(2), :delete_metrics_dashboard_annotation, Group.find(7))
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Console access logs on server
- Unusual Ruby executions in production

## Related Procedures


## Related Tools

- [[tools/GraphQL-Explorer]]

## References

- Ruby IRB Documentation
- GitLab Rails Console Guide
