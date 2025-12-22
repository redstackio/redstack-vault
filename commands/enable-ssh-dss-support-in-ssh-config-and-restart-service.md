---
id: f53ece4a-de38-4ea1-9635-9c3d46d40b35
name: enable-ssh-dss-support-in-ssh-config-and-restart-service
type: command
executor: bash
data: |-
  echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/ssh_config
  echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/sshd_config
  /etc/init.d/ssh restart
output: null
created_at: '2023-04-06T03:56:18.624933+00:00'
updated_at: '2023-04-10T20:34:29.313841+00:00'
platforms:
  - Linux
tags:
  - ssh
  - configuration
verified: true
validated: true
---

# enable-ssh-dss-support-in-ssh-config-and-restart-service

## Command

```bash
echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/ssh_config
echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/sshd_config
/etc/init.d/ssh restart
```

## Description

This command enables support for legacy ssh-dss (DSA) keys in SSH by appending the PubkeyAcceptedKeyTypes directive to both client and server configuration files, then restarts the SSH service to apply the changes. It is used in scenarios involving exploitation of predictable PRNG in older key types, such as during privilege escalation on vulnerable Linux systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/etc/ssh/ssh_config` | Client-side SSH configuration file path | Yes (built-in) |
| `/etc/ssh/sshd_config` | Server-side SSH daemon configuration file path | Yes (built-in) |
| `/etc/init.d/ssh restart` | Service restart script (may vary by distro; alternative: `systemctl restart ssh` ) | Yes (built-in) |

## Examples

### Basic Usage

```bash
echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/ssh_config
echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/sshd_config
/etc/init.d/ssh restart
```

### Advanced Usage (with sudo for safety)

```bash
sudo bash -c 'echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/ssh_config && echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/sshd_config && /etc/init.d/ssh restart'
```

## Expected Output

The echo commands produce no output (silent append). The restart command outputs something like:

```
[ ok ] Restarting ssh (via systemctl): ssh.service.
```

If errors occur (e.g., permission denied), it will show "Permission denied" or service failure messages. Verify success by running `ssh -Q key` and checking for "ssh-dss" in supported types.

## Related

- [[procedures/Linux-Predictable-PRNG-SSH-Key-Privilege-Escalation]]
