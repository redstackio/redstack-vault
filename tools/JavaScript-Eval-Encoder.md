---
id: tool-js-encoder
url: >-
  https://www.martineve.com/2007/05/15/javascript-eval-string-fromcharcode-encoder/
tags:
  - obfuscation
  - xss
type: tool
verified: false
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.243Z'
validated: true
submitted: true
---
# JavaScript-Eval-Encoder

**Status**: Unverified

## Overview

Online tool for encoding JavaScript payloads into eval(String.fromCharCode(...)) format to obfuscate code for XSS injections and evade detection.

## Description

Used in offensive security to convert JS strings to ASCII char codes, allowing safe injection into HTML attributes like onerror. Ideal for client-side attacks in apps like Simplenote.

## Features

- Feature 1: Instant encoding to fromCharCode
- Feature 2: Supports eval wrapping
- Feature 3: No installation required (web-based)

## Installation

### Requirements

- Web browser

### Install Commands

No installation; access via URL.

## Basic Usage

```bash
# Visit URL and paste JS payload
```

### Common Options

| Option | Description |
|--------|-------------|
| Input field | Paste raw JS |
| Encode button | Generate obfuscated output |

## Examples

### Example 1: Basic Usage

Input: var x = 1;
Output: eval(String.fromCharCode(118,97,114,32,120,32,61,32,49,59))

### Example 2: Advanced Usage

Input full script creation code for external load.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual fromCharCode strings in web payloads
- Traffic to known encoder domains

## Related Procedures

- [[procedures/Encode-JavaScript-Payload-for-XSS-Injection]]

## Related Tools

- [[tools/Process-Monitor-ProcMon]]

## References

- Official page: https://www.martineve.com/2007/05/15/javascript-eval-string-fromcharcode-encoder/
