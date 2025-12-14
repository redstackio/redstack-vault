---
url: 'https://github.com/PortSwigger/clickbandit'
tags:
  - clickjacking
  - web-testing
type: tool
platforms:
  - Web
description: >-
  Burp Suite extension for creating clickjacking proof-of-concepts by
  manipulating iframes and overlays.
id: c0a1da3a-50ed-4d08-ad70-83ea143a1845
created_at: '2025-12-13T23:52:55.741Z'
updated_at: '2025-12-13T23:52:55.741Z'
verified: false
validated: true
submitted: true
---
# Burp-Clickbandit

**Status**: Unverified

## Overview

Burp Clickbandit is a Burp Suite extension designed for security testers to build interactive clickjacking demonstrations. It allows embedding target pages in iframes and adding customizable overlays to simulate user interactions, ideal for exploiting frameable sites like dev.twitter.com without X-Frame-Options.

## Description

The tool integrates with Burp Suite to generate HTML PoCs that load vulnerable pages in iframes. Users can define overlay elements (visible or invisible) positioned over specific coordinates, binding clicks to underlying elements. This is commonly used in web pentesting to demonstrate UI redressing attacks chained with XSS or other client-side vulns.

## Features

- Feature 1: Iframe embedding with adjustable size and position
- Feature 2: Overlay creation for click hijacking (transparent or styled)
- Feature 3: Exportable HTML PoCs for sharing or hosting

## Installation

### Requirements

- Burp Suite Professional or Community Edition
- Java 8 or higher

### Install Commands

```bash
# Download from PortSwigger BApp Store or GitHub
# In Burp: Extender > BApp Store > Search 'Clickbandit' > Install
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

In Burp, launch Clickbandit from the Extender tab, input the target URL (e.g., XSS page), and generate a basic iframe PoC.

### Example 2: Advanced Usage

Configure overlays: Set iframe src to vulnerable URL, add div with position (x:100, y:200) and opacity 0, then export the HTML.

```html
<iframe src="https://dev.twitter.com//x:1/:///%01javascript:alert(document.cookie)/"></iframe>
<div style="position:absolute; top:200px; left:100px; width:100px; height:20px; opacity:0;" onclick="clickUnderlying()"></div>
```

## Expected Output

Generated HTML file that, when opened, shows the embedded page with clickable overlays triggering actions on the target.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to Burp proxy during PoC generation
- Unusual iframe requests from localhost or testing domains

## Related Procedures


## Related Tools

- [[Burp-Suite]]

## References

- Official documentation: https://portswigger.net/bappstore/clickbandit
- Related resources: OWASP Clickjacking Guide
