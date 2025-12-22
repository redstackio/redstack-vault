---
url: 'https://www.adobe.com/products/flashplayer/end-of-life-alternative.html'
tags:
  - flash
  - legacy
  - bypass
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:36.186Z'
id: 359dcc44-f194-4d23-99e7-caa8bac29645
validated: true
submitted: true
---
# Adobe Flash

**Status**: Unverified

## Overview

Adobe Flash (SWF) is a legacy multimedia platform used here to forge custom HTTP headers in cross-origin requests, bypassing browser security for CSRF exploits.

## Description

Flash allows setting arbitrary headers via URLRequest, which modern JS cannot. Deprecated since 2020, but exploitable in legacy setups. Used to set Content-Type for JSON in this attack.

## Features

- Feature 1: Custom header injection in requests
- Feature 2: Cross-origin access with crossdomain.xml
- Feature 3: POST data handling with method preservation

## Installation

### Requirements

- Legacy browser supporting Flash
- Adobe Flash Player (discontinued)

### Install Commands

Flash is client-side; no install, but embed via <object> in HTML.

## Basic Usage

Embed SWF in page to trigger request.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Flash is scripted |

## Examples

### Example 1: Basic Usage

Embed:

```html
<object data="exploit.swf" type="application/x-shockwave-flash"></object>
```

### Example 2: Advanced Usage

Script AS3 for header forge as in procedure.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Flash plugin activity in logs
- Unusual cross-origin requests with custom headers
- Legacy Flash traffic

## Related Procedures


## Related Tools

- [[tools/PHP-Redirector-Script]]

## References

- Adobe Flash EOL notice
