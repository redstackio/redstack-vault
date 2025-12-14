---
url: 'https://git-scm.com'
tags:
  - vcs
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.379Z'
id: e005f658-bf77-4fc0-99ef-aa120e3b9239
validated: true
submitted: true
---
# git

**Status**: Unverified

## Overview

Version control system for cloning and checking out the Rocket.Chat repo to set up vulnerable environment.

## Description

Essential for reproducing the vulnerability by pulling specific tagged versions.

## Features

- Feature 1: Clone repositories
- Feature 2: Checkout tags/branches
- Feature 3: Local versioning

## Installation

### Requirements

- OS package manager

### Install Commands

```bash
sudo apt install git
```

## Basic Usage

```bash
git --help
```

### Common Options

| Option | Description |
|--------|-------------|
| clone | Clone repo |
| checkout | Switch versions |

## Examples

### Example 1: Basic Usage

```bash
git clone url
```

## MITRE ATT&CK Mapping

### Techniques

- [[Video Capture]] Video Discovery (adapted for setup)

### Tactics


## Detection

- Git processes in security contexts low risk

## Related Procedures


## Related Tools

- [[tools/docker-compose]]

## References

- Git docs
