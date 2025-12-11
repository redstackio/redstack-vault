---
url: null
tags:
  - mitigation
  - software
type: tool
platforms:
  - Windows
description: Beta installer for UniFi Video with vulnerability fix
id: ccc02efa-cec1-4cb2-87a5-0ab8064763a5
created_at: '2025-12-11T06:10:22.806Z'
updated_at: '2025-12-11T06:10:22.806Z'
verified: false
validated: true
submitted: true
---
# unifi-video.Win7_x64.v3.10.7-beta.2_ee88ac.190725.1817.exe

**Status**: Unverified

## Overview

Beta version of UniFi Video software adding client certificate authentication to secure the API.

## Description

Used for testing mitigations against the EvoStream vulnerability, preventing unauthenticated access.

## Features

- Authentication enforcement
- Vulnerability patch
- Windows compatibility

## Installation

### Requirements

- Windows 7+ x64

### Install Commands

```bash
# Run the .exe installer
```

## Basic Usage

Install and restart services.

### Common Options

N/A (installer)

## Examples

### Example 1: Basic Usage

Double-click to install.

### Example 2: Advanced Usage

Test post-install with exploit attempts.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

N/A (defensive)

### Tactics

N/A

## Detection

N/A (legitimate software)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools



## References

- Ubiquiti support
