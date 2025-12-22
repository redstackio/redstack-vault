---
id: 57214291-63f9-4203-a249-fa2264a9a81f-b
name: msf-set-socks-srvport
type: command
executor: msfconsole
data: set SRVPORT $_PORT
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

# msf-set-socks-srvport

## Command

```msfconsole
set SRVPORT $_PORT
```

## Description

Sets the server port for the SOCKS proxy module in Metasploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| SRVPORT $_PORT | Port to listen on, e.g., 9090 | Yes |

## Examples

### Basic Usage

```msfconsole
set SRVPORT 9090
```

## Expected Output

SRVPORT => 9090

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
