---
url: null
tags:
  - browser
  - demo
type: tool
platforms:
  - Web
description: Web browser used for demonstrating attacks with multiple profiles.
id: 5b16830e-adef-4385-ba47-3700dd8df22b
created_at: '2025-12-11T06:10:22.300Z'
updated_at: '2025-12-11T06:10:22.300Z'
verified: false
validated: true
submitted: true
---
# Chrome Browser

**Status**: Unverified

## Overview

Google Chrome is a web browser that supports multiple profiles and incognito mode, ideal for separating attacker and victim sessions in demos.

## Description

Used for initiating sign-ins, capturing states, and executing JavaScript in console for hijacking.

## Features

- Multiple user profiles
- Incognito mode
- Developer console

## Installation

### Requirements

- OS support

### Install Commands

Download from official site.

## Basic Usage

```bash
chrome --incognito
```

### Common Options

| Option | Description |
|--------|-------------|
| `--user-data-dir` | Specify profile directory |

## Examples

### Example 1: Basic Usage

Open with profile: chrome --profile-directory="Profile 1"

### Example 2: Advanced Usage

Incognito for hijack.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser activity logs
- Unusual profile usage

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

## References

- Official site: https://www.google.com/chrome
