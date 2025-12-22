---
type: command
executor: cobalt-strike-beacon
data: 'ssh [target:port] [user] [pass]'
output: null
created_at: '2023-04-06T03:56:16.358332+00:00'
updated_at: '2023-04-10T20:36:20.029042+00:00'
platforms:
  - Windows
  - Linux
tags:
  - cobalt-strike
  - ssh
  - lateral-movement
verified: true
validated: true
---

# cobalt-strike-beacon-ssh-password-auth

## Command

```cobalt-strike-beacon
ssh $_TARGET $_PORT $_USERNAME $_PASSWORD
```

## Description

This command, executed from within a Cobalt Strike beacon console, spawns an SSH client to connect to a remote target using password authentication. It enables lateral movement or persistence by establishing an encrypted SSH session from the compromised host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | IP address or hostname of the SSH server (e.g., 192.168.1.100) | Yes |
| $_PORT | SSH port (default 22, optional if standard) | No |
| $_USERNAME | Username for authentication | Yes |
| $_PASSWORD | Password for the user | Yes |

## Examples

### Basic Usage

```cobalt-strike-beacon
ssh 192.168.1.100:22 admin password123
```

### Advanced Usage

```cobalt-strike-beacon
ssh internal-server.internal:2222 serviceuser secretpass
```

## Expected Output

Successful connection: "Spawning SSH client... Connected to 192.168.1.100. Last login: ..." followed by a shell prompt. Failure: "Authentication failed (Permission denied)" or connection timeout.

## Related

- [[commands/cobalt-strike-beacon-ssh-key-auth]]
- [[procedures/Deploy-SSH-Beacon-via-Cobalt-Strike]]
