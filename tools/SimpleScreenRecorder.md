---
url: null
tags:
  - poc
  - recording
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.475Z'
id: 0bc5fab2-5253-446d-b558-c140677d6294
validated: true
submitted: true
---
# SimpleScreenRecorder

**Status**: Unverified

## Overview

SimpleScreenRecorder is a lightweight screen recording tool for Linux, ideal for capturing proof-of-concept videos in security demonstrations, such as showing subdomain resolution changes.

## Description

Used to record browser interactions and DNS verifications during attacks, providing visual evidence of exploits like subdomain takeovers without complex setup.

## Features

- Feature 1: Easy area selection for recording
- Feature 2: Audio and video capture
- Feature 3: Export to common formats for POCs

## Installation

### Requirements

- Linux OS (Ubuntu, etc.)

### Install Commands

```bash
sudo apt update && sudo apt install simplescreenrecorder
```

## Basic Usage

```bash
simplescreenrecorder
```

### Common Options

| Option | Description |
|--------|-------------|
| `--start-recording` | Begin recording immediately |
| `-g` | Show GUI |

## Examples

### Example 1: Basic Usage

```bash
simplescreenrecorder
```
Select area and record browser visit to subdomain.

### Example 2: Advanced Usage

```bash
simplescreenrecorder --start-recording
```
Capture DNS command execution and site load.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process: simplescreenrecorder running
- File artifacts: .srec recordings

## Related Procedures

- [[procedures/Verify-Subdomain-Takeover]]

## Related Tools

- [[tools/obs-studio]]

## References

- GitHub: https://github.com/MaartenBaert/ssr
