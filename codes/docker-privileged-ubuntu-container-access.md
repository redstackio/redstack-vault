---
id: 97831f16-ec89-4f75-b47d-746a92ad1af3
name: docker-privileged-ubuntu-container-access
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:19.469060+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - docker
  - privilege-escalation
validated: true
---

# docker-privileged-ubuntu-container-access

## Code

```bash
docker run --rm -it --pid=host --net=host --privileged -v /:/host ubuntu bash
```

## Description

This bash command launches a privileged Ubuntu container that shares the host's PID and network namespaces while mounting the host filesystem. It enables an attacker to access host processes, network interfaces, and files from within the container, facilitating privilege escalation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The command uses fixed flags; customize image or mount point if needed | N/A |

## Usage

Execute directly in a shell with Docker access to gain host visibility. Used in post-exploitation for process migration or network pivoting. Reference in [[procedures/Linux-Docker-Privilege-Escalation]] Step 3.

## Detection

- Docker logs showing --privileged, --pid=host, or --net=host flags.
- Auditd rules for docker.sock access or unusual container spawns.
- Host process monitoring for container-initiated connections to host ports.

## Related

- [[procedures/Linux-Docker-Privilege-Escalation]]
- [[tools/Docker]]
