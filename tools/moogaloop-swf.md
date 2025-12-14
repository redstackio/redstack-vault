---
id: tool-vimeo-moogaloop-001
url: 'https://f.vimeocdn.com/p/flash/moogaloop/6.3.5/moogaloop.swf'
tags:
  - flash-player
  - vimeo
type: tool
verified: false
platforms:
  - Web
  - Flash
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:36.200Z'
validated: true
submitted: true
---
# moogaloop-swf

**Status**: Unverified

## Overview

moogaloop.swf is Vimeo's official Flash player SWF used for embedding and playing videos on their platform. In security testing, it is exploited due to lack of input sanitization in the 'config_url' parameter, allowing external SWFs to load and control it for cross-site requests.

## Description

This SWF file handles video playback and configuration via FlashVars like config_url. When loaded externally, it can be manipulated to request arbitrary URLs, such as Vimeo's /moogaloop 404 page, exposing sensitive data under permissive crossdomain policies. Commonly used in offensive operations to chain with malicious SWFs for token theft and CSRF.

## Features

- Feature 1: Video embedding and playback control
- Feature 2: Configurable via FlashVars (e.g., config_url for API endpoints)
- Feature 3: Cross-domain requests enabled by Vimeo's policy

## Installation

### Requirements

- Adobe Flash Player plugin in browser
- No installation; loaded via URL

### Install Commands

N/A (web resource)

## Basic Usage

Embed in HTML:

```html
<object data="https://f.vimeocdn.com/p/flash/moogaloop/6.3.5/moogaloop.swf?config_url=https://vimeo.com/video/123" type="application/x-shockwave-flash"></object>
```

### Common Options

| Option | Description |
|--------|-------------|
| config_url | URL for player configuration (exploitable for arbitrary requests) |
| autoplay | Boolean for auto-play |

## Examples

### Example 1: Basic Usage

Load for video playback:

```html
<embed src="https://f.vimeocdn.com/p/flash/moogaloop/6.3.5/moogaloop.swf" flashvars="config_url=https://vimeo.com/video/123">
```

### Example 2: Advanced Usage (Exploitation)

Set config_url to trigger 404:

```html
<embed src="https://f.vimeocdn.com/p/flash/moogaloop/6.3.5/moogaloop.swf" flashvars="config_url=https://vimeo.com/moogaloop">
```

## Expected Output

Flash player renders; requests config_url and displays video or error page content if exploited.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing requests to moogaloop.swf from external domains
- Flash sandbox violations or crossdomain.xml accesses
- Anomalous 404 requests to /moogaloop

## Related Procedures


## Related Tools

- [[tools/evil-swf]]
- [[tools/xss-swf]]

## References

- Vimeo Flash documentation (archived)
- HackerOne Report #136481
