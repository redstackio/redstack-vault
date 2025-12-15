---
url: 'https://testingsubdomain.000webhostapp.com/stripo.php'
tags:
  - php
  - redirect
  - server
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:36.185Z'
id: 80c34f5f-947b-4400-9885-fc97437ff9d7
validated: true
submitted: true
---
# PHP Redirector Script

**Status**: Unverified

## Overview

A simple PHP script that issues a 307 Temporary Redirect to preserve POST requests, used in CSRF chains to forward forged requests to vulnerable endpoints.

## Description

Hosted on free platforms, this script takes parameters like userid and redirects while maintaining method and body, essential for bypassing CSRF in JSON APIs.

## Features

- Feature 1: 307 status for method preservation
- Feature 2: Parameterized target URL
- Feature 3: Lightweight, no dependencies

## Installation

### Requirements

- PHP-enabled web host
- Basic file upload access

### Install Commands

Upload PHP file via FTP or panel.

## Basic Usage

Access script URL with query params.

### Common Options

| Option | Description |
|--------|-------------|
| userid | Target user ID |

## Examples

### Example 1: Basic Usage

Visit: https://testingsubdomain.000webhostapp.com/stripo.php?userid=123

### Example 2: Advanced Usage

With POST body preserved via client.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- 307 redirects from unknown domains
- Unusual POST forwards
- PHP execution logs

## Related Procedures


## Related Tools

- [[tools/Adobe-Flash]]

## References

- PHP header() documentation
