---
id: tool-order2-py
url: null
tags:
  - python-script
  - api-testing
  - price-tampering
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.491Z'
validated: true
submitted: true
---
# order2.py

**Status**: Unverified

## Overview

Custom Python script for advanced manipulation of Upserve OLO order JSON, focusing on setting arbitrary low prices and zero taxes to further reduce totals in exploitation scenarios.

## Description

Similar to order.py but extended for price (e.g., 1 cent) and tax (0) tampering. It generates payloads ensuring client-side total matches, submits via POST, and handles responses for orders with extreme discounts.

## Features

- Support for minimal price and zero tax configurations.
- Integration with delivery fee bypassing.
- Logging of stored database values.

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
python order2.py
```

### Common Options

| Option | Description |
|--------|-------------|
| `--help` | Show usage |
| `--price` | Set custom item price (default 1) |
| `--tax` | Set tax amount (default 0) |

## Examples

### Example 1: Basic Usage

```bash
python order2.py
```

Submits with 1 cent price and zero tax.

### Example 2: Advanced Usage

```bash
python order2.py --price 1 --tax 0 --store upserve-hacker-cafe
```

Targets specific store with minimal values.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- API logs with zero-tax or sub-cent price payloads.
- Repeated submissions from same IP.

## Related Procedures

- [[procedures/Further-Manipulate-Prices-and-Taxes]]

## Related Tools

- [[tools/order-py]]

## References

- Derived from Upserve vulnerability PoC in HackerOne report
