---
url: 'https://github.com/websockets/wscat'
tags:
  - websocket
  - testing
  - socketio
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.820Z'
id: 7ec0eb23-ac16-4d8d-b067-0122f3aed086
validated: true
submitted: true
---
# wscat

**Status**: Unverified

## Overview

wscat is a command-line WebSocket client tool for testing and interacting with WebSocket servers, including Socket.IO endpoints, commonly used in security testing for vulnerabilities like XSS in real-time web applications.

## Description

wscat allows users to connect to WebSocket URLs, send messages, and receive responses interactively from the terminal. It's particularly useful for manual exploitation of WebSocket-based vulnerabilities, such as injecting payloads into Socket.IO events without needing a full browser environment. In offensive security, it's employed to simulate client-server interactions and probe for issues like reflected XSS in Node.js applications like Hyperledger Cactus.

## Features

- Feature 1: Interactive REPL for sending/receiving WebSocket messages
- Feature 2: Support for ws:// and wss:// protocols with TLS options
- Feature 3: Piping input/output for scripted testing and automation

## Installation

### Requirements

- Node.js (v10+)
- npm package manager

### Install Commands

```bash
npm install -g wscat
```

## Basic Usage

```bash
wscat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-c, --connect` | Connect to WebSocket URL |
| `-n, --no-check` | Skip TLS certificate validation |
| `-H, --header` | Add custom headers |

## Examples

### Example 1: Basic Usage

```bash
wscat -c ws://echo.websocket.org
```

Type messages and see them echoed back.

### Example 2: Advanced Usage

```bash
wscat -c ws://target:3000/socket.io/?EIO=4 -H "Authorization: Bearer token"
```

Connect with headers for authenticated endpoints.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing wscat user-agent or unusual WebSocket connections from CLI tools
- Process monitoring for 'wscat' executable on endpoints
- WebSocket traffic analysis for non-browser origins

## Related Procedures

- [[procedures/Exploit-Reflected-XSS-in-SocketIO-Handling]]

## Related Tools

- [[websocat]]
- [[Browser Developer Tools]]

## References

- Official documentation: https://github.com/websockets/wscat
- Related resources: Socket.IO protocol specs
