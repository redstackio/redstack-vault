---
url: 'http://meyerweb.com/eric/tools/dencoder/'
tags:
  - encoding
  - xss
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.366Z'
id: 92bd5be7-6d48-46f2-abd3-a5f0d3efd5c5
validated: true
submitted: true
---
# Meyerweb-Dencoder-URL-Encoder

**Status**: Unverified

## Overview

The Meyerweb Dencoder is a web-based tool for encoding and decoding URLs, HTML entities, and other formats, commonly used in security testing to prepare payloads for injection into web applications that reject raw special characters.

## Description

This online utility, created by Eric Meyer, supports URL encoding/decoding, HTML entity conversion, and base64 operations. In offensive security, it's ideal for crafting XSS payloads like '<img src=x onerror=alert(1) "' by encoding to evade input filters, as seen in Mapbox editor injections. It runs entirely in the browser, requiring no installation, and handles common web encoding needs without server-side dependencies.

## Features

- Feature 1: URL encoding/decoding for query strings and paths
- Feature 2: HTML entity encoding/decoding (e.g., &lt; to <)
- Feature 3: Base64 encode/decode for obfuscation

## Installation

### Requirements

- Modern web browser (Chrome, Firefox, etc.)
- Internet access to the tool's URL

### Install Commands

No installation needed; access via browser.

## Basic Usage

Visit http://meyerweb.com/eric/tools/dencoder/ and select the encoding type.

### Common Options

| Option | Description |
|--------|-------------|
| URL Encode | Converts special chars to %XX format |
| HTML Decode | Converts entities like &lt; to < |

## Examples

### Example 1: Basic Usage

Input: <img src=x onerror=alert(1)"
Select HTML Encode.

### Example 2: Advanced Usage

Input: https://example.com?payload=<script>alert(1)</script>
Select URL Encode to get https://example.com?payload=%3Cscript%3Ealert(1)%3C/script%3E

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser history entries for meyerweb.com
- Encoded payloads in application logs

## Related Procedures


## Related Tools

- [[Burp Suite Encoder]]
- [[Online URL Encoder Tools]]

## References

- Official site: http://meyerweb.com/eric/tools/dencoder/
- Usage in XSS: OWASP XSS Prevention Cheat Sheet
