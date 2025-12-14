---
url: null
tags:
  - browser
  - testing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.653Z'
configuration: Build 61.0.3131.0
id: b3c0b4df-d6c5-48ee-9ca4-cccf8d5d6176
validated: true
submitted: true
---
# Chromium

**Status**: Unverified

## Overview

Chromium is the open-source browser project behind Chrome, used for vulnerability testing due to its similarity to production browsers and customizable builds.

## Description

Build 61.0.3131.0 was employed to verify JS execution consistency across browsers in the XSS PoC, ensuring the payload works beyond Chrome.

## Features

- Feature 1: Open-source for modifications
- Feature 2: Dev tools identical to Chrome
- Feature 3: Lightweight alternative

## Installation

### Requirements

- Linux preferred

### Install Commands

```bash
# Build from source or use package manager
sudo apt install chromium-browser
```

## Basic Usage

```bash
chromium --version
```

### Common Options

| Option | Description |
|--------|-------------|
| `--no-sandbox` | For root testing |

## Examples

### Example 1: Basic Usage

Launch and navigate to CMS for testing.

### Example 2: Advanced Usage

Use with --user-data-dir for profile isolation.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- User-Agent identifying Chromium builds

## Related Procedures

- [[procedures/Trigger-XSS-via-Victim-Reply]]

## Related Tools

- [[tools/Chrome]]

## References

- Official: https://www.chromium.org/
