---
id: tool-mailapp-001
name: Mail.app
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.751Z'
platforms:
  - macOS
tags:
  - email-client
  - delivery-vector
url: 'https://support.apple.com/guide/mail/welcome/mac'
validated: true
submitted: true
---

# Mail.app

**Status**: Unverified

## Overview

Mail.app is macOS's native email client, used in this exploit as an alternative vector to deliver malicious chrome:// URLs for drag-and-drop into Brave, bypassing the need for shortcut files.

## Description

Built into macOS, Mail.app handles email composition and link rendering, allowing easy DnD of URLs to other apps like browsers. In security testing, it's leveraged for social engineering deliveries where direct file attachments are restricted. No configuration needed beyond email setup.

## Features

- Feature 1: Native link handling with DnD support
- Feature 2: Integration with macOS Finder for seamless interactions
- Feature 3: Rich text emails for embedding malicious links

## Installation

### Requirements

- macOS (pre-installed)

### Install Commands

```bash
# Already installed; update via System Update
softwareupdate --install --all
```

## Basic Usage

```bash
open -a Mail
```

### Common Options

N/A (GUI app)

## Examples

### Example 1: Basic Usage

Open Mail.app and compose new message with link.

### Example 2: Advanced Usage

Send HTML email with embedded chrome:// link for DnD.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]] Phishing
- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Email logs for suspicious URLs (chrome:// schemes)
- Activity monitoring for DnD from Mail to browser

## Related Procedures


## Related Tools

- [[tools/Node.js]]

## References

- Official documentation: https://support.apple.com/guide/mail/
- Related resources: macOS security guides on app interactions
