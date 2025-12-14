---
id: tool-google-lens-001
url: 'https://lens.google/'
tags:
  - qr-code
  - scanner
type: tool
verified: false
platforms:
  - Android
  - iOS
  - Mobile
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:34.832Z'
configuration: Default mobile app integration
validated: true
submitted: true
---
# Google-Lens

**Status**: Unverified

## Overview

Google Lens is a visual search tool with QR code scanning capabilities that previews URLs before opening, serving as a safer alternative for testing malicious QR codes without auto-redirects.

## Description

Integrated into Google apps, Lens scans QR codes and displays link previews with a 'Go to site' option, preventing automatic exploitation. Useful for verification in security assessments. Mobile-focused; no install for basic use on Android.

## Features

- Feature 1: QR code decoding with URL preview
- Feature 2: Visual search integration
- Feature 3: Cross-app sharing

## Installation

### Requirements

- Google app or standalone on mobile

### Install Commands

Install via app store if not pre-installed.

## Basic Usage

Open Google app, tap Lens icon, scan QR.

### Common Options

| Option | Description |
|--------|-------------|
| Scan | Camera activation for QR |
| Preview | Displays URL before action |

## Examples

### Example 1: Basic Usage

Scan QR; view URL preview.

### Example 2: Advanced Usage

Copy previewed URL for manual verification.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- None (defensive use)

### Tactics


## Detection

Indicators and methods for detecting this tool's usage:

- App usage logs for safe scanning patterns

## Related Procedures


## Related Tools

- [[tools/Brave-Browser]]

## References

- Official site: https://lens.google/
