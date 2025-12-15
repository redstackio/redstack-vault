---
data: 'set lhost [your public ip]'
tags:
  - metasploit
  - callback
type: command
output: LHOST set
executor: msfconsole
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.138Z'
id: e9727283-670d-42ce-979d-6e34433ae61d
verified: false
validated: true
submitted: true
---
# msf-set-lhost-ip

## Command

```msf
set lhost [your public ip]
```

## Description

Configures the local host IP in Metasploit for the reverse connection from the Meterpreter payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| lhost | Attacker's public IP | Yes |

## Examples

### Basic Usage

```msf
set lhost 13.53.201.208
```

## Expected Output

'LHOST => 13.53.201.208'.

## Related

- [[commands/msf-set-payload-5]]
- [[procedures/Set-Up-Metasploit-Exploit-Server-for-Browser-RCE]]
