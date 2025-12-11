---
url: >-
  https://github.com/rapid7/metasploit-framework/pull/15007/files#diff-42ae645fcacbd90d93296471ac57e1d734544af7fb082efd607db0a29d197ac4R53
tags:
  - exploitation
  - reverse-shell
type: tool
platforms:
  - Linux
  - Windows
description: Exploitation framework for generating and serving payloads.
id: e7f2d37d-0c2e-46e4-8a23-cf9ebeec129a
created_at: '2025-12-11T03:47:47.760Z'
updated_at: '2025-12-11T03:47:47.760Z'
verified: false
validated: true
submitted: true
---
# Metasploit

**Status**: Unverified

## Overview

Metasploit is used to generate and serve Chrome exploit payloads, establishing Meterpreter sessions for full compromise in the Kibana RCE scenario.

## Description

It includes modules like chrome_simplifiedlowering_overflow for targeting vulnerable browsers, configured with targets, payloads, and listeners.

## Features

- Exploit modules: Pre-built exploits for vulnerabilities
- Payload generation: Reverse shells like Meterpreter
- Listener setup: Handle incoming connections

## Installation

### Requirements

- Ruby environment

### Install Commands

```bash
git clone https://github.com/rapid7/metasploit-framework
cd metasploit-framework
bundle install
```

## Basic Usage

```bash
msfconsole
```

### Common Options

| Option | Description |
|--------|-------------|
| `use` | Select module |
| `set` | Configure options |

## Examples

### Example 1: Basic Usage

```bash
use exploit/multi/browser/chrome_simplifiedlowering_overflow
```

### Example 2: Advanced Usage

```bash
set target 0
set payload 5
set lhost [ip]
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for msfconsole processes
- Network traffic to known exploit ports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/headless_shell]]

## References

- Metasploit GitHub
