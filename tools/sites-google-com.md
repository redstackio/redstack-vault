---
url: 'https://sites.google.com'
tags:
  - hosting
  - phishing
  - web
type: tool
platforms:
  - Web
description: >-
  Google Sites platform for hosting static HTML pages, used in this attack to
  deploy malicious clickjacking PoCs without advanced server setup.
id: 0757d256-87f2-4787-8f82-2ddf6333243e
created_at: '2025-12-14T17:28:05.376Z'
updated_at: '2025-12-14T17:28:05.376Z'
verified: false
validated: true
submitted: true
---
# sites-google-com

**Status**: Unverified

## Overview

Google Sites is a free website builder for creating and hosting simple static pages, often abused in red teaming to host phishing or PoC attack pages due to its ease of use and lack of strict content moderation.

## Description

Attackers use Google Sites to quickly deploy HTML-based exploits like clickjacking pages, embedding iframes and scripts without needing custom domains or servers. Pages can be shared via links for social engineering, with basic customization for disguising malicious intent.

## Features

- Feature 1: Drag-and-drop HTML embedding and publishing
- Feature 2: Public or restricted access sharing
- Feature 3: Integration with Google Drive for file uploads

## Installation

### Requirements

- Google account
- Web browser

### Install Commands

No installation; access via browser at https://sites.google.com.

## Basic Usage

Create a new site, add HTML embed, and publish.

### Common Options

| Option | Description |
|--------|-------------|
| Public Visibility | Share link without authentication |
| Embed Code | Insert custom HTML/JS |
| Theme | Basic styling to mimic legit sites |

## Examples

### Example 1: Basic Usage

Log in, create site, embed HTML iframe, publish, and share URL.

### Example 2: Advanced Usage

Upload PoC HTML to a page, set to public, and use in phishing emails with custom title like "App Dev Test".

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]
- [[T1566.001]]

### Tactics

- [[Initial Access]]
- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Scan for Google Sites URLs in phishing reports
- Monitor employee clicks to sites.google.com domains
- Use threat intel feeds for known malicious site IDs

## Related Procedures


## Related Tools

- [[GitHub Pages]]
- [[Netlify]]

## References

- Official documentation: https://support.google.com/sites/
- Related resources: Phishing awareness guides
