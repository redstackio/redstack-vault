---
id: 57214291-63f9-4203-a249-fa2264a9a81f-c
name: msf-set-socks-version
type: command
executor: msfconsole
data: set VERSION $_VERSION
output: null
created_at: '2023-04-06T03:56:22.631903+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - pivoting
  - socks
  - metasploit
verified: true
validated: true
---

# msf-set-socks-version

## Command

```msfconsole
set VERSION $_VERSION
```

## Description

Sets the SOCKS protocol version for the proxy module (4 or 4a for UDP support).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| VERSION $_VERSION | SOCKS version, e.g., 4a | Yes |

## Examples

### Basic Usage

```msfconsole
set VERSION 4a
```

## Expected Output

VERSION => 4a

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
