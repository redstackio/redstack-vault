---
id: 343600f5-fe61-4572-88de-f22f97402962
type: command
executor: powershell
data: $Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
output: >-
  PS C:\Users\Bob > $Pass = ConvertTo-SecureString -String "secretpass"
  -AsPlainText -Force
created_at: '2020-03-13T23:31:09.273542+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - authentication
  - powershell
  - credentials
verified: true
validated: true
---

# Create Windows Secure String

## Command

```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
```

## Description

This command converts a plaintext password into a SecureString object in PowerShell, which encrypts the password in memory to prevent exposure. It is a foundational step for creating secure credential objects used in authentication scenarios, such as remote command execution or service access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PASSWORD | The plaintext password to convert (e.g., "P@ssw0rd123") | Yes |
| -AsPlainText | Treats the input string as plaintext rather than prompting for secure input | Yes |
| -Force | Suppresses confirmation prompts for the plaintext conversion | Yes |

## Examples

### Basic Usage

```powershell
$Pass = ConvertTo-SecureString -String "secretpass" -AsPlainText -Force
```

### Usage with Domain Password

```powershell
$Pass = ConvertTo-SecureString -String "DomainP@ss123" -AsPlainText -Force
```

## Expected Output

No direct output is produced; the command succeeds silently, and the $Pass variable holds the SecureString object. To verify, you can check the type with `$Pass.GetType().Name`, which should return "SecureString".

## Related

- [[Related Procedure|procedures/create-windows-pscredential-object]]
