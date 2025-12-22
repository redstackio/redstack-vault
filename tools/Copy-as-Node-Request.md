---
url: 'https://portswigger.net/bappstore/e170472f83ef4da1bca5897203b6b33d'
tags:
  - burp-extension
  - code-generation
type: tool
verified: false
platforms:
  - Java
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:53.802Z'
id: aaf15765-5786-43b7-a2b0-6e2e3355c996
validated: true
submitted: true
---
# Copy-as-Node-Request

**Status**: Unverified

## Overview

Burp Suite extension for copying HTTP requests as executable Node.js code, vulnerable to code injection via unsanitized cookie values.

## Description

This BApp generates Node.js scripts from Burp-intercepted requests, useful for reproducing issues in Node environments. However, its cookie handling in BurpExtender.java fails to escape single quotes, enabling RCE when malicious cookies are present.

## Features

- Feature 1: Converts requests to Node.js fetch or http module code
- Feature 2: Handles headers including cookies in string literals
- Feature 3: Integrates directly with Burp's right-click menu

## Installation

### Requirements

- Burp Suite
- Java 8+

### Install Commands

No CLI; install via Burp Extender > BApp Store > Search 'Copy as Node Request' > Install.

## Basic Usage

Right-click intercepted request > Copy as Node.js Request.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | GUI-based; no CLI options |

## Examples

### Example 1: Basic Usage

Intercept request, right-click, copy – pastes Node.js code to clipboard.

### Example 2: Advanced Usage

Use with malicious cookie: Generates injectable code.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Software
- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Burp logs showing extension loads
- Node.js processes from generated scripts
- Anomalous calc.exe spawns post-Burp use

## Related Procedures

- [[procedures/Install-Copy-as-Node-Request-Extension]]
- [[procedures/Copy-Request-as-Node-js-Code]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- PortSwigger BApp Store
- GitHub source for vulnerability review
