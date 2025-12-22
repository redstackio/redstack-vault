---
id: cmd-run-poc-server
data: python poc.py
tags:
  - ssh
  - poc
type: command
output: Server listening on port 22 for SSH connections.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.696Z'
verified: false
validated: true
submitted: true
---
# run-poc-server

## Command

```bash
python poc.py
```

## Description

Runs the Python PoC script to start a malicious SSH server that listens on port 22 and prepares crafted responses for exploiting PuTTY vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The script runs without arguments; customize source for payloads | No |

## Examples

### Basic Usage

```bash
python poc.py
```

### Advanced Usage

Edit poc.py to modify payloads, then:

```bash
python poc.py
```

## Expected Output

Server outputs: "Listening on 0.0.0.0:22" and awaits connections; logs interactions and payload sends.

## Related

- [[Related Procedure|procedures/Set-Up-Malicious-SSH-PoC-Server]]
