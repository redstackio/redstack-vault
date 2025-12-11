---
url: null
tags:
  - email
  - xss
type: tool
platforms:
  - Mac
  - Windows
description: Client for sending plaintext emails with payloads
id: ef3267fa-51ed-47e9-ab10-c0d96bfc2c6c
created_at: '2025-12-11T06:10:22.463Z'
updated_at: '2025-12-11T06:10:22.463Z'
verified: false
validated: true
submitted: true
---
# Email Client

**Status**: Unverified

## Overview

Email client set to plaintext mode for sending HTML/JS payloads to exploit XSS on files.slack.com.

## Description

Sends emails stored as text/html without filtering, enabling XSS when uploaded to Slack.

## Features

- Plaintext mode: Avoid HTML stripping.
- Attachment support: For payloads.

## Installation

### Requirements

- macOS Mail or similar.

### Install Commands

```bash
# Built-in on OS
```

## Basic Usage

```bash
# CMD+SHIFT+T for plaintext
```

### Common Options

N/A

## Examples

### Example 1: Basic Usage

```bash
# Send email with HTML payload
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious email uploads to Slack.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/HTTP-Proxy]]

## References

- Apple Mail docs
