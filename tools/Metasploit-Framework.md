---
url: >-
  https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/rails_secret_deserialization.rb
tags:
  - exploit
  - rce
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.908Z'
id: 38fced69-1e94-4c26-8c71-c87e2bb768dd
validated: true
submitted: true
---
# Metasploit-Framework

**Status**: Unverified

## Overview

Metasploit Framework is a penetration testing platform with modules for exploiting vulnerabilities, including Rails secret deserialization for RCE via crafted session cookies.

## Description

It provides msfconsole for loading, configuring, and executing exploits. The rails_secret_deserialization module was patched here to handle specific cookie formats, injecting Ruby objects for code execution. Used for web app RCE in offensive ops.

## Features

- Feature 1: Modular exploits with payloads like reverse shells
- Feature 2: Configuration options for targets and secrets
- Feature 3: Integration with handlers for shell management

## Installation

### Requirements

- Ruby 2.7+
- PostgreSQL (optional)

### Install Commands

```bash
# On Kali/Debian
sudo apt update && sudo apt install metasploit-framework
```

## Basic Usage

```bash
msfconsole --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -q | Quiet mode |
| -x | Execute command |

## Examples

### Example 1: Basic Usage

```bash
msfconsole
use exploit/multi/http/rails_secret_deserialization
```

### Example 2: Advanced Usage

Patch as described, then set options and exploit.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Command-Line Interface]] Command and Scripting Interpreter

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- msfconsole processes on endpoints
- Outbound connections to attacker handlers
- Suspicious HTTP requests with large cookies

## Related Procedures

- [[procedures/Configure-and-Execute-Rails-Deserialization-Exploit]]

## Related Tools

- [[Burp Suite]]
- [[Cobalt Strike]]

## References

- Official: https://metasploit.com
- Module: https://github.com/rapid7/metasploit-framework
