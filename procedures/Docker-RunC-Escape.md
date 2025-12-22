---
id: 6038c7b2-3a08-49ec-a013-a9392cd6a014
name: Docker-RunC-Escape
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.195954+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
tags:
  - container-escape
  - docker
  - runc
  - cve-2019-5736
commands:
  - '[[commands/docker-build-cve-2019-5736-poc-image]]'
  - '[[commands/docker-run-cve-2019-5736-poc-container]]'
platforms:
  - Linux
tools: []
validated: true
---

# Docker-RunC-Escape

## Summary

This procedure exploits CVE-2019-5736 in the runC component used by Docker to escape from a container and gain root access on the underlying host system. It involves building a malicious Docker image with the exploit payload and running it to overwrite the host's runC binary, allowing arbitrary code execution outside the container isolation.

## Description

CVE-2019-5736 is a vulnerability in runC (versions prior to 1.0-rc6 and 1.0.0-65), the default OCI runtime for Docker, that allows container escapes by overwriting the host's runC binary via a race condition during container startup. An attacker with access to run a container can prepare a malicious image that, upon execution, mounts the host's runC binary into the container and replaces it with shell code. This grants root privileges on the host, bypassing container security controls like namespaces and cgroups. This technique is effective in misconfigured environments where untrusted images can be run, such as multi-tenant cloud setups or development servers. The procedure assumes the attacker has the POC files (Dockerfile and exploit script) available in a local directory.

## Requirements

1. Access to run a Docker container on the target host (user with docker group membership or equivalent).
2. runC version vulnerable to CVE-2019-5736 (pre-1.0-rc6 or specific patches missing).
3. Local POC files: A Dockerfile and exploit script in the directory `./RunC-CVE-2019-5736/malicious_image_POC` (download from public sources like GitHub repos for this CVE).
4. Docker installed on the host.
5. Linux-based host OS (tested on Ubuntu/CentOS).

## Defense

- Update runC to version 1.0-rc6 or later and Docker to patched versions (e.g., 18.09.2+).
- Enforce image signing and scanning with tools like Docker Content Trust or Trivy to prevent malicious images.
- Run containers with minimal privileges: Use non-root users, seccomp profiles, and AppArmor/SELinux.
- Monitor for anomalous host file modifications (e.g., to /usr/bin/runc) and container escapes via audit logs.
- Isolate containers with network policies and limit docker daemon socket access.

## Objectives

1. Build a malicious Docker image containing the CVE-2019-5736 exploit payload.
2. Execute the container to trigger the runC overwrite and escape to the host.
3. Achieve root shell access on the host system for further post-exploitation.

## Instructions

### Step 1: Build Malicious Docker Image

**Context**: Prepare the exploit by building a Docker image from the POC Dockerfile, which includes the malicious runC overwrite script. This step creates the tagged image ready for execution.

**Command** ([[commands/docker-build-cve-2019-5736-poc-image]]):
```bash
docker build -t cve-2019-5736:malicious_image_POC ./RunC-CVE-2019-5736/malicious_image_POC
```

This command uses the Dockerfile in the specified directory to assemble the image. The tag `cve-2019-5736:malicious_image_POC` identifies the exploit image. Success is indicated by Docker confirming the build completion without errors, producing layers including the exploit binary.

### Step 2: Run Exploit Container

**Context**: Launch the malicious container to trigger the CVE-2019-5736 exploit. The container startup process will overwrite the host's runC binary, executing a shell on the host instead of the containerized process.

**Command** ([[commands/docker-run-cve-2019-5736-poc-container]]):
```bash
docker run --rm cve-2019-5736:malicious_image_POC
```

The `--rm` flag auto-removes the container post-execution. Upon running, the exploit activates during the runC initialization, mounting and replacing the host binary. If successful, a root shell prompt appears on the host, confirming the escape.
