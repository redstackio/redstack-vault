---
id: uuid-12
url: null
tags:
  - ruby
  - brute-force
  - custom-script
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.499Z'
validated: true
submitted: true
---
# InstagramBrandLoginBruteForce.rb

**Status**: Unverified

## Overview

Custom Ruby script for automating brute-force attacks on the WordPress login endpoint, testing password lists against a target email to achieve account takeover.

## Description

Built with Net::HTTP, the script sends POST requests to /wp-json/brc/v1/login/ with email/password combos, checking for success responses. Single-threaded by default, it exploits no protections for high-volume guessing.

## Features

- Feature 1: Loads passwords from txt file
- Feature 2: Configurable target email
- Feature 3: Logs successes and failures

## Installation

### Requirements

- Ruby 2.0+

### Install Commands

```bash
# Save as InstagramBrandLoginBruteForce.rb
# Edit line 7 for email
# Create passlist.txt
```

## Basic Usage

```bash
ruby InstagramBrandLoginBruteForce.rb
```

### Common Options

| Option | Description |
|--------|-------------|
| Line 7 | Set target email | Required |
| passlist.txt | Password file | Required |

## Examples

### Example 1: Basic Usage

```bash
ruby InstagramBrandLoginBruteForce.rb
```

### Example 2: Advanced Usage

Enhance with threading (modify script):

```bash
# Add threads=4 in script
ruby InstagramBrandLoginBruteForce.rb
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Guessing]] Brute Force: Password Guessing

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Repeated failed logins from single IP
- Sequential password attempts in logs
- No variation in user-agent

## Related Procedures

- [[procedures/Automated-Brute-Force-Login-with-Ruby-Script]]

## Related Tools

- [[tools/InstagramBrandEnumerationExploit.rb]]

## References

- Custom from HackerOne report #209008
