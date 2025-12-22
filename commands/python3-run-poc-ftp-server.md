---
id: cmd-002
data: python3 server.py
tags:
  - network-listen
  - data-exfil
type: command
output: b'PASS AAAAAAAAAAAAAA\r\n' (or similar leaked data)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.303Z'
verified: false
validated: true
submitted: true
---
# python3-run-poc-ftp-server

## Command

```bash
python3 server.py
```

## Description

This command executes a Python script (server.py) using pwntools to start a minimal FTP server on port 1337, capturing leaked heap data from the libcurl exploit in the PASS command.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `server.py` | The Python script implementing the FTP listener with pwntools | Yes |

## Examples

### Basic Usage

```bash
python3 server.py
```

### Advanced Usage

Run with verbose logging if script supports:

```bash
python3 server.py --verbose
```

## Expected Output

Server output showing connection receipt and leaked PASS command, e.g., "Received PASS: b'PASS AAAAAAAAAAAAAA\r\n'", indicating heap over-read data.

## Related

- [[procedures/Capture-Leaked-Data-via-FTP-Server]]
