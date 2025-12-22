---
id: 82eb629f-8b84-40dd-91a3-0d7e8ece0348
name: meterpreter-autoroute-list-routes
type: command
executor: msfconsole
data: run autoroute -p
output: null
created_at: '2023-04-06T03:56:22.631951+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - pivoting
  - routing
  - meterpreter
verified: true
validated: true
---

# meterpreter-autoroute-list-routes

## Command

```msfconsole
run autoroute -p
```

## Description

Lists all active routes added by the autoroute module in the Meterpreter session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p | Print routes | No |

## Examples

### Basic Usage

```msfconsole
run autoroute -p
```

## Expected Output

[*] Active routes:
[*]   192.168.15.0/24 via session 1

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
