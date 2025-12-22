---
type: command
executor: meterpreter
data: mimikatz_command -f version
output: null
platforms:
  - Windows
tags:
  - mimikatz
  - credential-access
verified: true
validated: true
---

# mimikatz-version

## Command

```meterpreter
mimikatz_command -f version
```

## Description

Displays the version and build information of the loaded Mimikatz extension in Meterpreter, useful for verifying compatibility and functionality before dumping credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f version | Specifies the version module | Yes |

## Examples

### Basic Usage

```meterpreter
mimikatz_command -f version
```

## Expected Output

mimikatz # version
RPC Server : mimikatz 2.2.0 (x64) built on Jan 10 2020
... (build details and modules listed)

## Related

- [[procedures/Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]
- [[commands/meterpreter-load-mimikatz]]
