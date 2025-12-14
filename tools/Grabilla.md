---
url: 'https://www.grabilla.com/'
tags:
  - screenshot
  - poc
type: tool
verified: false
platforms:
  - Windows
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.297Z'
id: a33d454b-c7bb-49fd-b0fe-fbf87ffa9519
validated: true
submitted: true
---
# Grabilla

**Status**: Unverified

## Overview

Grabilla is a lightweight screenshot capture tool used for quickly documenting web pages and interfaces during security testing, such as proving unclaimed subdomain status in vulnerability reports.

## Description

Grabilla allows users to capture full-page screenshots, annotate them, and share via links or files. In offensive security, it's ideal for PoC evidence without complex setups, supporting quick grabs of browser content like Zendesk claim pages.

## Features

- Feature 1: Full-screen or selected area capture
- Feature 2: Automatic upload and link generation
- Feature 3: Basic annotations and editing

## Installation

### Requirements

- Windows OS (primary support)
- Internet for uploads (optional)

### Install Commands

Download from official site; no CLI install needed.

```bash
# Download and run installer from https://www.grabilla.com/
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| Capture hotkey | Default PrtSc for full screen |
| Edit mode | Post-capture drawing tools |

## Examples

### Example 1: Basic Usage

Press hotkey to capture browser page showing vulnerability.

### Example 2: Advanced Usage

Capture, annotate with arrows pointing to claim message, then upload for sharing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to grabilla.com upload servers
- Local process 'grabilla.exe' running

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://www.grabilla.com/help
- Related resources: Screenshot tools in pentesting guides
