---
url: 'https://tempmail.org/'
tags:
  - email
  - disposable
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.134Z'
id: 9ca6f4ca-8dd3-4334-8756-e649ebd541c6
validated: true
submitted: true
---
# tempmail

**Status**: Unverified

## Overview

Tempmail is an online service for generating temporary, disposable email addresses, commonly used in security testing to receive one-time notifications like password resets without exposing real accounts.

## Description

It provides instant email generation and inbox access via web interface, with addresses expiring after a short period. Ideal for CSRF follow-ups involving email hijacking in web app attacks. No installation needed; browser-based.

## Features

- Feature 1: Instant disposable email creation
- Feature 2: Real-time inbox viewing without registration
- Feature 3: Auto-expiration for privacy

## Installation

### Requirements

- Web browser

### Install Commands

No installation; access via URL.

## Basic Usage

Visit https://tempmail.org/ and generate an address.

### Common Options

| Option | Description |
|--------|-------------|
| Generate | Create new email |
| Refresh | Update inbox |

## Examples

### Example 1: Basic Usage

Navigate to site, copy generated email like voyan61996@jrvps.com, use in attack, then check inbox for incoming mail.

### Example 2: Advanced Usage

Use in script to automate checks, but primarily manual for quick tests.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Traffic to known temp mail domains
- Disposable emails in app logs
- Rapid account changes followed by resets

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official site: https://tempmail.org/
- Alternatives: 10minutemail.com
