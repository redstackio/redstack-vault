---
id: new-uuid-1
name: load-kiwi-extension
type: command
executor: meterpreter
data: load kiwi
output: null
created_at: '2023-04-06T03:56:04.748900+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - credentials
verified: true
validated: true
---

# load-kiwi-extension

## Command

```meterpreter
load kiwi
```

## Description

Loads the kiwi extension into an active Meterpreter session, enabling advanced credential dumping and Kerberos ticket manipulation capabilities based on Mimikatz functionality.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters needed; kiwi must be available in the Metasploit modules | Yes |

## Examples

### Basic Usage

```meterpreter
load kiwi
```

### Troubleshooting Usage

If load fails, ensure Metasploit is updated: use 'msfupdate' before starting the session.

## Expected Output

[*] Loading extension kiwi...
Kiwi (32-bit) extension loaded.
Successfully loaded kiwi extension!

## Related

- [[procedures/pass-the-golden-ticket-attack-using-meterpreter]]
- [[tools/kiwi-metasploit-extension]]
