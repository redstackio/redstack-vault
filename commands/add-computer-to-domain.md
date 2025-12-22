---
id: 0a31cea8-b444-4f75-9ad6-3e08a265f16e
name: Add-Computer-to-Domain
type: command
executor: powershell
data: Add-Computer -DomainName $_DOMAIN_NAME -Credential $_CREDENTIAL -Restart
output: null
created_at: '2023-04-06T03:56:03.096135+00:00'
updated_at: '2023-04-10T20:26:11.555942+00:00'
platforms:
  - Windows
tags:
  - powershell
  - domain
verified: true
validated: true
---

# Add-Computer-to-Domain

## Command

```powershell
Add-Computer -DomainName $_DOMAIN_NAME -Credential $_CREDENTIAL -Restart
```

## Description

This command adds the local computer to a domain or moves it between domains/workgroups, useful in JEA-constrained sessions for delegated domain management tasks without full admin access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -DomainName | The name of the domain to join (e.g., 'example.com') | Yes |
| -Credential | PSCredential object for domain admin (use Get-Credential) | Yes |
| -Restart | Automatically restart the computer after joining | No |
| -WorkgroupName | Alternative for workgroup (if not joining domain) | No |

## Examples

### Basic Usage

```powershell
Add-Computer -DomainName 'contoso.com' -Credential (Get-Credential)
```

### Advanced Usage

```powershell
Add-Computer -DomainName 'contoso.com' -Credential $cred -OUPath 'OU=Computers,DC=contoso,DC=com' -Restart
```

## Expected Output

Computer 'WORKSTATION01' was added to the domain 'contoso.com' successfully. The computer will be restarted.

## Related

- [[procedures/implement-jea-to-limit-powershell-cmdlet-usage]]
