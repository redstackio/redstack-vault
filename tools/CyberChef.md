---
url: 'https://gchq.github.io/CyberChef/'
tags:
  - encoding
  - decoding
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.325Z'
id: f9b9234f-cc2a-45fc-a651-6c685298f8b9
validated: true
submitted: true
---
# CyberChef

**Status**: Unverified

## Overview

CyberChef is a web-based tool for encoding, decoding, and transforming data, used here to prepare JavaScript payloads by minifying, base64-encoding, and URL-encoding for XSS injection.

## Description

It supports drag-and-drop recipes for operations like regex replace and base64. In the attack, recipes chain JS minify > base64 > wrap for eval > URL encode to create smuggling-ready payloads for keylogger and ATO.

## Features

- Feature 1: Modular recipe builder for data ops
- Feature 2: Supports 300+ operations (base64, URL encode, regex)
- Feature 3: Browser-based, no install needed

## Installation

### Requirements

- Modern browser

### Install Commands

```bash
# No install; access via URL
# Or clone repo: git clone https://github.com/gchq/CyberChef.git
```

## Basic Usage

```javascript
# Load page, add operations to recipe bar
```

### Common Options

| Option | Description |
|--------|-------------|
| Input | Paste data to encode |
| Recipe | Add ops like To_Base64 |

## Examples

### Example 1: Basic Usage

Minify JS > To_Base64 on keylogger code.

### Example 2: Advanced Usage

Full recipe: JS Minify > Base64 > Regex Replace for wrapping > URL Encode.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript (payload crafting)
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- N/A (client-side web tool)
- Look for encoded payloads in traffic

## Related Procedures

- [[procedures/Deploy-Persistent-Keylogger-for-Credential-Theft]]
- [[procedures/Perform-Account-Takeover-via-Google-Linking]]

## Related Tools

- [[tools/Base64-Encode-CLI]]

## References

- Official documentation: https://gchq.github.io/CyberChef/
- Related resources: GCHQ CyberChef GitHub
