---
url: null
tags:
  - web-exploitation
  - proxy
  - interception
type: tool
platforms:
  - Web
  - Linux
  - Windows
  - macOS
description: >-
  Web vulnerability scanner and proxy tool for intercepting and modifying HTTP
  requests.
id: a0988cce-af4b-4109-80d4-4f7ec832ff4f
created_at: '2025-12-11T03:48:06.089Z'
updated_at: '2025-12-11T03:48:06.089Z'
verified: false
validated: true
submitted: true
---
# Burp Suite

**Status**: Unverified

## Overview

Burp Suite is a comprehensive platform for web application security testing, commonly used to intercept, analyze, and modify HTTP/S traffic between a browser and target application.

## Description

It includes tools like Proxy for traffic interception, Repeater for request manipulation, and Intruder for automated attacks. In offensive security, it's essential for discovering and exploiting vulnerabilities like improper access controls in web endpoints.

## Features

- Feature 1: HTTP request interception and modification
- Feature 2: Built-in vulnerability scanning
- Feature 3: Extensibility via BApp Store extensions

## Installation

### Requirements

- Java Runtime Environment (JRE)
- Compatible OS (Windows, Linux, macOS)

### Install Commands

```bash
# Download from official site and run the installer
```

## Basic Usage

```bash
java -jar burpsuite_community.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--project-file` | Load project file |

## Examples

### Example 1: Basic Usage

```bash
java -jar burpsuite_community.jar
```

### Example 2: Advanced Usage

```bash
java -jar burpsuite_pro.jar --collaborator-server
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Sniffing]]

### Tactics

- [[Initial Access]]
- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual proxy traffic or certificate pinning bypasses
- Detection method 2: Logs showing repeated requests to sensitive endpoints

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #zaproxy
- #mitmproxy

## References

- https://portswigger.net/burp
- Burp Suite documentation
