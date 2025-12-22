---
id: 33b8eb9c-23c1-41e9-985c-91ef2aa9a700
name: seatbelt-remote-checks
type: command
executor: cmd
data: >-
  Seatbelt.exe -group=remote -computername=dc.theshire.local
  -username=THESHIRE\sam -password="yum \"po-ta-toes\""
output: null
created_at: '2023-04-06T03:56:28.514179+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
platforms:
  - Windows
tags:
  - remote
  - enumeration
verified: true
validated: true
---

# seatbelt-remote-checks

## Command

```cmd
Seatbelt.exe -group=remote -computername=dc.theshire.local -username=THESHIRE\sam -password="yum \"po-ta-toes\"" 
```

## Description

Performs remote security checks on a target machine using provided credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -group=remote | Focuses on remote-accessible checks | Yes |
| -computername | Target hostname or IP | Yes |
| -username | Domain\user for auth | Yes |
| -password | Password for the user | Yes |

## Examples

### Basic Usage

```cmd
Seatbelt.exe -group=remote -computername=TARGET -username=DOMAIN\user -password="pass"
```

## Expected Output

Remote findings like "Remote: SMB Signing Disabled - Risk of Relay Attacks".

## Related

- [[commands/seatbelt-all-full-checks]]
- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
