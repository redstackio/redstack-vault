---
id: tool-uuid-3
url: 'https://www.mozilla.org/en-US/firefox/new/'
tags:
  - browser
  - web
  - testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.248Z'
validated: true
submitted: true
---
# Firefox

**Status**: Unverified

## Overview

Firefox is an open-source web browser used for accessing target sites, crafting URLs, and simulating victim interactions in web vulnerability testing like SSRF exploitation.

## Description

In security assessments, Firefox's developer tools aid in inspecting payloads and triggers. Version 80.0.1 was used here for compatibility with the exploit scenario, supporting JavaScript execution and network monitoring.

## Features

- Feature 1: Developer Tools for network inspection and console logging
- Feature 2: Extensions like Firebug for advanced debugging
- Feature 3: Cross-platform support with privacy-focused modes

## Installation

### Requirements

- Modern OS with GUI

### Install Commands

```bash
# On Ubuntu
sudo apt update && sudo apt install firefox
# Download from official site for other OS
```

## Basic Usage

```bash
firefox https://example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `--private-window` | Open in private mode |
| `--headless` | Run without GUI (for automation) |

## Examples

### Example 1: Basic Usage

```bash
firefox https://www.█████████
```

### Example 2: Advanced Usage

```bash
firefox --private-window "malicious-url-here"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Browser user-agent strings in logs (e.g., Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0)
- Access patterns to vulnerable URLs

## Related Procedures

- [[procedures/Craft-and-Inject-SSRF-Payload-into-Login-URL]]
- [[procedures/Trigger-SSRF-Exploit-from-Victim-Device]]

## Related Tools

- [[Related Tool: Chrome]]
- [[Related Tool: Burp Suite Proxy]]

## References

- Official documentation: https://support.mozilla.org/en-US/products/firefox
- Related resources: MDN Web Docs for JS fetch API
