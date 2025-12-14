---
url: ''
tags:
  - email
  - reset
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.216Z'
id: 58e8721a-ee70-40c5-916b-6fb6c5fba1d0
validated: true
submitted: true
---
# Email-Client

**Status**: Unverified

## Overview

Standard email clients (e.g., Thunderbird, Outlook, Gmail web) for receiving and acting on password reset links, critical for completing account takeover after email redirection.

## Description

Used to monitor inbox for reset emails, click links, and interact with reset forms. In attacks, ensures timely hijacking before victim notices changes.

## Features

- Feature 1: Real-time email reception and notifications
- Feature 2: Link handling and security warnings
- Feature 3: Search and filtering for specific subjects

## Installation

### Requirements

- Internet access and email account

### Install Commands

```bash
# For Thunderbird
sudo apt install thunderbird  # Linux
```

## Basic Usage

```bash
thunderbird
```

### Common Options

| Option | Description |
|--------|-------------|
| Inbox View | Check for reset emails |
| Open Link | Follow reset URL |

## Examples

### Example 1: Basic Usage

Open client, check inbox for "Password Reset" from app.

### Example 2: Advanced Usage

Use filters to alert on sender domain.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]] Phishing
- [[Account Manipulation]] Account Manipulation

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Multiple logins from email-linked accounts
- Unusual reset link clicks

## Related Procedures


## Related Tools


## References

- General email client docs
