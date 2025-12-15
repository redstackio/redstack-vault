---
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/lawafgj3ghtqfg37s0zep44nfe7f?response-content-disposition=attachment%3B%20filename%3D%22generate-payload.py%22%3B%20filename%2A%3DUTF-8%27%27generate-payload.py&response-content-type=text%2Fx-python&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQSRV3EVNB%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T095708Z&X-Amz-Expires=3600&X-Amz-Security-Token=...&X-Amz-SignedHeaders=host&X-Amz-Signature=14ef58f693d2475b2a07bc3c9434477b4ecf05025b09ce81716d9691600f2d7a
tags:
  - payload-generation
  - dos
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-12-14T10:00:00Z'
updated_at: '2025-12-14T17:26:48.471Z'
id: 4465c4df-454a-460a-a48f-a1e831938c82
validated: true
submitted: true
---
# generate-payload.py

**Status**: Unverified

## Overview

A Python script designed to generate a large JSON payload for testing size limits in Mattermost Playbooks, specifically creating a 50MB run_summary_template to enable DoS exploitation.

## Description

This tool crafts a JSON file mimicking a playbook creation request but with an excessively large string in the run_summary_template field (50,000,000 characters). It's used in offensive security to demonstrate uncontrolled resource consumption vulnerabilities in web applications like Mattermost.

## Features

- Feature 1: Generates precisely sized strings (e.g., 50MB) for payload inflation
- Feature 2: Structures output as valid JSON for API compatibility
- Feature 3: Customizable size via script parameters (if modified)

## Installation

### Requirements

- Python 3.x
- No additional libraries needed (uses built-in json and string modules)

### Install Commands

```bash
# Download the script from the provided URL
wget "<URL>" -O generate-payload.py
chmod +x generate-payload.py
```

## Basic Usage

```bash
python generate-payload.py
```

### Common Options

| Option | Description |
|--------|-------------|
| No options by default | Generates fixed 50MB payload |
| Modify script for size | Edit character count variable |

## Examples

### Example 1: Basic Usage

```bash
python generate-payload.py
```

This creates 'payload.json' with oversized run_summary_template.

### Example 2: Advanced Usage

Edit the script to change size:

```python
# In script: size = 50000000  # Change to desired bytes
python generate-payload.py
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for large file generations in temp directories
- Detect Python scripts creating oversized JSON files
- Alert on 50MB+ payloads in API logs

## Related Procedures

- [[procedures/Generate-Oversized-Playbook-Payload]]

## Related Tools


## References

- HackerOne Report #1685979
- Mattermost Playbooks API Documentation
