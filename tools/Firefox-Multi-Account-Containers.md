---
url: 'https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/'
tags:
  - browser
  - session-management
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.448Z'
id: 850a785b-2c99-48e6-8801-4a871e3e8324
validated: true
submitted: true
---
# Firefox-Multi-Account-Containers

**Status**: Unverified

## Overview

Browser extension for Firefox to isolate sessions in separate containers, preventing cookie interference in multi-session testing like PoC demos.

## Description

Allows creating color-coded containers for different identities, ideal for simulating attacker/victim sessions without logout issues in web vulnerability testing.

## Features

- Feature 1: Create unlimited isolated containers
- Feature 2: Assign tabs to specific containers
- Feature 3: Manage cookies per container

## Installation

### Requirements

- Firefox browser version 57+

### Install Commands

No CLI install; add via Firefox Add-ons store.

## Basic Usage

```bash
tool-name --help
```

Open Firefox, install extension, create new container via toolbar icon.

### Common Options

N/A (GUI-based)

## Examples

### Example 1: Basic Usage

Create 'Attacker' and 'Victim' containers, open site in each.

### Example 2: Advanced Usage

Assign dev tools to specific container for isolated debugging.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Manipulation]]

### Tactics

- [[Persistence]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser extension lists in forensics
- Multiple container profiles in Firefox storage

## Related Procedures

- [[procedures/Intercept-and-Identify-IDOR-in-Self-Endpoint]]
- [[procedures/Modify-Self-Request-to-Add-Attacker-Recovery-Email]]

## Related Tools

- [[Burp Suite]]
- [[Browser DevTools]]

## References

- Official documentation: https://support.mozilla.org/en-US/kb/containers
- Related resources: Firefox Add-ons page
