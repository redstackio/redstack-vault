---
id: cmd-uuid-1
name: create-windows-pscredential-object
type: command
executor: powershell
data: >-
  $Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force

  $Cred = New-Object -TypeName System.Management.Automation.PSCredential
  -Argument "$_DOMAIN\$_USER", $Pass
output: null
created_at: '2023-01-01T00:00:00Z'
updated_at: '2023-01-01T00:00:00Z'
platforms:
  - Windows
tags:
  - powershell
  - credentials
verified: true
validated: true
---

# create-windows-pscredential-object

## Command

```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```

## Description

This command creates a secure PSCredential object in PowerShell for authenticating to Active Directory operations, using domain credentials. It converts a plaintext password to a secure string and builds the credential for use with cmdlets like Set-DomainObject.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | The NetBIOS or FQDN of the domain (e.g., 'BANK') | Yes |
| $_USER | The username for authentication (e.g., 'admin') | Yes |
| $_PASSWORD | The plaintext password for the user | Yes |
| -AsPlainText | Converts string to secure string without prompting | Built-in |
| -Force | Suppresses confirmation prompts | Built-in |

## Examples

### Basic Usage

```powershell
$Pass = ConvertTo-SecureString -String "Password123" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "BANK\admin", $Pass
```

### Advanced Usage

Use in a script with error handling:

```powershell
try {
    $Pass = ConvertTo-SecureString -String "Password123" -AsPlainText -Force
    $Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "BANK\admin", $Pass
    Write-Output "Credential created successfully."
} catch {
    Write-Error "Failed to create credential: $_"
}
```

## Expected Output

No direct console output; the $Cred variable holds the PSCredential object. Verify with:

```powershell
$Cred.UserName
$Cred.Password  # Returns SecureString
```

Output example:

```
BANK\admin
System.Security.SecureString
```

## Related

- [[procedures/Add-SPN-to-Domain-User-and-Kerberoast-for-NTLMv2-Hash]]
- [[commands/powerview-add-spn-to-domain-user]]
