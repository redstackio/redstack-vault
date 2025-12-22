---
type: command
executor: bash
data: sudo ./teamserver $_TEAMSERVER_IP "$_PASSWORD" $_C2_PROFILE
output: null
created_at: '2023-04-06T03:56:16.220752+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - c2
  - cobalt-strike
  - execution
verified: true
validated: true
---

# start-cobalt-strike-teamserver

## Command

```bash
sudo ./teamserver $_TEAMSERVER_IP "$_PASSWORD" $_C2_PROFILE
```

## Description

Starts the Cobalt Strike Team Server, binding to a specified IP and protecting access with a password; optionally loads a malleable C2 profile for customized traffic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_TEAMSERVER_IP` | IP address for the server to bind to (e.g., 10.10.10.10) | Yes |
| `$_PASSWORD` | Password for client authentication | Yes |
| `$_C2_PROFILE` | Path to malleable C2 profile file (optional) | No |

## Examples

### Basic Usage

```bash
sudo ./teamserver 10.10.10.10 "strongpass"
```

### With C2 Profile

```bash
sudo ./teamserver 10.10.10.10 "strongpass" ./profile.cna
```

## Expected Output

[Team Server] Started on 10.10.10.10:50050
Waiting for clients...

## Related

- [[commands/start-cobalt-strike-client]]
- [[procedures/Cobalt-Strike-Team-Server-Installation-and-Execution]]
