---
data: python -m SimpleHTTPServer 8000
tags:
  - hosting
type: command
executor: bash
platforms:
  - Linux
id: db4a33d2-f054-4ac6-8b5f-ca234ed48a39
created_at: '2025-12-11T03:47:47.786Z'
updated_at: '2025-12-11T03:47:47.786Z'
verified: false
validated: true
submitted: true
---
# python-simplehttpserver

## Command

```bash
python -m SimpleHTTPServer 8000
```

## Description

Starts a simple HTTP server on port 8000 serving the current directory, used to host the malicious HTML file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m SimpleHTTPServer` | Module to run | Yes |
| `8000` | Port number | Yes |

## Examples

### Basic Usage

```bash
python -m SimpleHTTPServer 8000
```

## Expected Output

Starts serving files on port 8000.

## Related

- [[procedures/Host-Malicious-HTML-for-RCE]]
- [[commands/headless-shell-exploit]]
