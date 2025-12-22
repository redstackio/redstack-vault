---
id: 57214291-63f9-4203-a249-fa2264a9a81f-a
name: msf-use-socks-proxy-module
type: command
executor: msfconsole
data: use auxiliary/server/socks_proxy
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

# msf-use-socks-proxy-module

## Command

```msfconsole
use auxiliary/server/socks_proxy
```

## Description

Loads the SOCKS proxy server module in Metasploit for setting up a proxy through the pivot session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Loads the module | No |

## Examples

### Basic Usage

```msfconsole
use auxiliary/server/socks_proxy
```

## Expected Output

[*] Module loaded: auxiliary/server/socks_proxy

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
