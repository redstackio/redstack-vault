---
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/h0h1llrczzhyhl941x480fp6yusj?response-content-disposition=attachment%3B%20filename%3D%22poc_timing_attack.py%22%3B%20filename%2A%3DUTF-8%27%27poc_timing_attack.py&response-content-type=application%2Fx-sh&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ3PYP6QN7%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T065512Z&X-Amz-Expires=3600&X-Amz-Security-Token=...&X-Amz-SignedHeaders=host&X-Amz-Signature=340d451aa1c92b5d3fa19128bca01713a429d019dd91d523916c39356d3760e8
tags:
  - poc
  - timing-attack
type: tool
verified: false
platforms:
  - Linux
created_at: '2024-12-14T00:00:00Z'
updated_at: '2025-12-14T17:31:30.948Z'
id: 1ad8a497-502f-4303-9fe0-cab7da5e442a
validated: true
submitted: true
---
# poc-timing-attack-py

**Status**: Unverified

## Overview

A custom Python PoC script designed to exploit the timing attack in curl's Digest Authentication by testing algorithms and detecting response time discrepancies.

## Description

The script sends HTTP requests to a target using curl subprocesses or requests, measures nanosecond timings, and analyzes deviations to fingerprint supported algorithms like MD5 or SHA-1, targeting the strcmp() vuln at digest.c:360.

## Features

- Feature 1: Multi-algorithm testing (MD5, MD5-sess, SHA-1)
- Feature 2: High-precision timing with perf_counter
- Feature 3: Automatic deviation calculation and vuln confirmation

## Installation

### Requirements

- Python 3 and requests module

### Install Commands

```bash
# Download from source
wget [URL] -O poc_timing_attack.py
# Or pip if packaged, but custom
```

## Basic Usage

```bash
python3 poc_timing_attack.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u, --url` | Target URL |
| `-a, --algorithms` | List of algorithms to test |

## Examples

### Example 1: Basic Usage

```bash
python3 poc_timing_attack.py http://localhost:8080/protected
```

### Example 2: Advanced Usage

```bash
python3 poc_timing_attack.py http://target.com --algorithms MD5,SHA1 --iterations 100
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Script execution logs with timing measurements
- Repeated auth requests with varying algorithms

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: Python]]
- [[Related Tool: requests-module]]

## References

- HackerOne report: https://hackerone.com/reports/3346118
