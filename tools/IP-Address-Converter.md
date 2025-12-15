---
id: tool-ip-address-converter
url: 'http://www.smartconversion.com/unit_conversion/IP_Address_Converter.aspx'
tags:
  - obfuscation
  - conversion
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.847Z'
validated: true
submitted: true
---
# IP-Address-Converter

**Status**: Unverified

## Overview

Online tool for converting IPv4 addresses between dotted decimal and single integer formats, useful in security testing for obfuscating IPs in URLs to evade detection.

## Description

This web-based converter supports bidirectional transformation (e.g., 216.58.217.206 to 3627735502), aiding in crafting deceptive redirects or payloads. Commonly used in offensive ops for phishing and evasion without local installation.

## Features

- Feature 1: Dotted decimal to integer conversion
- Feature 2: Integer to dotted decimal reverse
- Feature 3: Simple web interface, no download needed

## Installation

### Requirements

- Web browser
- Internet access

### Install Commands

No installation; access via URL.

## Basic Usage

Visit the URL and input IP.

### Common Options

N/A (web form)

## Examples

### Example 1: Basic Usage

Input 216.58.217.206 → Output: 3627735502

### Example 2: Advanced Usage

Convert back: 3627735502 → 216.58.217.206

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]] Phishing

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Web traffic to conversion sites during testing
- Logs showing decimal IPs in URLs

## Related Procedures

- [[procedures/Obfuscate-IP-for-Phishing]]

## Related Tools

- [[Related Tool: Online IP Calculators]]

## References

- Official site: http://www.smartconversion.com/unit_conversion/IP_Address_Converter.aspx
