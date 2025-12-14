---
url: 'https://github.com/xmendez/wfuzz'
tags:
  - fuzzing
  - web
type: tool
platforms:
  - Linux
description: Web application fuzzer for brute-forcing and race condition exploitation.
id: da8933f0-bc46-4e1b-a431-9cdaafb89dea
created_at: '2025-12-14T03:46:09.448Z'
updated_at: '2025-12-14T03:46:09.448Z'
verified: false
validated: true
submitted: true
---
# wfuzz

**Status**: Unverified

## Overview

Wfuzz is a Python-based web fuzzer for discovering resources, fuzzing parameters, and exploiting races via parallel requests.

## Description

Used in pentesting for directory brute-force, parameter injection, and high-volume testing. Here, it floods GitLab's test endpoint to win the ToCToU race.

## Features

- Feature 1: Payload generators (range, file, etc.)
- Feature 2: HTTP method support (POST, GET)
- Feature 3: Cookie and header manipulation

## Installation

### Requirements

- Python 2/3

### Install Commands

```bash
pip install wfuzz
```

## Basic Usage

```bash
wfuzz -z list,1-10 http://target/FUZZ
```

### Common Options

| Option | Description |
|--------|-------------|
| -z | Payload set |
| -X | HTTP method |

## Examples

### Example 1: Basic Usage

```bash
wfuzz -z range,0-1000 https://target/test?FUZZ
```

### Example 2: Advanced Usage

With POST, cookies, data as in GitLab exploit.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- High request rates to specific endpoints
- Anomalous POST payloads

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[ffuf]]
- [[gobuster]]

## References

- GitHub: https://github.com/xmendez/wfuzz
