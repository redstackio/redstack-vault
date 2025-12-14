---
id: tool-002
url: 'https://portswigger.net/bappstore/...'
tags:
  - burp-extension
  - format-conversion
  - json
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.516Z'
validated: true
submitted: true
---
# Content-Type-Converter

**Status**: Unverified

## Overview

Content-Type Converter is a Burp Suite extension that allows quick transformation of HTTP request/response bodies between formats like form-encoded to JSON, useful for testing API endpoints that accept multiple content types.

## Description

Installed via Burp's BApp Store, this plugin adds right-click options in the HTTP editor to convert payloads, aiding in vulnerability exploitation like format confusion in web apps such as GitLab's reset feature.

## Features

- Feature 1: Convert between JSON, XML, form-urlencoded
- Feature 2: Automatic header updates (e.g., Content-Type)
- Feature 3: Integration with Burp's editor for seamless workflow

## Installation

### Requirements

- Burp Suite Professional or Community
- Internet access for BApp Store

### Install Commands

No CLI; in Burp: Extender > BApp Store > Search 'Content-Type Converter' > Install.

## Basic Usage

Right-click in HTTP editor > Extensions > Content-Type Converter > Convert to JSON.

### Common Options

| Option | Description |
|--------|-------------|
| Convert to JSON | Transform body to JSON |
| Convert to URL-encoded | Reverse transformation |

## Examples

### Example 1: Basic Usage

Intercept form POST, right-click body, convert to JSON.

### Example 2: Advanced Usage

After conversion, edit JSON, then forward.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Requests with mismatched Content-Type and body format
- Server logs showing JSON on form endpoints

## Related Procedures

- [[procedures/Intercept-and-Convert-Reset-Request-to-JSON]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: Burp BApp Store page
- Related resources: PortSwigger extensions guide
