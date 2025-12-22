---
url: >-
  https://chromewebstore.google.com/detail/cookie-manager-plus/fhkajaliakkbdjolbpjmbeghmhnlipjh
tags:
  - browser-extension
  - cookie-management
type: tool
verified: false
platforms:
  - Web
  - Chrome
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.444Z'
id: 72f6fc1a-b830-4cc5-a424-cb5b7d2cb7ac
validated: true
submitted: true
---
# Cookies-Manager-Plus

**Status**: Unverified

## Overview

Cookies Manager+ is a Chrome extension for managing, clearing, and importing cookies, useful for testing session cleanup and hijacking in web vulnerability assessments.

## Description

This extension allows selective deletion or bulk management of cookies per domain, aiding in simulating post-logout states or reinjecting stolen data. It's lightweight and focuses on privacy and testing, commonly used in scenarios like OAuth session flaws on platforms like MicroPurchase.

## Features

- Feature 1: Domain-specific cookie filtering and deletion
- Feature 2: Backup and restore functionality for session testing
- Feature 3: Search and export options for quick analysis

## Installation

### Requirements

- Google Chrome browser

### Install Commands

Install via Chrome Web Store; no CLI.

## Basic Usage

Activate on the site and select cookies to clear or import.

### Common Options

| Option | Description |
|--------|-------------|
| Clear All | Remove all cookies for domain |
| Import | Load from file |

## Examples

### Example 1: Basic Usage

After logout, use to clear micropurchase.18f.gov cookies.

### Example 2: Advanced Usage

Import extracted cookies to test hijack.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Extension in browser extensions list
- Detection method 2: Frequent cookie clear/import events

## Related Procedures


## Related Tools

- [[tools/EditThisCookie]]
- [[tools/Burp-Suite]]

## References

- Official documentation: Chrome Web Store
- Related resources: Cookie management best practices
