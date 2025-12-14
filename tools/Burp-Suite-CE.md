---
id: tool-burp-ce-001
url: 'https://portswigger.net/burp/communitydownload'
tags:
  - proxy
  - interception
  - web-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:12.716Z'
validated: true
submitted: true
---
# Burp-Suite-CE

**Status**: Unverified

## Overview

Burp Suite Community Edition (CE) is a free web vulnerability scanner and proxy tool used for intercepting, inspecting, and modifying HTTP/S traffic during security assessments, ideal for discovering API flaws like unauthenticated updates in KYC processes.

## Description

Burp Suite CE provides core features for manual web app testing: proxy for traffic interception, Repeater for request modification/replay, and HTTP history for logging. In offensive operations, it's used to capture and tamper with requests, such as modifying JSON payloads in verification flows. Lacks automation in CE but sufficient for targeted exploits.

## Features

- Feature 1: Proxy interception and logging for passive/active analysis
- Feature 2: Repeater module for request editing and replay
- Feature 3: Intruder for basic fuzzing (limited in CE)

## Installation

### Requirements

- Java 11+ runtime
- 2GB+ RAM for smooth operation

### Install Commands

```bash
# Download and run (Linux/macOS/Windows via JAR)
java -jar burpsuite_community_v2023.x.x.jar
```

Or use package managers like brew: `brew install --cask burpsuite`

## Basic Usage

```bash
# Launch
java -jar burpsuite_community_v2023.x.x.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| Proxy Tab | Configure listeners and interception rules |
| Target Tab | View site map and scope |
| Repeater | Send requests for modification |

## Examples

### Example 1: Basic Usage

Launch Burp, configure browser proxy to 127.0.0.1:8080, browse target site to log requests in HTTP history.

### Example 2: Advanced Usage

Intercept a request, send to Repeater, modify body, and replay: e.g., change JSON in PATCH request and send to test API response.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Discovery]] Discovery
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing traffic to 127.0.0.1:8080 or unusual proxy chains
- Presence of Burp CA certificate in client trust stores
- Anomalous request patterns like repeated identical calls

## Related Procedures


## Related Tools

- [[Related Tool: OWASP ZAP]]
- [[Related Tool: Fiddler]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: PortSwigger Web Security Academy
