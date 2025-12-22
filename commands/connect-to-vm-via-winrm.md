---
type: command
executor: powershell
data: >-
  $password = ConvertTo-SecureString '<PASSWORD>' -AsPlainText -Force

  $creds = New-Object System.Management.Automation.PSCredential('username',
  $password)

  $sess = New-PSSession -ComputerName <VM-IP> -Credential $creds -SessionOption
  (New-PSSessionOption -ProxyAccessType NoProxyServer)

  Enter-PSSession $sess
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Cloud
  - Windows
tags:
  - azure
  - remote-access
verified: true
validated: true
---

# Connect to VM via WinRM

## Command

```powershell
$password = ConvertTo-SecureString '<PASSWORD>' -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential('username', $password)
$sess = New-PSSession -ComputerName <VM-IP> -Credential $creds -SessionOption (New-PSSessionOption -ProxyAccessType NoProxyServer)
Enter-PSSession $sess
```

## Description

Establishes a remote PowerShell session to an Azure VM over WinRM using provided credentials, enabling interactive command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <PASSWORD> | Plaintext password for the user | Yes |
| username | Local or domain username on the VM | Yes |
| <VM-IP> | Public or private IP of the VM | Yes |
| -ProxyAccessType NoProxyServer | Bypasses proxy for direct connection | No |

## Examples

### Basic Usage

```powershell
$password = ConvertTo-SecureString 'P@ssw0rd123!' -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential('user', $password)
$sess = New-PSSession -ComputerName 20.123.45.67 -Credential $creds
Enter-PSSession $sess
```

### Advanced Usage

With timeout:

```powershell
$sess = New-PSSession -ComputerName <VM-IP> -Credential $creds -SessionOption (New-PSSessionOption -OpenTimeout 60000)
```

## Expected Output

```
[20.123.45.67]: PS C:\Users\user\Documents>
```

Interactive PS prompt on the remote VM.

## Related

- [[procedures/azure-vm-runcommand-execution]]
- [[commands/get-public-ip-of-azure-vm]]
