---
type: command
executor: meterpreter
data: load kiwi
output: null
platforms:
  - Windows
tags:
  - metasploit
  - kiwi
verified: true
validated: true
---

# meterpreter-load-kiwi

## Command

```meterpreter
load kiwi
```

## Description

Loads the Kiwi extension (Metasploit's Mimikatz integration) into the Meterpreter session for advanced credential access and Kerberos ticket manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Loads the extension | No |

## Examples

### Basic Usage

```meterpreter
load kiwi
```

## Expected Output

[*] Loading extension kiwi from /path/to/kiwi.dll
Loaded extension 'kiwi'

## Related

- [[procedures/Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]
- [[tools/Metasploit-Framework]]
