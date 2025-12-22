---
url: null
tags:
  - automation
  - api-scripting
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Custom Python script to automate interactions with Snapchat's API, including
  logout and login requests.
id: 9d1a7644-3967-4e61-973e-4cdd2c7cbbdd
created_at: '2025-12-11T06:10:40.159Z'
updated_at: '2025-12-11T06:10:40.159Z'
verified: false
validated: true
submitted: true
---
# Python Script for Snapchat API Automation

**Status**: Unverified

## Overview

A custom Python script designed to automate the exploitation of Snapchat's OTP vulnerability by sending manipulated API requests.

## Description

The script uses libraries like requests to perform the logout request with arbitrary user_id and subsequent login with the obtained token. It's useful for demonstrating and testing the vulnerability in a scripted manner.

## Features

- Feature 1: Manipulate user_id in logout requests
- Feature 2: Automate OTP extraction and login
- Feature 3: Handle authentication headers

## Installation

### Requirements

- Python 3.x
- requests library

### Install Commands

```bash
pip install requests
```

## Basic Usage

```bash
python script.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --user_id | Victim's user_id |
| --username | Victim's username |

## Examples

### Example 1: Basic Usage

```bash
python script.py --user_id victim_id --username victim_user
```

### Example 2: Advanced Usage

```bash
python script.py --token stolen_token --device_id device
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]
- [[Use Alternate Authentication Material]]

### Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Script execution logs
- Detection method 2: API access from scripted clients

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]]

## References

- Custom script based on HackerOne report
