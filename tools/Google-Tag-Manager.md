---
url: 'https://tagmanager.google.com'
tags:
  - gtm
  - payload-hosting
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:16:37.504Z'
id: 555e55e0-2567-4be0-85ca-81a4e4728c3d
validated: true
submitted: true
---
# Google-Tag-Manager

**Status**: Unverified

## Overview

Google Tag Manager (GTM) is a free tag management platform that allows users to deploy and manage marketing tags, analytics, and custom HTML/JavaScript snippets on websites without modifying the code directly. In security testing, it's commonly used to host arbitrary HTML payloads for XSS exploitation, as it serves content via public endpoints.

## Description

GTM enables creation of containers that publish HTML, scripts, or tags triggered by events. For offensive use, attackers create containers with XSS payloads (e.g., img onerror handlers) and use the container ID to reference the content. In the redditmedia.com case, GTM hosts unsanitized HTML that executes JavaScript like cookie bombs when fetched by vulnerable endpoints.

## Features

- Feature 1: Container-based tag deployment for HTML/JS
- Feature 2: Preview and debug modes for testing payloads
- Feature 3: Publicly accessible publish URLs for external fetches

## Installation

### Requirements

- Google account
- Web browser

### Install Commands

No installation needed; access via web at https://tagmanager.google.com.

## Basic Usage

```bash
# No CLI; use web interface
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Web-based configuration |

## Examples

### Example 1: Basic Usage

Log in, create container, add Custom HTML tag with payload, publish.

### Example 2: Advanced Usage

Set triggers for specific pages; use variables for dynamic content.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous GTM container creations with suspicious HTML
- Traffic to gtm.google.com domains from vulnerable apps
- JavaScript execution traces in logs

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[Custom Script Host]]

## References

- Official documentation: https://support.google.com/tagmanager
- Related resources: HackerOne reports on GTM abuse
