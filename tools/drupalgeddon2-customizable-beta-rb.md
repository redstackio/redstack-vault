---
id: tool-004
url: 'https://github.com/dreadlocked/Drupalgeddon2'
tags:
  - exploit
  - rce
type: tool
verified: false
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.605Z'
validated: true
submitted: true
---
# drupalgeddon2-customizable-beta-rb

**Status**: Unverified

## Overview

A Ruby script exploiting CVE-2018-7600 for RCE in Drupal 7 via form API flaws.

## Description

Automates POST injections to /user/password and /file/ajax, executing arbitrary commands. Used for pentesting outdated CMS.

## Features

- Feature 1: Custom command execution
- Feature 2: Form targeting
- Feature 3: Version-specific exploits

## Installation

### Requirements

- Ruby and nokogiri

### Install Commands

```bash
# Clone from GitHub
```

## Basic Usage

```bash
ruby drupalgeddon2-customizable-beta.rb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u | Target URL |
| -c | Command |
| -v | Version |

## Examples

### Example 1: Basic Usage

```bash
ruby drupalgeddon2-customizable-beta.rb -u https://target/ -c id
```

### Example 2: Advanced Usage

```bash
ruby drupalgeddon2-customizable-beta.rb -u https://target/ -v 7 -c 'cat /etc/passwd' --form user/login
```

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

- HTTP POST anomalies to Drupal forms

## Related Procedures

- [[procedures/Execute-RCE-with-ID-Command]]

## Related Tools

- [[Related Tool: Metasploit]]

## References

- GitHub repo
