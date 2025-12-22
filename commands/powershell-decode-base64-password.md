---
id: 1580aa58-d038-42e3-b46c-45a33b067022
name: powershell-decode-base64-password
type: command
executor: powershell
data: >-
  $encoded = "$_ENCODED";
  [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encoded))
output: null
created_at: '2023-04-06T03:56:29.080698+00:00'
updated_at: '2023-04-10T20:37:39.339735+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - decoding
verified: true
validated: true
---

# powershell-decode-base64-password

## Command

```powershell
$encoded = "$_ENCODED"; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encoded))
```

## Description

This PowerShell one-liner decodes a base64-encoded string, commonly used in Windows unattend files to reveal plaintext passwords. It uses .NET classes for native decoding without external dependencies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ENCODED | The base64-encoded string (e.g., from <Password> tag) | Yes |

## Examples

### Basic Usage

```powershell
$encoded = "U2VjcmV0U2VjdXJlUGFzc3dvcmQxMjM0Kgo="; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encoded))
```

Outputs: SecretSecurePassword1234*

### Advanced Usage

Decode from file input:

```powershell
$encoded = (Get-Content "C:\path\unattend.xml" | Select-String "<Password>(.*?)</Password>" | ForEach-Object { $_.Matches.Groups[1].Value }); [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encoded))
```

## Expected Output

The plaintext decoded string, for example:

```
SecretSecurePassword1234*
```

If invalid base64, it will throw a FormatException.

## Related

- [[procedures/windows-unattend-password-extraction]]
- [[commands/windows-cmd-search-unattend-files]]
