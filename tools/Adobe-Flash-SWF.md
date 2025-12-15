---
id: tool-adobe-flash-swf
url: 'https://www.adobe.com/products/flashplayer.html'
tags:
  - flash
  - swf
  - cross-domain
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.757Z'
validated: true
submitted: true
---
# Adobe-Flash-SWF

**Status**: Unverified

## Overview

Adobe Flash SWF files are used to create interactive web content, but in security testing, they exploit legacy cross-domain policies for bypassing restrictions in APIs like Vimeo's OAuth.

## Description

Flash enables client-side execution of ActionScript for network requests, loading policy files to relax security sandboxes. Commonly used in offensive ops for CSRF and cross-site flashing attacks on outdated services. Tested on Windows 8.1/10 with browsers like Firefox 46, Chrome 50, IE 11.

## Features

- Feature 1: Security.loadPolicyFile for cross-domain policy loading
- Feature 2: URLLoader for making HTTP requests across domains
- Feature 3: Event handling for asynchronous response parsing

## Installation

### Requirements

- Adobe Flash Player plugin
- ActionScript compiler (e.g., Adobe Flex SDK)

### Install Commands

```bash
# Download and install Flash Player from Adobe site
# Compile SWF: asc malicious.as -out malicious.swf
```

## Basic Usage

```actionscript
Security.loadPolicyFile('https://target.com/crossdomain.xml');
```

### Common Options

| Option | Description |
|--------|-------------|
| `-swf` | Compile to SWF format |
| `--debug` | Enable debug tracing |

## Examples

### Example 1: Basic Usage

```actionscript
var loader = new URLLoader(new URLRequest('https://api.vimeo.com/oauth/authorize'));
```

### Example 2: Advanced Usage

```actionscript
Security.loadPolicyFile('https://api.vimeo.com/oauth/crossdomain.xml');
loader.load(new URLRequest('https://api.vimeo.com/oauth/authorize'));
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Tactics

- [[Execution]]
- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Flash plugin loads from untrusted sources
- Network requests to crossdomain.xml
- SWF execution traces in browser dev tools

## Related Procedures


## Related Tools

- [[tools/xss-swf]]

## References

- Adobe Flash Documentation
- OWASP Flash Security Guide
