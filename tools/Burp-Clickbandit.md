---
id: tool-uuid-001
url: >-
  https://portswigger.net/burp/documentation/desktop/testing-workflow/clickbandit
tags:
  - clickjacking
  - poc-generation
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.723Z'
validated: true
submitted: true
---
# Burp-Clickbandit

**Status**: Unverified

## Overview

Burp Clickbandit is a Burp Suite extension for generating clickjacking proof-of-concept HTML pages, used to demonstrate UI redress attacks by overlaying iframes with invisible elements.

## Description

It automates creation of malicious HTML that embeds target sites in iframes and positions overlays to capture clicks on sensitive elements. Ideal for testing missing X-Frame-Options in web apps like dev.twitter.com. Features include customizable overlay text, positioning, and exportable PoCs.

## Features

- Feature 1: Automatic iframe embedding with target URL
- Feature 2: Overlay configuration for deceptive UI (e.g., fake buttons)
- Feature 3: Preview and export of HTML PoC files

## Installation

### Requirements

- Burp Suite Professional or Community
- Java 8+

### Install Commands

```bash
# Download from PortSwigger BApp Store within Burp Suite
# Or manually: wget https://portswigger.net/bappstore/.../clickbandit.jar
# Load in Burp: Extender > Extensions > Add > JAR file
```

## Basic Usage

```bash
tool-name --help
```

In Burp: Go to Clickbandit tab, enter target URL, configure overlay, generate PoC.

### Common Options

| Option | Description |
|--------|-------------|
| Target URL | URL to iframe |
| Overlay Text | Text for fake button |
| Position | X/Y coordinates for overlay |

## Examples

### Example 1: Basic Usage

Enter XSS URL in Clickbandit, set overlay to "Click to Continue", generate HTML.

### Example 2: Advanced Usage

```bash
# Within Burp UI: Set multiple overlays for complex deception
```

Host generated HTML on local server and test in browser.

## Expected Output

HTML file with <iframe> and <div> overlay; loads target and tricks clicks.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTML with nested iframes and absolute-positioned divs
- Traffic to Burp proxy during PoC generation
- Anomalous click patterns in web logs

## Related Procedures


## Related Tools

- [[Burp-Suite]]
- [[BeEF]]

## References

- Official documentation: https://portswigger.net/burp/documentation/desktop/testing-workflow/clickbandit
- Related resources: OWASP Clickjacking Defense Cheat Sheet
