---
id: tool-lookout-clickjacking-test-1195209
url: 'https://www.lookout.net/test/clickjack.html'
tags:
  - clickjacking
  - testing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.910Z'
validated: true
submitted: true
---
# Lookout-Clickjacking-Test

**Status**: Unverified

## Overview

The Lookout Clickjacking Test is a free, web-based tool designed for quickly assessing whether a website is vulnerable to clickjacking by attempting to load it within an iframe and overlaying interactive elements to simulate UI redressing attacks.

## Description

This browser-based tester provides an iframe environment where users can input a target URL to check for the presence of frame-busting protections. If the site loads, it indicates susceptibility to clickjacking, where attackers can create malicious pages that invisibly frame the victim site and trick users into clicking hidden elements, such as submit buttons for sensitive actions. Commonly used in penetration testing and vulnerability reports, like the Sifchain subdomain assessment, it requires no installation and works directly in modern browsers.

## Features

- Feature 1: Simple iframe embedding to test X-Frame-Options and CSP compliance.
- Feature 2: Built-in overlay simulation for visualizing click hijacking scenarios.
- Feature 3: Instant feedback on whether the site blocks framing.

## Installation

### Requirements

- A modern web browser (e.g., Chrome, Firefox).
- Internet access.

### Install Commands

No installation required; access via URL.

## Basic Usage

Visit https://www.lookout.net/test/clickjack.html and enter the target URL in the provided field.

### Common Options

| Option | Description |
|--------|-------------|
| Target URL Input | Field to specify the site to test for framing |
| Overlay Toggle | Enables/disables visual overlay for deception demo |

## Examples

### Example 1: Basic Usage

1. Navigate to https://www.lookout.net/test/clickjack.html.
2. Enter https://cryptoeconomics.sifchain.finance/#sif10jatqfd88m8s2uhtdtdl3txtayjtzsve2klyhh&type=lm.
3. Observe if it loads in the iframe.

### Example 2: Advanced Usage

Modify the page's source (via dev tools) to add CSS overlays:

```html
<iframe src="https://target.com" style="opacity: 0.5; position: absolute;"></iframe>
<div style="position: relative;">Fake Button</div>
```

This simulates tricking clicks onto hidden elements.

## Expected Output

Successful framing shows the target site loaded; failure displays an error or blank iframe due to protections.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing requests to lookout.net from testing environments.
- Browser dev tools traces of iframe src modifications.

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[OWASP ZAP]]

## References

- Official page: https://www.lookout.net/test/clickjack.html
- OWASP Clickjacking Cheat Sheet
