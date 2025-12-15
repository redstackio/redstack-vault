---
id: tool-uuid-001
url: 'https://portswigger.net/burp/documentation/desktop/tools/intruder'
tags:
  - web-proxy
  - fuzzing
  - enumeration
  - reconnaissance
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.348Z'
validated: true
submitted: true
---
# Burp-Suite-Intruder

**Status**: Unverified

## Overview

Burp Suite Intruder is a module within the Burp Suite web vulnerability scanner used for automated customized attacks, such as directory and parameter fuzzing, to discover hidden files or inputs in web applications.

## Description

Burp Suite Intruder excels in offensive security for tasks like directory enumeration on web servers. It intercepts HTTP requests, allows payload insertion at specified positions, and launches attacks against targets. In this context, it's used to fuzz paths on a PHP-based site to uncover exposed files like info.php, revealing server configs. Features include multiple attack types (Sniper, Battering Ram), payload sets (wordlists), and result analysis by response codes, lengths, or grep items.

## Features

- Feature 1: Payload positioning for precise fuzzing of URLs, headers, or bodies
- Feature 2: Built-in and custom wordlists for common directories/files
- Feature 3: Response analysis tools like Grep - Match/Extract for identifying content signatures

## Installation

### Requirements

- Java 11+ runtime
- 4GB+ RAM for smooth operation

### Install Commands

```bash
# Download from official site (Community Edition free)
# No install needed; run the JAR
java -jar burpsuite_community_v2023.x.x.jar
```

## Basic Usage

```bash
# Launch Burp Suite
java -jar burpsuite_community.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help (via GUI menu) |
| `--project-file=FILE` | Load/save project configurations |

## Examples

### Example 1: Basic Usage

Configure proxy in browser (127.0.0.1:8080), browse to target, intercept request, send to Intruder, set payload, and attack.

### Example 2: Advanced Usage

For directory fuzzing: Right-click request > Send to Intruder > Positions tab: Clear § around path > Add wordlist payload > Intruder tab: Start attack > Sort by length to find 200s.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of similar requests from one IP (e.g., /admin§, /config§)
- Anomalous User-Agent (Burp's default) in logs
- WAF alerts on fuzzing patterns or rapid 404s

## Related Procedures


## Related Tools

- [[tools/Dirbuster]]
- [[tools/Gobuster]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide on Directory Enumeration
