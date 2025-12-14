---
id: tool-3
url: ''
tags:
  - fuzzing
  - automation
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.945Z'
validated: true
submitted: true
---
# Burp-Suite-Intruder

**Status**: Unverified

## Overview

Burp Suite Intruder is an automated fuzzing tool for testing web applications by injecting payloads into requests and analyzing responses, ideal for parameter scanning like port fuzzing in SSRF.

## Description

It allows positioning payloads (e.g., on imapPort), loading wordlists, and configuring attacks based on response metrics like time or length. Here, used to automate port scanning by fuzzing ports and sorting by response time.

## Features

- Feature 1: Payload positions and types (e.g., numbers, lists)
- Feature 2: Attack configurations (Sniper, Cluster bomb)
- Feature 3: Response analysis by length, time, or grep

## Installation

### Requirements

- Burp Suite Professional

### Install Commands

```bash
# Part of Burp Suite; access via Proxy > Send to Intruder
java -jar burpsuite_pro.jar
```

## Basic Usage

```bash
# GUI: Right-click request > Send to Intruder > Positions > Add § > Payloads > Load list > Start attack
```

### Common Options

| Option | Description |
|--------|-------------|
| Sniper | Single payload position |
| Response Time | Sort by timing |

## Examples

### Example 1: Basic Usage

Fuzz imapPort with ports list for timing-based scan.

### Example 2: Advanced Usage

Use grep-extract to pull service banners if possible.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Rapid successive requests with incremental payloads
- Server logs showing patterned fuzzing on endpoints

## Related Procedures

- [[procedures/Automated-Port-Scanning-with-Burp-Intruder]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Documentation: https://portswigger.net/burp/documentation/desktop/testing-workflow/intruder
