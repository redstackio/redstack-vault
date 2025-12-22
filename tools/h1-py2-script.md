---
id: tool-h1-py2-script-001
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/000/112/672/.../h1-py2.py
tags:
  - custom-script
  - hackerone
  - monitoring
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.041Z'
validated: true
submitted: true
---
# h1-py2-script

**Status**: Unverified

## Overview

h1-py2.py is a custom Python 2 script for Windows designed to find the last known HackerOne report ID and monitor new submissions via polling the reports endpoint.

## Description

Tailored for the vulnerability, it uses requests to iterate IDs, detect length changes, and log timestamps. It's a proof-of-concept for real-time platform activity reconnaissance, with alternatives for Python 3.

## Features

- Feature 1: User-prompted starting ID
- Feature 2: Polling loop with 30s delays
- Feature 3: Timestamp logging on detections

## Installation

### Requirements

- Python 2.7 on Windows
- requests library

### Install Commands

```bash
pip install requests
# Download script from URL
curl -o h1-py2.py <URL>
```

## Basic Usage

```bash
python h1-py2.py
```

### Common Options

| Option | Description |
|--------|-------------|
| None | Interactive prompt for ID |

## Examples

### Example 1: Basic Usage

```bash
python h1-py2.py
# Follow prompts, then monitors
```

### Example 2: Advanced Usage

Run in background for continuous monitoring.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Specific request patterns to /reports/*.json
- Python 2 User-Agent in logs

## Related Procedures

- [[procedures/Log-and-Monitor-Submission-Activity]]

## Related Tools

- [[tools/h1-py3-script]]
- [[tools/python-requests]]

## References

- HackerOne report attachment
