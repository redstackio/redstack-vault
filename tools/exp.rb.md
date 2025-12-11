---
url: ''
tags:
  - exploit
  - ruby
type: tool
platforms:
  - Linux
description: >-
  Custom Ruby exploit script to combine path traversal with Gitaly race
  condition for arbitrary file reads.
id: e351b42e-3e47-41d1-9dd3-d31b8e8404a0
created_at: '2025-12-11T03:47:39.707Z'
updated_at: '2025-12-11T03:47:39.707Z'
verified: false
validated: true
submitted: true
---
# exp.rb

**Status**: Unverified

## Overview

exp.rb is a custom script for exploiting GitLab vulnerabilities, specifically path traversal and Gitaly race for file reads.

## Description

The script uses Faraday and rubyzip to upload packages and exploit the race, requiring URL and credential edits.

## Features

- API interaction
- Race condition timing
- File exfiltration

## Installation

### Requirements

- Ruby, Faraday, rubyzip

### Install Commands

```bash
# Script is custom, dependencies via gem install
```

## Basic Usage

```bash
ruby exp.rb
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Script-specific |

## Examples

### Example 1: Basic Usage

```bash
ruby exp.rb --url https://gitlab.example.com --token token
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for script execution patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Faraday]]

## References

- HackerOne report #822262
