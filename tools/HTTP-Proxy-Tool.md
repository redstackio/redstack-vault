---
url: 'https://portswigger.net/burp/documentation'
tags:
  - proxy
  - http-intercept
  - web
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-05T12:00:00Z'
updated_at: '2025-12-14T17:31:10.643Z'
id: 2672d0e4-aa9c-4a7b-823d-adfbbe34f96f
validated: true
submitted: true
---
# HTTP-Proxy-Tool

**Status**: Unverified

## Overview

HTTP Proxy Tool (e.g., Burp Suite Proxy) is used for intercepting, inspecting, and modifying HTTP/HTTPS traffic between a client (like a browser) and a server, commonly in security testing to analyze authentication mechanisms like Basic Auth in WebDAV.

## Description

This tool acts as a man-in-the-middle proxy, allowing capture of requests and responses. In offensive security, it's essential for observing headers such as Authorization in vulnerable setups like Nextcloud WebDAV, where credentials are exposed in Base64. Features include traffic interception, decoding, and replay.

## Features

- Feature 1: Real-time request/response interception and modification
- Feature 2: Built-in Base64 and other decoders for header analysis
- Feature 3: History logging for repeated traffic inspection

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher
- Administrative privileges for proxy setup

### Install Commands

```bash
# For Burp Suite Community (free version)
# Download from https://portswigger.net/burp/releases/download?product=community&type=Jar
java -jar burpsuite_community_v2023.x.x.jar
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
# Launch and configure proxy on default port 8080
java -jar burpsuite_community.jar
```
Set browser proxy to 127.0.0.1:8080 and intercept traffic.

### Example 2: Advanced Usage

```bash
# Use with CA certificate for HTTPS interception (install Burp CA in browser)
java -jar burpsuite_community.jar --config-file=proxy-config.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Discovery]] Discovery
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual proxy traffic on local ports (e.g., 8080) via netstat
- Detection method 2: Browser CA certificate mismatches or proxy settings alterations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Wireshark]]
- [[ZAP]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide on Proxy Usage
