---
url: 'https://github.com/danielmiessler/SecLists'
tags:
  - wordlists
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.903Z'
id: ed6a8f7f-f8ba-44f3-b753-474597a049e7
validated: true
submitted: true
---
# SecLists

**Status**: Unverified

## Overview

Collection of wordlists for security testing and fuzzing.

## Description

Provides payloads for directory enumeration, API fuzzing, etc., used throughout the attack for common.txt.

## Features

- Feature 1: Categorized lists
- Feature 2: Web content discovery
- Feature 3: Regularly updated

## Installation

### Requirements

- Git

### Install Commands

```bash
git clone https://github.com/danielmiessler/SecLists.git
```

## Basic Usage

Use as -w path/to/SecLists/...

### Common Options

N/A (wordlist collection)

## Examples

### Example 1: Basic Usage

```bash
ffuf -w SecLists/Discovery/Web-Content/common.txt -u target/FUZZ
```

## MITRE ATT&CK Mapping

### Techniques

- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

- Usage inferred from fuzzing traffic

## Related Procedures

Multiple fuzzing steps

## Related Tools

- [[tools/dirb]]

## References

- GitHub repo
