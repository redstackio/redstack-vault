---
id: 123e4567-e89b-12d3-a456-426614174005
name: videoLeak-php
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.184Z'
platforms:
  - Web
tags:
  - poc
  - vimeo
  - authorization-bypass
url: 'http://opnsec.com/vimeo/vl/videoLeak.php'
validated: true
submitted: true
---

# videoLeak-php

**Status**: Unverified

## Overview

videoLeak.php is a proof-of-concept PHP script that automates the Vimeo private video disclosure vulnerability by sending requests to the share endpoint, extracting the secret token, and loading the video player config for demonstration.

## Description

This tool targets the authorization bypass in Vimeo's share endpoint, performing the full chain: AJAX request, token extraction, config fetch, and player embed. It's designed for security researchers to validate the vuln on private videos. Runs on PHP-enabled servers and requires basic auth for access.

## Features

- Feature 1: Automates AJAX request to leak token
- Feature 2: Parses response for secret parameter
- Feature 3: Fetches and displays video config/player

## Installation

### Requirements

- PHP 5+ environment
- Web server (e.g., Apache)
- Access to the hosted script URL

### Install Commands

No installation needed; access via URL. For local: Download and host on PHP server.

```bash
# wget http://opnsec.com/vimeo/vl/videoLeak.php
# php -S localhost:8000
```

## Basic Usage

Access the script URL with video ID:

http://opnsec.com/vimeo/vl/videoLeak.php?video=[VIDEO_ID]

### Common Options

| Option | Description |
|--------|-------------|
| video=[VIDEO_ID] | Target private video ID | 

## Examples

### Example 1: Basic Usage

Browse to: http://opnsec.com/vimeo/vl/videoLeak.php?video=123456789

### Example 2: Advanced Usage

The script handles auth internally; provide credentials if prompted (username: vimeo, password: aS3cr3tP4$$wrD7854123).

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- HTTP requests to /videoLeak.php endpoints
- Unusual auth attempts with hardcoded credentials
- Patterns of config fetches post-share errors

## Related Procedures


## Related Tools


## References

- HackerOne Report #137502
- Original POC hosting

