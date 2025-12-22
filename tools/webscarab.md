---
id: d059de37-cabd-4fbc-be8c-e6497a3eb2fc
type: tool
verified: true
created_at: '2019-08-28T21:17:25.727078+00:00'
updated_at: '2023-10-01T12:00:00Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - web-proxy
  - intercept
  - web-testing
  - owasp
url: 'https://owasp.org/www-project-webscarab/'
description: >-
  WebScarab is an open-source framework for analyzing HTTP(S) communications,
  serving as an intercepting proxy for web application security testing and
  debugging.
validated: true
---

# WebScarab

**Status**: Unverified

## Overview

WebScarab is a lightweight, open-source tool designed for testing and analyzing web applications by intercepting and modifying HTTP(S) traffic. It functions as a proxy, allowing security testers to inspect requests and responses, identify vulnerabilities like injection flaws or authentication issues, and debug application behavior. Commonly used in penetration testing for manual exploration of web apps, it's particularly useful for those seeking a free alternative to commercial tools like Burp Suite.

## Description

WebScarab records all communications between a browser and web server, enabling users to view, edit, and replay HTTP messages. It supports features like spidering for site mapping, fuzzing for input testing, and session handling for maintaining state. Developed by OWASP, it's Java-based, making it cross-platform, but note that it's somewhat dated and may require updates for modern TLS/HTTPS handling. Ideal for educational purposes, red teaming web apps, or identifying misconfigurations in HTTP-based services.

## Features

- **Proxy Interception**: Captures and modifies HTTP(S) requests/responses in real-time.
- **Spider Module**: Automatically crawls websites to map structure and discover endpoints.
- **Manual Request Editor**: Allows crafting custom HTTP requests for testing.
- **Fuzzer**: Tests inputs for vulnerabilities like XSS or SQLi.
- **Session Management**: Handles cookies, authentication tokens, and multi-step interactions.
- **Encoder/Decoder**: Built-in tools for Base64, URL encoding, and more.

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher.
- At least 512MB RAM for basic usage.

### Install Commands

On Kali Linux (pre-installed in older versions; for newer, download manually):

```bash
# Download the latest JAR from OWASP
wget https://github.com/OWASP/webscarab/releases/download/v2.1/WebScarab-2011-11-16.jar -O webscarab.jar
# Or clone the repo for source build
apt install default-jdk
git clone https://github.com/OWASP/webscarab.git
cd webscarab
ant dist
```

On Ubuntu:

```bash
apt update
apt install default-jre
wget https://github.com/OWASP/webscarab/releases/download/v2.1/WebScarab-2011-11-16.jar -O /opt/webscarab.jar
```

On Windows/macOS: Download the JAR from the official GitHub releases and run via `java -jar WebScarab.jar`.

## Basic Usage

```bash
java -jar webscarab.jar
```

This launches the GUI. Configure your browser to proxy through WebScarab (default: 127.0.0.1:8000).

### Common Options

| Option | Description |
|--------|-------------|
| `-proxy` | Start in proxy-only mode for interception. |
| `-spider` | Launch the spider module directly. |
| `-help` | Display available command-line options. |
| `-config file.properties` | Load custom configuration. |

## Examples

### Example 1: Basic Usage (Launch GUI)

```bash
java -jar /opt/webscarab.jar
```

Open the GUI, set up the proxy tab, and configure your browser to use localhost:8000 as proxy.

### Example 2: Advanced Usage (Proxy Mode)

```bash
java -jar webscarab.jar -proxy
```

Intercepts traffic without full GUI; useful for scripted testing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Java processes (e.g., `java -jar webscarab.jar`) on endpoints.
- Proxy traffic rerouting to localhost ports like 8000.
- Network logs showing intercepted/modified HTTP requests from testing tools.
- Presence of WebScarab JAR files in temporary directories.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]]
- [[tools/ZAP]]
- [[tools/Fiddler]]

## References

- Official OWASP Project: https://owasp.org/www-project-webscarab/
- GitHub Repository: https://github.com/OWASP/webscarab
- Documentation: https://webscarab.readthedocs.io/

*Last updated: 2023-10-01T12:00:00Z*
