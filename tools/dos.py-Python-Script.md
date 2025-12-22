---
url: null
tags:
  - dos
  - automation
  - python
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Custom Python script for automating DoS attacks on API endpoints
id: c7199833-411d-4bed-9844-eaf4ed2c7675
created_at: '2025-12-14T17:32:01.627Z'
updated_at: '2025-12-14T17:32:01.627Z'
verified: false
validated: true
submitted: true
---
# dos.py-Python-Script

**Status**: Unverified

## Overview

This is a custom Python script designed to perform DoS attacks by sending continuous authenticated requests to unprotected API endpoints, such as those on the Semmle platform.

## Description

The script uses the requests library to loop through API calls with inserted session cookies and nonces. It targets internal endpoints without rate limits, causing server overload. Configuration involves editing the script to add auth details.

## Features

- Feature 1: Infinite loop for endless requests
- Feature 2: Support for GET/POST methods with custom headers
- Feature 3: Basic logging of request success/failure

## Installation

### Requirements

- Python 3.x
- requests library: pip install requests

### Install Commands

```bash
# No installation; save as dos.py and edit
pip install requests
```

## Basic Usage

```bash
python dos.py
```

### Common Options

| Option | Description |
|--------|-------------|
| `--cookie` | Specify cookie value (edit script) |
| `--nonce` | Specify nonce value (edit script) |

## Examples

### Example 1: Basic Usage

Edit dos.py with cookie/nonce, then: ```bash
python dos.py
```

### Example 2: Advanced Usage

Add delays or targets in script: Modify loop to include multiple endpoints.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]
- [[Endpoint Denial of Service]]

### Tactics

- [[Execution]]
- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of API requests from a single session
- Python process with requests library activity
- Log patterns of repeated endpoint hits

## Related Procedures

- [[procedures/Automate-Excessive-API-Requests-with-Python-Script]]

## Related Tools

- [[tools/Apache-Benchmark]]
- [[tools/Slowloris]]

## References

- Python requests docs: https://docs.python-requests.org
- Custom script based on HackerOne report
