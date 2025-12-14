---
id: tool-burp-intruder
url: 'https://portswigger.net/burp/documentation/desktop/tools/intruder'
tags:
  - fuzzing
  - scanning
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.867Z'
validated: true
submitted: true
---
# Burp-Intruder

**Status**: Unverified

## Overview

Burp Intruder is a module within Burp Suite for automated customized attacks, ideal for fuzzing parameters like ports in Blind SSRF scenarios to detect open services via response analysis.

## Description

It allows setting payload positions in requests, generating wordlists (e.g., ports 1-65535), and analyzing results based on metrics like response time. For SSRF port scanning, it exploits timing differences without visible output.

## Features

- Feature 1: Payload generation and insertion for brute-force testing.
- Feature 2: Response analysis by length, time, or custom rules.
- Feature 3: Attack types like Sniper for single-position fuzzing.

## Installation

### Requirements

- Burp Suite Community or Professional edition.

### Install Commands

```bash
# Included in Burp Suite; launch via GUI
```

## Basic Usage

In Burp, right-click request > Send to Intruder.

### Common Options

| Option | Description |
|--------|-------------|
| Sniper | Single payload position |
| Cluster bomb | Multiple positions |

## Examples

### Example 1: Basic Usage

Set §sievePort§ position, add numbers payload, start attack.

### Example 2: Advanced Usage

Configure grep-extract for timings; sort by response received.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Rapid successive requests to the same endpoint with varying parameters.
- Server-side logs showing connection timeouts from fuzzing.

## Related Procedures

- [[procedures/Fuzz-Ports-with-Burp-Intruder-for-Blind-Scanning]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://portswigger.net/burp/documentation/desktop/tools/intruder
