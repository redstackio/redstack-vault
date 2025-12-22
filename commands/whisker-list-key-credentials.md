---
id: ca98790e-0409-48db-809a-fc1e590d3400
name: whisker-list-key-credentials
type: command
executor: cmd
data: 'Whisker.exe list /target:$_TARGET_NAME'
output: null
created_at: '2023-04-06T03:56:06.261255+00:00'
updated_at: '2023-04-10T20:26:09.591812+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - key-credentials
verified: true
validated: true
---

# whisker-list-key-credentials

## Command

```cmd
Whisker.exe list /target:$_TARGET_NAME
```

## Description

Lists all msDS-KeyCredentialLink attribute entries for a target user or computer object in Active Directory using Whisker.exe. Use this to enumerate existing Windows Hello key credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /target:$_TARGET_NAME | SAM account name of the target (e.g., computername$ or username) | Yes |

## Examples

### Basic Usage

```cmd
Whisker.exe list /target:dc01$
```

### With Domain Context (if needed)

Whisker.exe may auto-detect domain; specify if issues arise.

## Expected Output

A formatted list of key credentials:

DeviceID: {guid}
Public Key: [base64 encoded]
Timestamp: [date]
...

Success if entries are returned; errors indicate permission issues.

## Related

- [[procedures/Shadow-Credentials-for-Windows-Hello]]
- [[tools/Whisker]]
