---
url: null
tags:
  - scanning
  - manual-testing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.971Z'
id: e78eddbc-9f43-4c3b-8da3-645722ea2ee0
validated: true
submitted: true
---
# Custom Scan Rules for Phabricator

**Status**: Unverified

## Overview

Custom scan rules are tailored configurations for vulnerability scanners or manual testing frameworks to identify issues like authentication bypasses in Phabricator, combining automated code analysis with targeted manual verification.

## Description

These rules focus on Phabricator's codebase, checking for re-authentication gaps in features like email management. Used in offensive security to replicate and confirm vulnerabilities reported in bug bounties, such as HackerOne #139965. Ideal for web app pentesting where manual exploration uncovers logic flaws.

## Features

- Feature 1: Automated endpoint fuzzing for auth checks
- Feature 2: Integration with manual browser testing
- Feature 3: Custom payloads for session-based exploits

## Installation

### Requirements

- Access to Phabricator source or running instance
- Basic scripting knowledge (e.g., Python for rules)

### Install Commands

```bash
# Clone Phabricator repo for analysis
git clone https://github.com/phacility/phabricator.git
# Set up custom rules in scanner config (e.g., Semgrep or similar)
semgrep --config custom_phabricator_rules.yaml
```

## Basic Usage

```bash
scanner --rules phabricator_auth_bypass --target phabricator_url
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output for manual verification |

## Examples

### Example 1: Basic Usage

```bash
semgrep --config phabricator_email.yaml /path/to/phabricator
```

### Example 2: Advanced Usage

```bash
scanner --rules auth_bypass --manual-test --url https://target.phabricator.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]
- [[Account Manipulation]]

### Tactics

- [[Initial Access]]
- [[Defense Evasion]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual code scans on Phabricator repos
- Manual testing logs showing session manipulations
- Network traffic to auth endpoints

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[ZAP Proxy]]

## References

- Phabricator documentation
- HackerOne Report #139965
