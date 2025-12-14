---
id: tool-att-text-to-web-16696
url: 'https://www.att.com/support/'
tags:
  - sms-interception
  - telecom
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.384Z'
validated: true
submitted: true
---
# ATT-Text-to-Web

**Status**: Unverified

## Overview

ATT Text to Web is a telecom service feature allowing users to view SMS messages online via a web portal, intended for convenience but exploitable for intercepting authentication codes.

## Description

This web-based service syncs phone SMS to an online dashboard, accessible after login. In security testing, it's abused post-account compromise to monitor 2FA messages in real-time. It supports viewing historical and live texts but lacks strong session controls, making it vulnerable to unauthorized feature enabling.

## Features

- Feature 1: Real-time SMS viewing on web
- Feature 2: Integration with call forwarding for voice codes
- Feature 3: Mobile app companion for access

## Installation

### Requirements

- Active ATT account
- Web browser access

### Install Commands

```bash
# No installation; access via https://www.att.com/my/
```

## Basic Usage

Log in to ATT portal and navigate to messaging section.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Web-based, no CLI options |

## Examples

### Example 1: Basic Usage

Enable Text to Web in account settings to start viewing SMS.

### Example 2: Advanced Usage

Combine with call forwarding to capture all authentication traffic.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Account login alerts from unfamiliar IPs
- Sudden enabling of web SMS features
- Anomalous SMS viewing patterns in logs

## Related Procedures


## Related Tools

- [[Verizon Message+]]
- [[T-Mobile DIGITS]]

## References

- Official documentation: https://www.att.com/support/article/wireless/KM1008728/
- Related resources: Telecom security guidelines
