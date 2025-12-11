---
url: ''
tags:
  - verification
  - user
type: tool
platforms:
  - Linux
description: 'Displays the current user''s name, used to confirm RCE.'
id: 5ec2919d-f3a0-4614-9313-2dfd3935683c
created_at: '2025-12-11T03:47:39.842Z'
updated_at: '2025-12-11T03:47:39.842Z'
verified: false
validated: true
submitted: true
---
# whoami

**Status**: Unverified

## Overview

Whoami is a command to print the effective username, useful for verifying user context after access gain.

## Description

Simple utility for user identification in shells; common in post-exploitation to confirm privileges.

## Features

- User name display

## Installation

### Requirements

- Linux system

### Install Commands

(Pre-installed)

## Basic Usage

```bash
whoami
```

### Common Options

| Option | Description |
|--------|-------------|
| (none) | No options |

## Examples

### Example 1: Basic Usage

```bash
whoami
```

## Expected Output

Current username.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Owner-User Discovery]]

### Tactics

- [[Discovery]]

## Detection

- Monitor whoami in logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #id

## References

- Man page: whoami(1)
