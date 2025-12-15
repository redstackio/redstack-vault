---
data: python3 poc.py
tags:
  - exploit
  - poc
type: command
executor: bash
platforms:
  - Linux
id: 5d4989df-784f-4d26-bc6a-02003143c02b
created_at: '2025-12-14T17:28:28.346Z'
updated_at: '2025-12-14T17:28:28.346Z'
verified: false
validated: true
submitted: true
---
# python3-poc-py

## Command

```bash
python3 poc.py
```

## Description

Executes the Python script poc.py to start an exploit server for the GoldSrc buffer overflow, listening on 127.0.0.1 and sending crafted packets to trigger RCE upon Counter-Strike 1.6 client connection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `poc.py` | The Python script file implementing packet crafting and server logic | Yes |

## Examples

### Basic Usage

```bash
python3 poc.py
```

### Advanced Usage

```bash
python3 poc.py --port 27015 --host 127.0.0.1
```
(If script supports flags; base assumes default.)

## Expected Output

Server listens on 127.0.0.1, triggers xcalc popup when CS 1.6 client connects. Output includes: "Server started on 127.0.0.1:27015", "Client connected", "Packets sent", and confirmation of execution.

## Related

- [[Related Procedure|procedures/Run-PoC-Exploit-Server]]
