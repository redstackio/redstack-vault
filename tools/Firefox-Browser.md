---
id: tool-firefox
url: 'https://www.mozilla.org/en-US/firefox/new/'
tags:
  - browser
  - firefox
  - vulnerable-browser
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.007Z'
validated: true
submitted: true
---
# Firefox Browser

**Status**: Unverified

## Overview

Firefox is a web browser where the self-XSS in Imgur's beta upload is exploitable, and saved passwords can be read via form auto-fill in the attack context.

## Description

Version around 75.0 is targeted; allows clipboard API with permission and DOM XSS via unsanitized inputs. Used for testing the full chain as other browsers like Chrome resist the self-XSS.

## Features

- Feature 1: Saved password auto-fill in forms
- Feature 2: navigator.clipboard API support with prompts
- Feature 3: Vulnerable to specific DOM handling in Imgur upload

## Installation

### Requirements

- Compatible OS (Linux/Windows/macOS)

### Install Commands

```bash
# Download from official site or use package manager
sudo apt install firefox  # Ubuntu
brew install --cask firefox  # macOS
```

## Basic Usage

```bash
firefox https://attacker-site.com
```

### Common Options

| Option | Description |
|--------|-------------|
| --profile | Use specific profile |
| --no-remote | Allow multiple instances |

## Examples

### Example 1: Basic Usage

```bash
firefox
```
Open and navigate to malicious page.

### Example 2: Advanced Usage

```bash
firefox --profile /path/to/profile
```
Use profile with saved Imgur creds.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials from Web Browsers]] Credentials from Web Browsers
- [[JavaScript]] JavaScript

### Tactics

- [[Credential Access]] Credential Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Browser user-agent strings in logs
- Permission prompts for clipboard
- Anomalous form submissions

## Related Procedures

- [[procedures/perform-account-takeover-via-password-form-manipulation]]
- [[procedures/trigger-dom-based-self-xss-via-paste]]

## Related Tools

- [[tools/navigator-clipboard-api]]

## References

- Mozilla Firefox Documentation
- HackerOne Report #892289
