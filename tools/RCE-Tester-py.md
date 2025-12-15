---
url: null
tags:
  - scripting
  - rce-testing
  - dos
type: tool
verified: false
platforms:
  - Linux
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.023Z'
id: 42720562-381c-4787-839b-82d1c65a016d
validated: true
submitted: true
---
# RCE-Tester.py

**Status**: Unverified

## Overview

Python script for simulating API requests to test RCE payloads via crafted image data in the saveImage.php endpoint and performing DoS with repeated large file uploads using the DDOS() function.

## Description

The script crafts malicious image streams (e.g., embedding PHP code), sends POST requests to reverb.twitter.com, and automates DoS attacks. It handles base64 encoding for payloads and loops for resource exhaustion, targeting the unauthenticated file upload vulnerability.

## Features

- Feature 1: Generate crafted image payloads with PHP code
- Feature 2: Send HTTP POST requests with traversal parameters
- Feature 3: DDOS function for repeated large uploads

## Installation

### Requirements

- Python 3.x
- requests library: pip install requests

### Install Commands

```bash
pip install requests
```

## Basic Usage

```bash
python RCE-Tester.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -u, --url | Target URL (default: https://reverb.twitter.com/api/actions/saveImage.php) |
| -f, --filename | Filename parameter |
| -e, --extension | Extension (e.g., php) |
| -p, --payload | Malicious image payload |

## Examples

### Example 1: Basic Usage

```bash
python RCE-Tester.py --url https://reverb.twitter.com/api/actions/saveImage.php --filename /../../shell --extension php --payload "<?php system('id'); ?>"
```

### Example 2: Advanced Usage

DoS mode:

```bash
python RCE-Tester.py --ddos --count 100 --size 1MB
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]] PHP
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Tactics

- [[Execution]] Execution
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of POST requests to saveImage.php in access logs
- Unusual image data sizes or patterns
- Python process with requests library hitting the endpoint

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[curl]]

## References

- Custom script from HackerOne report #191884
