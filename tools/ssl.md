---
url: 'https://docs.python.org/3/library/ssl.html'
tags:
  - tls
  - python-module
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.976Z'
id: 755b09c6-db3d-4a44-9f07-b5122d8caa9e
validated: true
submitted: true
---
# ssl

**Status**: Unverified

## Overview

ssl is a Python module providing SSL/TLS wrapper for sockets, used to secure the http.server with certificates and enable ALPN for HTTP/2.

## Description

Loads cert chains, wraps sockets with PROTOCOL_TLS_SERVER, and sets ALPN protocols for protocol negotiation in the PoC server.

## Features

- Feature 1: Cert chain loading
- Feature 2: Socket wrapping
- Feature 3: ALPN support

## Installation

### Requirements

- Python 3 standard library (requires OpenSSL)

### Install Commands

```bash
# Built-in
```

## Basic Usage

```python
import ssl
context = ssl.create_default_context()
```

### Common Options

| Option | Description |
|--------|-------------|
| `PROTOCOL_TLS_SERVER` | Server mode |
| `load_cert_chain` | Load cert/key |
| `set_alpn_protocols` | Set protocols |

## Examples

### Example 1: Basic Usage

```python
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')
```

### Example 2: Advanced Usage

```python
context.set_alpn_protocols(['h2', 'http/1.1'])
sock = context.wrap_socket(sock, server_side=True)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Python imports of ssl module in server scripts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/python3]]

## References

- Official documentation: https://docs.python.org/3/library/ssl.html
