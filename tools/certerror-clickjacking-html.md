---
id: tool-uuid-004
url: null
tags:
  - malicious-html
  - clickjacking
type: tool
verified: false
platforms:
  - Windows
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.427Z'
validated: true
submitted: true
---
# certerror-clickjacking-html

**Status**: Unverified

## Overview

A custom malicious HTML file designed to perform clickjacking by embedding Kaspersky's certificate error page in an iframe and overlaying a fake network protection warning to capture override clicks.

## Description

The file uses standard HTML/JS to load the warning via iframe (no X-Frame-Options block) and positions a transparent or styled link over the real button, tricking users into bypassing SSL. Can be extended to Safe Money or phishing UIs.

## Features

- Feature 1: Iframe embedding of security pages
- Feature 2: CSS positioning for UI overlay
- Feature 3: Mimics legitimate Kaspersky styling for deception

## Installation

### Requirements

- Text editor to create the file
- Browser for execution

### Install Commands

```bash
# Create file with content:
<html><body><iframe src="about:blank" style="opacity:0.5"></iframe><a href="#" style="position:absolute">Fake Warning</a></body></html>
# Customize src to target error page
```

## Basic Usage

```bash
# Open in browser: file:///path/to/certerror_clickjacking.html
```

### Common Options

N/A (static HTML)

## Examples

### Example 1: Basic Usage

Save as .html and open in Firefox; click fake link to trigger real override.

### Example 2: Advanced Usage

Modify iframe src dynamically via JS to target specific warnings.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Local HTML files with iframe to security domains
- JS/CSS anomalies in network traces

## Related Procedures


## Related Tools

- [[tools/Firefox]]

## References

- HackerOne Report: https://hackerone.com/reports/463695
