---
id: tool-004
url: 'https://github.com/Gallopsled/pwntools'
tags:
  - ctf
  - pwn
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.277Z'
validated: true
submitted: true
---
# pwntools

**Status**: Unverified

## Overview

Pwntools is a Python library for writing exploits, solving CTF challenges, and handling low-level binary and network interactions, used here for the FTP server to capture leaks.

## Description

It provides utilities for sockets, process management, and protocol handling, simplifying the FTP listener implementation.

## Features

- Feature 1: listen() for TCP sockets with easy connection handling
- Feature 2: recvuntil() for protocol parsing
- Feature 3: Integration with Python for rapid exploit development

## Installation

### Requirements

- Python 3

### Install Commands

```bash
pip3 install pwntools
```

## Basic Usage

```bash
python3 -c "from pwn import *; print('pwntools loaded')"
```

### Common Options

| Option | Description |
|--------|-------------|
| listen(port) | Start TCP listener on port |
| recvuntil(delims) | Receive until delimiter |

## Examples

### Example 1: Basic Usage

```bash
python3 -c "from pwn import *; l=listen(1337); c=l.wait_for_connection(); c.send(b'hello'); c.close()"
```

### Example 2: Advanced Usage

For FTP: listen(1337), respond to commands, print received data.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]] Python (via pwntools)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes importing pwn
- Network traffic from pwntools listeners

## Related Procedures

- [[procedures/Capture-Leaked-Data-via-FTP-Server]]

## Related Tools

- [[tools/python3]]

## References

- Official documentation: https://docs.pwntools.com/en/stable/
