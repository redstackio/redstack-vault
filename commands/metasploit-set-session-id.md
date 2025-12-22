---
id: 8fb6186d-4b5a-4e9e-a1a0-0df0e9a27c27-part2
name: metasploit-set-session-id
type: command
executor: metasploit
data: set session $_SESSION_ID
output: |-
  msf6 exploit(windows/local/payload_inject) > set session 2
  session => 2
created_at: '2019-11-14T01:00:13.488117+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - metasploit
  - session-management
verified: true
validated: true
---

# Metasploit Set Session ID

## Command

```metasploit
set session $_SESSION_ID
```

## Description

Sets the target session ID for a Metasploit module, linking it to an existing backgrounded Meterpreter session for operations like payload injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SESSION_ID | ID of the backgrounded session (e.g., 2) | Yes |

## Examples

### Basic Usage

```metasploit
set session 2
```

Targets session 2 for the current module.

### Advanced Usage

Set multiple options: `set session 2; set LHOST 10.10.10.100`.

## Expected Output

```
msf6 exploit(windows/local/payload_inject) > set session 2
session => 2
```

Confirms the session is set.

## Related

- [[commands/metasploit-run-payload-inject]]
- [[procedures/upgrade-windows-meterpreter-x32-to-x64]]
