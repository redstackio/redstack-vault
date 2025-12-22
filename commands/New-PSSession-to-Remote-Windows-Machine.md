---
id: 37797ac4-3bd9-4c71-ae2c-343bac18f15d
name: New-PSSession-to-Remote-Windows-Machine
type: command
executor: powershell
data: |-
  $session = New-PSSession -ComputerName $_COMPUTER_NAME
  Enter-PSSession $session
output: null
created_at: '2023-01-12T07:48:43.751451+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - PowerShell-Remoting
  - remote-execution
verified: true
validated: true
---

# New-PSSession-to-Remote-Windows-Machine

## Command

```powershell
$session = New-PSSession -ComputerName $_COMPUTER_NAME
Enter-PSSession $session
```

## Description

Creates a new PowerShell session to a remote Windows machine and enters it for interactive execution, using implicit authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName $_COMPUTER_NAME | Target hostname or IP | Yes |

## Examples

### Basic Usage

```powershell
$session = New-PSSession -ComputerName TARGET-PC
Enter-PSSession $session
```

### Advanced Usage

```powershell
$session = New-PSSession -ComputerName TARGET-PC -Port 5986
Enter-PSSession $session
```
(Uses HTTPS port if configured.)

## Expected Output

Session creation:

```
Id Name            ComputerName    State         ConfigurationName
-- ----            ------------    -----         -----------------
2   WinRM1          TARGET-PC       Opened        Microsoft.PowerShell
```
Then enters remote prompt:

`[TARGET-PC]: PS C:\Users\Public\Documents> `

## Related

- [[commands/New-PSSession-to-Remote-Windows-Machine-With-Credentials]]
- [[procedures/Remote-Access-to-Windows-Machine-Using-Credentials]]
