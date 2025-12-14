---
id: tool-email-client-macos
url: ''
tags:
  - email
  - xss
type: tool
verified: false
platforms:
  - Mac
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.094Z'
validated: true
submitted: true
---
# Email-Client-macOS

**Status**: Unverified

## Overview

macOS default Mail app or similar clients send emails in plaintext mode to upload unfiltered HTML to Slack integrations for stored XSS.

## Description

Enables sending HTML payloads without rendering, stored as text/html on files.slack.com.

## Features

- Feature 1: Plaintext composition (CMD+SHIFT+T)
- Feature 2: Attachment handling
- Feature 3: Integration with Slack email addresses

## Installation

### Requirements

- macOS

### Install Commands

Pre-installed.

## Basic Usage

Open Mail, new message.

### Common Options

| Option | Description |
|--------|-------------|

## Examples

### Example 1: Basic Usage

Compose plaintext email with <script>alert(1)</script> to slack-email@team.slack.com.

### Example 2: Advanced Usage

Include full RCE JS.

## MITRE ATT&CK Mapping

### Techniques

- [[T1566.001]] Spearphishing Attachment

### Tactics

- [[Initial Access]] Initial Access

## Detection

- Monitor email uploads for HTML content.

## Related Procedures


## Related Tools

- [[tools/HTTP-Proxy]]

## References

- Apple Mail docs
