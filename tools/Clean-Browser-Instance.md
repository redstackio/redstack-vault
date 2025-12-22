---
url: ''
tags:
  - testing
  - sandbox
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.882Z'
id: e2f1947f-f217-44dc-91cc-cab07a0d2228
validated: true
submitted: true
---
# Clean-Browser-Instance

**Status**: Unverified

## Overview

A virgin state browser instance (e.g., incognito mode or containerized browser) used to test attack chains without interference from cookies, sessions, or prior logins.

## Description

This setup simulates a fresh user environment to observe full redirect sequences, randomization, and behaviors like JS automation in the Twitter/Google attack without cached data influencing results.

## Features

- Feature 1: Isolated sessions without persistent storage
- Feature 2: No cookies or local storage
- Feature 3: Easy reset for repeated tests

## Installation

### Requirements

- Modern browser (Chrome, Firefox)

### Install Commands

No install; use built-in features.

```bash
# Launch incognito Chrome
google-chrome --incognito
```

## Basic Usage

```bash
# N/A - Browser launch
```

### Common Options

| Option | Description |
|--------|-------------|
| --incognito | Private browsing mode |
| --disable-extensions | No extensions |

## Examples

### Example 1: Basic Usage

Launch clean Chrome:

```bash
google-chrome --incognito --disable-extensions
```

### Example 2: Advanced Usage

Test redirect chain:

Navigate to malicious DM link in clean instance to follow full path without logins.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Audio Capture]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser flags in user-agent
- Lack of session cookies in traffic

## Related Procedures


## Related Tools

- [[tools/Firefox-Container]]
- [[tools/Burp-Suite]]

## References

- Official documentation: Browser privacy modes
- Related resources: Secure testing practices
