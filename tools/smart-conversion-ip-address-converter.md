---
id: tool-002
url: 'http://www.smartconversion.com/unit_conversion/IP_Address_Converter.aspx'
tags:
  - ip-conversion
  - decimal-encoding
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:23.205Z'
validated: true
submitted: true
---
# Smart Conversion IP Address Converter

**Status**: Unverified

## Overview

Smart Conversion IP Address Converter is an online tool that converts standard dotted IPv4 addresses to single decimal (dotless) numbers and vice versa, aiding in bypass techniques for web vulnerabilities that filter dots.

## Description

This utility takes an IP like 93.184.216.34 and outputs its integer equivalent (1572395042), calculated as (93*256^3 + 184*256^2 + 216*256 + 34). It's essential for encoding IPs in URL paths for open redirects or SSRF where dotted notation is blocked. Browser-based, no setup needed.

## Features

- Feature 1: Bidirectional conversion (dotted to decimal, decimal to dotted).
- Feature 2: Handles IPv4 only with precise calculations.
- Feature 3: Simple interface for quick conversions.

## Installation

### Requirements

- Internet-connected browser.

### Install Commands

Direct URL access; no install.

## Basic Usage

Input dotted IP and select conversion type.

### Common Options

| Option | Description |
|--------|-------------|
| IP Input | Dotted IP (e.g., 93.184.216.34) |
| Convert | Performs decimal transformation |

## Examples

### Example 1: Basic Usage

Input 93.184.216.34 to get 1572395042.

### Example 2: Advanced Usage

Convert back: Input 1572395042 to verify 93.184.216.34.

## Expected Output

Single integer value representing the IP in decimal form.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Traffic to smartconversion.com from pentesting IPs.
- Unusual numeric URL paths in app logs.

## Related Procedures


## Related Tools

- [[tools/site24x7-ip-finder]]

## References

- Official site: http://www.smartconversion.com/unit_conversion/IP_Address_Converter.aspx
