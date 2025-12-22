---
id: a0f06bb0-4ebb-4a91-a513-5cb6a9a22e7b
name: create-pscredential-from-plaintext-password
type: command
executor: powershell
data: >-
  $pass = ConvertTo-SecureString '$_PASSWORD' -AsPlainText -Force

  $cred = New-Object System.Management.Automation.PSCredential
  ('$_DOMAIN\\$_USERNAME', $pass)
output: null
created_at: '2023-04-06T03:56:31.111678+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - powershell
  - credentials
verified: true
validated: true
---

# create-pscredential-from-plaintext-password

## Command

```powershell
$pass = ConvertTo-SecureString '$_PASSWORD' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ('$_DOMAIN\\$_USERNAME', $pass)
```

## Description

This PowerShell command sequence creates a PSCredential object from a plaintext password, first converting it to a SecureString for secure handling, then encapsulating it with a username. Use this in scripts for authenticating to remote Windows systems via WinRM without interactive prompts, ideal for automation in red team engagements.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PASSWORD | The plaintext password to secure (e.g., 'supersecurepassword') | Yes |
| $_DOMAIN | The domain name (e.g., 'CONTOSO') | Yes |
| $_USERNAME | The username (e.g., 'Administrator') | Yes |
| -AsPlainText | Treats input as plaintext despite security warnings | Built-in |
| -Force | Overrides security checks for plaintext conversion | Built-in |

## Examples

### Basic Usage

```powershell
$pass = ConvertTo-SecureString 'P@ssw0rd123' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ('CONTOSO\\Admin', $pass)
```

### Advanced Usage

Combine with remote execution:

```powershell
$pass = ConvertTo-SecureString 'P@ssw0rd123' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ('CONTOSO\\Admin', $pass)
Invoke-Command -ComputerName DC01 -Credential $cred -ScriptBlock { whoami }
```

## Expected Output

No direct output from the command itself. The $cred variable holds the PSCredential object. Verify with:

```powershell
$cred.UserName  # Outputs: CONTOSO\Admin
```

Successful creation allows seamless use in remoting cmdlets; failure results in a conversion or object instantiation error.
