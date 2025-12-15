---
id: tool-fromcharcode-encoder-001
url: >-
  https://www.martineve.com/2007/05/15/javascript-eval-string-fromcharcode-encoder
tags:
  - encoding
  - obfuscation
  - javascript
type: tool
verified: false
platforms:
  - Web
  - Browser
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.385Z'
validated: true
submitted: true
---
# String-fromCharCode-Encoder

**Status**: Unverified

## Overview

A JavaScript encoder that converts strings to Unicode character codes using String.fromCharCode, used to obfuscate payloads and bypass filters in XSS attacks like Simplenote exploitation.

## Description

This online tool or script encodes JS code into comma-separated char codes, allowing injection via writeln() in restricted contexts, essential for escalating XSS to RCE by hiding Node.js commands.

## Features

- Feature 1: String to fromCharCode conversion
- Feature 2: Supports eval decoding
- Feature 3: Handles special characters for evasion

## Installation

### Requirements

- Web browser

### Install Commands

No installation; use online version.

## Basic Usage

Visit the URL and input JS code to encode.

### Common Options

| Option | Description |
|--------|-------------|
| Input | JS string to encode |
| Output | Comma-separated codes |

## Examples

### Example 1: Basic Usage

Input: `alert('XSS')`
Output: `97,108,101,114,116,40,39,88,83,83,39,41`

### Example 2: Advanced Usage

Input: Full Node.js RCE script
Output: Long sequence for writeln injection.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Scan for fromCharCode patterns in input
- Monitor encoded JS in web requests

## Related Procedures

- [[procedures/Escalate-XSS-to-RCE-with-Encoded-Payload]]

## Related Tools

- [[tools/Simplenote-Desktop-App]]

## References

- Tool page: https://www.martineve.com/2007/05/15/javascript-eval-string-fromcharcode-encoder
