---
url: 'https://portswigger.net/burp/documentation/desktop/tools/intruder'
tags:
  - fuzzing
  - dos
  - web
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:01.878Z'
id: 98a258e7-4bcd-4b4d-977f-93eb3310fbad
validated: true
submitted: true
---
# Burp-Intruder

**Status**: Unverified

## Overview

Burp Intruder is a module within Burp Suite for automated customized attacks against web applications, commonly used to exploit vulnerabilities like rate limit bypasses by replaying requests en masse.

## Description

It allows sending HTTP requests repeatedly with variations, ideal for brute-force, fuzzing, or DoS simulations. In rate limit exploits, it replays form POSTs without limits to spam or overload servers.

## Features

- Feature 1: Multiple attack types (Sniper, Battering Ram, etc.)
- Feature 2: Payload generation and threading control
- Feature 3: Response analysis for success metrics

## Installation

### Requirements

- Burp Suite Community or Professional
- Java 8+

### Install Commands

```bash
# Included in Burp Suite; launch Burp and access via GUI
java -jar burpsuite_community.jar
```

## Basic Usage

In Burp GUI: Intercept > Send to Intruder > Configure > Start Attack.

### Common Options

| Option | Description |
|--------|-------------|
| Threads | Number of concurrent requests |
| Payloads | Data for insertion positions |

## Examples

### Example 1: Basic Usage

Replay a POST 100 times: Set no positions, iterations=100, start attack.

### Example 2: Advanced Usage

Fuzz email field: Mark §email§ position, load wordlist, launch Sniper attack.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Rapid successive requests from single IP
- Consistent payload patterns in logs

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]
- [[tools/ffuf]]

## References

- Official documentation: https://portswigger.net/burp/documentation/desktop/tools/intruder
- Related resources: PortSwigger Academy labs
