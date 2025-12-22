---
id: 48affa3e-4f34-41dd-a294-27042ae9eabd
type: command
executor: bash
data: ssh root@172.16.84.1
output: |-
  root@kali:~# ssh root@172.16.84.1
  The authenticity of host '172.16.84.1 (172.16.84.1)' can't be established.
  ECDSA key fingerprint is SHA256:...
  Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
  root@172.16.84.1's password: sh3llz
created_at: '2023-02-17T02:28:40.491138+00:00'
updated_at: '2023-03-13T19:50:21.945040+00:00'
platforms:
  - Linux
tags:
  - setup
  - ssh
verified: true
validated: true
---

# ssh-lan-turtle-initial-setup

## Command

```bash
ssh root@172.16.84.1
```

## Description

This command establishes an SSH connection to the Lan Turtle device at its default IP address using the default root credentials. It is used during the initial setup to gain shell access for configuration, such as changing the password and enabling internet access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| root@172.16.84.1 | Default username and IP address of the Lan Turtle device (assumes the device is connected via USB and in the 172.16.84.0/24 network) | Yes |

No additional flags are required for basic connection, but standard SSH options like -i for identity files can be added if custom keys are configured later.

## Examples

### Basic Usage

```bash
ssh root@172.16.84.1
```

Connect to the device and enter the default password when prompted.

### Advanced Usage

```bash
ssh -o StrictHostKeyChecking=no root@172.16.84.1
```

Bypasses host key verification for automated setups or first-time connections.

## Expected Output

Upon successful connection, you will see a prompt for the password. After entering 'sh3llz', you gain root shell access to the device:

```
root@kali:~# ssh root@172.16.84.1
The authenticity of host '172.16.84.1 (172.16.84.1)' can't be established.
ECDSA key fingerprint is SHA256:... (example fingerprint).
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
root@172.16.84.1's password: sh3llz
Last login: ... from ...
root@lanturtle:~# 
```

The shell prompt indicates successful access. Immediately change the default password using the `passwd` command for security.

## Related

- [[tools/Lan-Turtle]] (Tool documentation for full setup and usage)
