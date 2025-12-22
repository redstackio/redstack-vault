---
id: 00000000-0000-0000-0000-000000000008
name: nextcloud_ssrf.py
type: tool
verified: false
created_at: '2023-12-14T00:00:00Z'
updated_at: '2025-12-14T04:08:48.744Z'
platforms:
  - Linux
  - Python
tags:
  - ssrf
  - nextcloud
  - poc
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/srpeWfQYz5LMrNA1QG93X4Mq?response-content-disposition=attachment%3B%20filename%3D%22nextcloud_ssrf.py%22%3B%20filename%2A%3DUTF-8%27%27nextcloud_ssrf.py&response-content-type=text%2Fx-python&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQUZB5WN6Z%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030920Z&X-Amz-Expires=3600&X-Amz-Security-Token=...
validated: true
submitted: true
---

# nextcloud_ssrf.py

**Status**: Unverified

## Overview

A Python proof-of-concept (POC) script for exploiting SSRF in Nextcloud's Calendar and DAV apps by automating authentication and injecting malicious WebCal URLs into calendar events.

## Description

The script uses the requests library to authenticate to Nextcloud via DAV API, constructs an ICS payload with the SSRF URL, and creates a subscription event. This triggers the background job to fetch the internal resource, demonstrating the IPv6 bypass. It's designed for security testing and requires Python 3 with requests installed.

## Features

- Feature 1: Basic authentication to Nextcloud using username/password
- Feature 2: ICS file generation with embedded WebCal URL
- Feature 3: DAV API interaction to create calendar events

## Installation

### Requirements

- Python 3.x
- requests library: `pip install requests`

### Install Commands

```bash
# Download from HackerOne attachment or GitHub equivalent
wget [URL] -O nextcloud_ssrf.py
pip install requests
```

## Basic Usage

```bash
python nextcloud_ssrf.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output for debugging |

## Examples

### Example 1: Basic Usage

```bash
python nextcloud_ssrf.py http://target/nextcloud admin "password" http://[::ffff:127.0.0.1]/secret
```

### Example 2: Advanced Usage

```bash
python nextcloud_ssrf.py -v https://nextcloud.example.com user "pass" http://[0:0:0:0:0:ffff:10.0.0.1]:80/internal
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to /remote.php/dav/calendars with POST requests containing ICS payloads
- Python process spawning requests to Nextcloud endpoints
- Anomalous calendar events with external WebCal URLs

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[curl]]

## References

- HackerOne Report #736867
- Nextcloud DAV API Documentation
