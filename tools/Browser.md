---
url: ''
tags:
  - web
  - poc
type: tool
platforms:
  - Web
description: >-
  Standard web browser used to access and execute web-based exploits like CORS
  PoCs.
id: a97c223b-04c1-4c6e-afad-684f9c0f4566
created_at: '2025-12-14T17:28:44.957Z'
updated_at: '2025-12-14T17:28:44.957Z'
verified: false
validated: true
submitted: true
---
# Browser

**Status**: Unverified

## Overview

A standard web browser (e.g., Chrome, Firefox) serves as the primary tool for loading HTML/JavaScript PoCs to test and exploit web vulnerabilities like CORS misconfigurations, enabling cross-origin requests and data exfiltration in security assessments.

## Description

Browsers enforce the same-origin policy but allow cross-origin requests when servers permit via CORS headers. In offensive security, they are used to simulate attacker scenarios by hosting local PoC files that fetch sensitive data from targets, as seen in enumerating WordPress user APIs.

## Features

- Feature 1: JavaScript execution for dynamic requests (XMLHttpRequest, Fetch API)
- Feature 2: Developer tools for inspecting network requests and CORS headers
- Feature 3: Local file loading for PoC testing without a server

## Installation

### Requirements

- Operating system with graphical interface (Windows, macOS, Linux)

### Install Commands

```bash
# Typically pre-installed; download from official sites
# e.g., For Chrome: wget https://dl.google.com/chrome/installer
```

## Basic Usage

```bash
# Open HTML PoC file
google-chrome poc.html
# Or Firefox: firefox poc.html
```

### Common Options

| Option | Description |
|--------|-------------|
| --disable-web-security | Disables CORS for testing (use cautiously) |
| --user-data-dir=/tmp/chrome | Isolated profile for security testing |

## Examples

### Example 1: Basic Usage

```bash
firefox poc.html
```
Load the file and observe the alert with fetched data.

### Example 2: Advanced Usage

```bash
google-chrome --disable-web-security --user-data-dir=/tmp/test poc.html
```
Bypasses CORS for local testing if needed.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[T1087.002]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser network logs showing cross-origin requests to sensitive endpoints
- Unusual JavaScript execution patterns in access logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp Suite]]
- [[Postman]]

## References

- Official browser documentation
- MDN Web Docs on CORS
