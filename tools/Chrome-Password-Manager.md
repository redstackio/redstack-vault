---
url: 'chrome://password-manager/passwords'
tags:
  - credential-management
  - autofill
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.574Z'
id: 012ba0f9-2ce8-47c4-9bba-d0eb9b4a109a
validated: true
submitted: true
---
# Chrome-Password-Manager

**Status**: Unverified

## Overview

Chrome's built-in password manager for storing, autofilling, and managing site credentials, useful in security testing to simulate user-saved logins for demonstrating autofill-based credential theft.

## Description

Accessed via chrome://password-manager/passwords, it allows adding, editing, and deleting saved passwords. In attacks, it autofills forms on matching domains, enabling leakage when forms submit externally due to CSP gaps. Alternatives include browser extensions or other managers like Firefox's.

## Features

- Feature 1: Automatic form filling for username/password fields
- Feature 2: Domain-specific credential storage
- Feature 3: Export/import options for testing

## Installation

### Requirements

- Google Chrome browser

### Install Commands

Built-in; no install needed.

## Basic Usage

Navigate to chrome://password-manager/passwords and add entry.

### Common Options

| Option | Description |
|--------|-------------|
| Add | Create new credential entry |
| Edit | Modify existing passwords |
| Settings > Autofill | Toggle autofill on/off |

## Examples

### Example 1: Basic Usage

Go to chrome://password-manager/passwords, add site https://portswigger.net with user/pass.

### Example 2: Advanced Usage

Disable autofill temporarily via chrome://settings/passwords for controlled testing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Keychain]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser autofill events in client-side analytics
- Unexpected credential fills on non-login forms
- Password manager access logs if extended

## Related Procedures

- [[procedures/Save-Credentials-for-Autofill-Leak]]
- [[procedures/Inject-Form-for-Credential-Submission]]

## Related Tools

- [[tools/Browser-Developer-Tools]]

## References

- Official documentation: https://support.google.com/chrome/answer/95606
- Related resources: Browser security guides on autofill risks
