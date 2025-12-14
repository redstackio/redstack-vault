---
url: 'https://cors-anywhere.herokuapp.com/'
tags:
  - proxy
  - cors-bypass
type: tool
verified: false
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.886Z'
id: 0353d4ce-8702-429a-8335-af76646b4707
validated: true
submitted: true
---
# CORS-Anywhere-Proxy

**Status**: Unverified

## Overview

A public proxy service to bypass CORS restrictions in browser-based requests, prepended to target URLs in AJAX calls for cross-origin exploitation.

## Description

In CSRF attacks, this tool allows JavaScript from external sites to reach protected endpoints like analytics.mopub.com/login by acting as an intermediary, forwarding requests without origin checks.

## Features

- Temporary CORS header addition
- Request forwarding
- Simple URL prepending

## Installation

### Requirements

- Internet access

### Install Commands

No installation; use via URL.

## Basic Usage

Visit https://cors-anywhere.herokuapp.com/ to activate, then prepend to targets.

### Common Options

N/A

## Examples

### Example 1: Basic Usage

In JS: fetch('https://cors-anywhere.herokuapp.com/https://target.com')

### Example 2: Advanced Usage

For POST: Include headers and body as normal.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Requests from herokuapp.com IPs
- Unusual proxy headers

## Related Procedures


## Related Tools

- [[tools/Browser]]

## References

- GitHub repo: cors-anywhere
