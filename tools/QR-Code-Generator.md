---
id: tool-qr-gen-001
url: 'https://app.qr-code-generator.com/'
tags:
  - qr-code
  - phishing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:34.847Z'
validated: true
submitted: true
---
# QR-Code-Generator

**Status**: Unverified

## Overview

QR Code Generator is a web-based tool for creating QR codes that encode URLs, text, or other data, commonly used in security testing to craft malicious payloads for phishing via QR scans.

## Description

This online service allows users to input data like URLs and generate scannable QR images in formats such as PNG. In offensive security, it's used to embed malicious links for exploiting scanner vulnerabilities, like auto-redirects in browsers. No installation required; fully browser-based.

## Features

- Feature 1: URL encoding into QR codes with customizable sizes and error correction
- Feature 2: Download options for PNG, SVG, or EPS formats
- Feature 3: Free basic usage; premium for logos or colors

## Installation

### Requirements

- Modern web browser
- Internet connection

### Install Commands

No installation needed; access via URL.

## Basic Usage

Visit https://app.qr-code-generator.com/ and enter data to generate.

### Common Options

| Option | Description |
|--------|-------------|
| URL Input | Field to enter the malicious URL |
| Size | Adjust QR dimensions for print/digital use |
| Download | Export as image file |

## Examples

### Example 1: Basic Usage

Enter `http://www.evil.com/` and generate; download PNG.

### Example 2: Advanced Usage

Add error correction level 'H' for robustness in scanning tests.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]] Phishing

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Web traffic to qr-code-generator domains from testing environments
- Presence of newly generated QR images with suspicious URLs

## Related Procedures


## Related Tools

- [[tools/Brave-Browser]]

## References

- Official site: https://app.qr-code-generator.com/
- QR code standards documentation
