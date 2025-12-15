---
url: 'https://portswigger.net/burp/'
tags:
  - proxy
  - intercept
  - web-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.728Z'
id: e4b6fde1-e2ae-4f0a-8f1b-8ab10ad81d0f
validated: true
submitted: true
---
# Burp

**Status**: Unverified

## Overview

Burp Suite is a comprehensive toolkit for web application security testing, primarily used for intercepting, inspecting, and modifying HTTP/S traffic to identify vulnerabilities like open redirects.

## Description

Burp Suite, developed by PortSwigger, includes modules like Proxy, Repeater, and Intruder for manual and automated web pentesting. In this scenario, its Proxy tool captures and tampers with POST requests during file uploads, enabling exploitation of unvalidated parameters in applications like Greenhouse.io. It's widely used in offensive security for traffic manipulation without requiring code changes.

## Features

- Feature 1: HTTP proxy for intercepting requests and responses
- Feature 2: Request editor for modifying parameters like URLs
- Feature 3: CA certificate generation for HTTPS interception

## Installation

### Requirements

- Java 11 or later
- 4GB RAM recommended

### Install Commands

```bash
# Download from https://portswigger.net/burp/releases/download
# For community edition (free)
java -jar burpsuite_community_v2023.x.x.jar
```

## Basic Usage

```bash
java -jar burpsuite_community_v2023.x.x.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--no-update-check` | Disable update checks |

## Examples

### Example 1: Basic Usage

Launch Burp and configure proxy:

```bash
java -jar burpsuite_community.jar
```
Then in Proxy > Options, set listener to 127.0.0.1:8080.

### Example 2: Advanced Usage

Intercept and modify a request:

Set browser proxy, submit form, edit in Intercept tab, forward.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.002]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic on port 8080
- Presence of Burp CA certificate in browser trust store
- Anomalous request modifications in server logs

## Related Procedures


## Related Tools

- [[ZAP]]
- [[Wireshark]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
