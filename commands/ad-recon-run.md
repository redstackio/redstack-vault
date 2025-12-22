---
type: command
executor: powershell
data: .\ADRecon.ps1 -DomainController $_DOMAIN_CONTROLLER -Credential $_CREDENTIAL
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - recon
  - active-directory
verified: true
validated: true
---

# ad-recon-run

## Command

```powershell
.\ADRecon.ps1 -DomainController $_DOMAIN_CONTROLLER -Credential $_CREDENTIAL
```

## Description

Runs the ADRecon PowerShell script to enumerate Active Directory objects like users, groups, and computers, exporting data for vulnerability analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN_CONTROLLER | Target domain controller FQDN or IP | Yes |
| $_CREDENTIAL | Domain credentials in format DOMAIN\user | Yes |

## Examples

### Basic Usage

```powershell
.\ADRecon.ps1 -DomainController dc01.example.com -Credential EXAMPLE\attacker
```

### Advanced Usage

Run with specific output path by modifying the script.

## Expected Output

Generates CSV files in the current directory, e.g.,

Users.csv: UserID,Name,PasswordLastSet,Enabled,...
Computers.csv: Computer,OperatingSystem,ServicePack,...

Success indicated by file creation without errors.

## Related

- [[tools/ADRecon]]
- [[procedures/Active-Directory-Assessment-and-Privilege-Escalation]]
