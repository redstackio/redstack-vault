---
id: tool-order-py
url: null
tags:
  - python-script
  - api-testing
  - payload-generation
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.493Z'
validated: true
submitted: true
---
# order.py

**Status**: Unverified

## Overview

Custom Python script for generating and submitting manipulated JSON payloads to Upserve's OLO API, primarily used in proof-of-concept exploits for negative quantity manipulation.

## Description

This script constructs order JSON with tampered 'charges.items' (negative quantities), includes store details, customer info, and payments, then performs a POST request to the submission endpoint. It's tailored for web API testing in business logic vulnerability assessments.

## Features

- JSON payload building with dynamic manipulation.
- HTTP POST submission via requests library.
- Response parsing for confirmation codes.

## Installation

### Requirements

- Python 3.x
- requests library: `pip install requests`

### Install Commands

```bash
pip install requests
```

## Basic Usage

```bash
python order.py
```

### Common Options

| Option | Description |
|--------|-------------|
| `--help` | Show usage (custom implementation) |
| `--payload` | Path to JSON file for submission |

## Examples

### Example 1: Basic Usage

```bash
python order.py
```

Submits hardcoded manipulated payload.

### Example 2: Advanced Usage

```bash
python order.py --store upserve-lounge-test-providence-2 --total 1870
```

Customizes store and total.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing POST to Upserve API with anomalous JSON.
- Python process spawning requests to order endpoints.

## Related Procedures

- [[procedures/Submit-Manipulated-JSON-to-Order-API]]

## Related Tools

- [[tools/order2-py]]

## References

- Upserve OLO API context from HackerOne report #364843
