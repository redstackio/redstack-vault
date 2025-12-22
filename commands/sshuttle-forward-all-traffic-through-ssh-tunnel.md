---
type: command
executor: bash
data: 'sshuttle -r root@localhost:2222 0/0'
output: |-
  root@localhost's password:
  client: Connected.
  Forwarding to 0/0 via 127.0.0.1:2222
platforms:
  - Linux
tags:
  - network
  - tunnel
  - ssh
verified: true
validated: true
---

# sshuttle-forward-all-traffic-through-ssh-tunnel

## Command

```bash
sshuttle -r root@localhost:2222 0/0
```

## Description

This command uses sshuttle to create a transparent proxy that forwards all outgoing IPv4 traffic (0/0) from the local machine through an existing SSH reverse tunnel listening on localhost port 2222. It is particularly useful in penetration testing scenarios for pivoting network access, such as routing traffic through a compromised host (e.g., via a Lan Turtle device) to reach internal networks without direct connectivity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r root@localhost:2222` | Specifies the remote SSH host and port for the tunnel endpoint (e.g., root user connecting to localhost on port 2222 for a reverse tunnel). | Yes |
| `0/0` | The destination network in CIDR notation; 0/0 routes all IPv4 traffic through the tunnel. | Yes |

## Examples

### Basic Usage

```bash
sudo sshuttle -r root@localhost:2222 0/0
```

Enter the SSH password when prompted to establish the tunnel.

### Advanced Usage

```bash
sudo sshuttle -r root@localhost:2222 --dns 0/0 -x 127.0.0.1
```

This variant also forwards DNS queries and excludes local loopback traffic to avoid routing issues.

## Expected Output

```
root@localhost's password:
client: Connected.
Forwarding to 0/0 via 127.0.0.1:2222
```

After entering the password, the tunnel activates. All traffic is now routed through the SSH connection. Verify success by pinging an internal IP (e.g., 10.0.0.1) that was previously unreachable, or check routing with `ip route show`.

## Related

- [[tools/sshuttle]]
- [[procedures/Setup-Lan-Turtle-for-AutoSSH-Reverse-Connection]]
