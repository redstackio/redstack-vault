---
id: tool-chrome-browser-001
url: 'https://www.google.com/chrome/'
tags:
  - browsing
  - testing
  - web-security
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.961Z'
validated: true
submitted: true
---
# Web-Browser-Chrome

**Status**: Unverified

## Overview

Google Chrome is a web browser used for accessing and interacting with web applications, pivotal in security testing for navigating sites, triggering vulnerabilities, and observing client-side behaviors like XSS execution.

## Description

Chrome supports extensions, devtools integration, and JavaScript execution, making it ideal for manual pentesting. In this context, it's used to maintain sessions, navigate to vulnerable pages, and perform UI interactions that reflect injected payloads.

## Features

- Feature 1: Session cookie management for authenticated testing
- Feature 2: UI automation via clicks and inputs for trigger simulation
- Feature 3: Integration with DevTools for real-time monitoring

## Installation

### Requirements

- Compatible OS (Windows, macOS, Linux)

### Install Commands

```bash
# Linux example
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

## Basic Usage

```bash
google-chrome https://www.yelp.com
```

### Common Options

| Option | Description |
|--------|-------------|
| --incognito | Private browsing |
| --user-data-dir=/path | Custom profile |
| --disable-web-security | Bypass CORS (testing only) |

## Examples

### Example 1: Basic Usage

Launch Chrome and navigate to https://www.yelp.com/profile_location.

### Example 2: Advanced Usage

```bash
google-chrome --user-data-dir=/tmp/chrome-session https://www.yelp.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- User-agent strings in logs identifying Chrome
- Frequent navigation patterns in web analytics

## Related Procedures


## Related Tools

- [[tools/Chrome-Developer-Tools]]

## References

- Official documentation: https://www.google.com/chrome/
- Related resources: Chrome for Developers
