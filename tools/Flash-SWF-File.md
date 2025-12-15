---
id: t-flash-swf
url: null
tags:
  - flash
  - csrf
  - bypass
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.807Z'
validated: true
submitted: true
---
# Flash SWF File

**Status**: Unverified

## Overview

Adobe Flash SWF files are used in this context to initiate cross-origin POST requests with forged headers, exploiting legacy browser support for CSRF in JSON APIs.

## Description

SWF enables sending HTTP requests outside SOP/CORS limits, allowing Content-Type forgery when proxied. In the Federalist attack, it's embedded in HTML to auto-send JSON payloads via PHP redirect.

## Features

- Cross-origin request capability
- Header manipulation (e.g., Content-Type: application/json)
- Parameterized payloads for dynamic exploits

## Installation

### Requirements

- Adobe Flash Player (legacy, browser-embedded)
- ActionScript compiler or pre-built from repos

### Install Commands

No installation; use browser with Flash enabled.

## Basic Usage

Embed in HTML: <embed src="exploit.swf?params" type="application/x-shockwave-flash">

### Common Options

| Option | Description |
|--------|-------------|
| jsonData | JSON payload string |
| php_url | Proxy endpoint |
| endpoint | Target API URL |

## Examples

### Example 1: Basic Embed

<html><body><embed src="swf.swf?jsonData={\"site\":1}&php_url=/proxy&endpoint=/v0/build/"></body></html>

### Example 2: With Crossdomain

Host with crossdomain.xml for * access.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Flash execution logs in browser
- Network requests from SWF origins
- Legacy Flash plugin detection

## Related Procedures


## Related Tools

- [[tools/PHP-Redirector]]
- [[tools/swf-json-csrf]]

## References

- Adobe Flash documentation (legacy)
