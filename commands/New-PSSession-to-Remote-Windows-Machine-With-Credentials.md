---
id: 2b6e9a4f-985e-4c9f-9bf5-71b0e88a9830
name: New-PSSession-to-Remote-Windows-Machine-With-Credentials
type: command
executor: powershell
data: >-
  $password = ConvertTo-SecureString $_PASSWORD -AsPlainText -Force

  $cred = New-Object System.Management.Automation.PSCredential ($_USERNAME,
  $password)

  $session = New-PSSession -ComputerName $_COMPUTER_NAME -Credential $cred

  Enter-PSSession $session
output: null
created_at: '2023-01-12T19:33:20.917690+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - PowerShell-Remoting
  - remote-execution
  - credentials
verified: true
validated: true
---

# New-PSSession-to-Remote-Windows-Machine-With-Credentials

## Command

```powershell
$password = ConvertTo-SecureString $_PASSWORD -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ($_USERNAME, $password)
$session = New-PSSession -ComputerName $_COMPUTER_NAME -Credential $cred
Enter-PSSession $session
```

## Description

Establishes a PowerShell remote session with provided credentials, converting the password to a secure string for safe handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Username for authentication | Yes |
| $_PASSWORD | Password (converted to secure string) | Yes |
| -ComputerName $_COMPUTER_NAME | Target machine | Yes |
| -Credential $cred | PSCredential object | Yes |

## Examples

### Basic Usage

```powershell
$password = ConvertTo-SecureString 'Pass123' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ('Administrator', $password)
$session = New-PSSession -ComputerName TARGET-PC -Credential $cred
Enter-PSSession $session
```

### Advanced Usage

```powershell
# For domain user
$cred = New-Object System.Management.Automation.PSCredential ('DOMAIN\user', $password)
$session = New-PSSession -ComputerName TARGET-PC -Credential $cred -UseSSL
```
(Enables SSL.)

## Expected Output

Session info:

```
Id Name            ComputerName    State         ConfigurationName
-- ----            ------------    -----         -----------------
3   WinRM2          TARGET-PC       Opened        Microsoft.PowerShell
```
Remote prompt: `[TARGET-PC]: PS C:\> `

## Related

- [[commands/New-PSSession-to-Remote-Windows-Machine]]
- [[procedures/Remote-Access-to-Windows-Machine-Using-Credentials]]
