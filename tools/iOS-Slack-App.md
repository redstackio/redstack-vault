---
url: 'https://apps.apple.com/us/app/slack/id803453959'
tags:
  - mobile
  - ios
  - exploit
type: tool
platforms:
  - iOS
description: >-
  Slack mobile app for iOS exploited due to SOP weaknesses for local file access
  via XSS
id: 26700c36-2a05-474a-b2b4-04530c63f634
created_at: '2025-12-13T23:55:38.154Z'
updated_at: '2025-12-13T23:55:38.154Z'
verified: false
validated: true
submitted: true
---
# iOS-Slack-App

**Status**: Unverified

## Overview

The official Slack iOS app is targeted for XSS exploitation, lacking SOP enforcement, allowing javascript: payloads to load external scripts and read local files.

## Description

In editing mode, clicked links execute without origin checks, enabling file disclosure like /etc/passwd.

## Features

- Feature 1: Real-time post editing
- Feature 2: Markdown support
- Feature 3: Link handling (vulnerable to js URIs)

## Installation

### Requirements

- iOS device

### Install Commands

```bash
# App Store install
```

## Basic Usage

Open app, navigate to post, edit.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Mobile app, no CLI |

## Examples

### Example 1: Basic Usage

Edit a post and click inserted link.

### Example 2: Advanced Usage

Use for file reading payloads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- App logs for JS execution
- File access anomalies

## Related Procedures


## Related Tools

- [[Related Tool: Google Chrome]]

## References

- Slack App Store page
